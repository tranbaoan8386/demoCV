# Task: LLM CV Parser Integration

## 1. Objective

Implement the LLM-based parsing module to extract structured data from cleaned CV text.

## 2. Required Context

Before writing any code, you MUST read and strictly follow these two files:

- Schema definition: `.github/backend/schemas/llm-extraction-schema.md`
- Engineering rules: `.github/backend/instructions/parser-engineering-rules.md`

## 3. Execution Steps

- **Step 1: Pydantic Models**
  Create `app/schemas/cv_schema.py`. Translate the JSON schema from `llm-extraction-schema.md` into strict Pydantic models. Ensure fields can handle `None` or empty lists `[]` as defined.

- **Step 2: LLM Service Implementation**
  Create `app/services/llm_service.py`. Implement an asynchronous function `extract_cv_data(cleaned_text: str)` that calls the LLM API.
  - Enforce JSON output.
  - Wrap the call in a `try-except` block to handle timeouts/rate limits.
  - Validate the LLM response using the Pydantic models created in Step 1.

- **Step 3: Environment Variables**
  Ensure the API key is loaded via `.env` and `app/core/config.py`. Do not hardcode any credentials.
