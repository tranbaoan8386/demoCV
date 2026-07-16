from __future__ import annotations

import asyncio
import json
import os
import traceback
from typing import Any, List

from google import genai
from pydantic import ValidationError

from app.schemas.cv_schema import CVSchema


GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


async def extract_cv_data(cleaned_text: str, timeout_seconds: int = 90) -> CVSchema:
    """Extract structured CV data from cleaned text using Gemini."""
    if GEMINI_API_KEY is None:
        raise RuntimeError("GEMINI_API_KEY must be configured in environment variables")

    # BƯỚC NGOẶT: Trích xuất cấu trúc Schema thành JSON string để nạp thẳng vào Prompt
    schema_json = json.dumps(CVSchema.model_json_schema(), indent=2)

    prompt = (
        "Extract the candidate CV data from the cleaned text as a valid JSON object. "
        "You MUST conform EXACTLY to the following JSON schema. "
        "Do not invent values or add extra fields. Replace missing fields with null, and empty arrays with [].\n\n"
        f"REQUIRED JSON SCHEMA:\n{schema_json}\n\n"
        f"Cleaned text:\n{cleaned_text}"
    )

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)

        response = await asyncio.wait_for(
            client.aio.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
                config={
                    "response_mime_type": "application/json",
                    # Bỏ parameter response_schema ở đây để tránh lỗi 400 của Google API
                }
            ),
            timeout=timeout_seconds
        )

        raw_json_str = response.text
        
        # Tiền xử lý: Dọn dẹp thẻ markdown code block
        raw_json_str = raw_json_str.strip()
        if raw_json_str.startswith("```json"):
            raw_json_str = raw_json_str[7:]
        if raw_json_str.startswith("```"):
            raw_json_str = raw_json_str[3:]
        if raw_json_str.endswith("```"):
            raw_json_str = raw_json_str[:-3]
        raw_json_str = raw_json_str.strip()

        raw_json = json.loads(raw_json_str)

        # Pydantic sẽ validate cấu trúc
        return CVSchema.model_validate(raw_json)

    except asyncio.TimeoutError as exc:
        raise RuntimeError(f"Gemini request timed out after {timeout_seconds}s") from exc
    
    except json.JSONDecodeError as exc:
        print(f"\n[LLM ERROR] Chuỗi lỗi không phải JSON:\n{raw_json_str}\n")
        raise ValueError("Gemini returned malformed JSON") from exc
        
    except ValidationError as exc:
        print(f"\n[PYDANTIC ERROR] Chi tiết lệch Schema:\n{exc}")
        print(f"\n[RAW JSON TỪ GEMINI]:\n{raw_json_str}\n")
        raise ValueError("Gemini response did not match CV schema") from exc
        
    except Exception as exc:
        traceback.print_exc() 
        raise RuntimeError(f"Unexpected error while calling Gemini: {str(exc)}") from exc


async def generate_embedding(text: str, timeout_seconds: int = 30) -> List[float]:
    """
    Generate a 768-dimensional embedding for the given text using Gemini.
    Returns a list[float] of length 768 on success.
    """
    if GEMINI_API_KEY is None:
        raise RuntimeError("GEMINI_API_KEY must be configured in environment variables")

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)

        # 1. Cập nhật tên model thành "gemini-embedding-001"
        # 2. Ép đầu ra về đúng 768 chiều để vượt qua bước check validate của bạn
        response = await asyncio.wait_for(
            client.aio.models.embed_content(
                model="gemini-embedding-001",
                contents=text,
                config={"output_dimensionality": 768} 
            ),
            timeout=timeout_seconds,
        )

        # Trích xuất vector embedding chuẩn từ SDK mới
        embedding_vector = None
        if hasattr(response, "embedding") and response.embedding:
            embedding_vector = response.embedding.values
        elif hasattr(response, "embeddings") and response.embeddings:
            embedding_vector = response.embeddings[0].values

        if embedding_vector is None:
            raise RuntimeError("Could not extract embedding from Gemini response")

        # Đảm bảo định dạng kiểu số thực và kiểm tra số chiều (dimension)
        embedding_vector = [float(x) for x in embedding_vector]
        if len(embedding_vector) != 768:
            raise ValueError(f"Unexpected embedding dimension: {len(embedding_vector)}")

        return embedding_vector

    except asyncio.TimeoutError as exc:
        raise RuntimeError(f"Gemini embedding request timed out after {timeout_seconds}s") from exc
    except Exception as exc:
        traceback.print_exc()
        raise RuntimeError(f"Unexpected error while generating embedding: {str(exc)}") from exc