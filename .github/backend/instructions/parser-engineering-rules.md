# Parser Engineering Rules (LLM Integration Paradigm)

## Purpose

This document defines the mandatory engineering standards for AI Agents and human developers when implementing the CV parsing system using AI/LLMs.

The goal is to ensure that the system executes secure API calls, guarantees accurate and structured data retrieval, maintains high performance, and remains highly maintainable.

---

## 1. New Parser Architecture (LLM-Based)

The system no longer utilizes fragmented Regex Parsers (such as `DateParser`, `DegreeParser`, etc.). Instead, the architecture is unified and simplified as follows:

```text
Raw PDF/Docx
    │
    ▼
Text Cleaner (Completed: Removes noise, normalizes text)
    │
    ▼
LLM Service (Injects the entire cleaned text into the Prompt)
    │
    ▼
Pydantic Validation (Validates the JSON structure returned by LLM)
    │
    ▼
Database (Stores the final Structured Data)
```

---

## 2. LLM Integration Rules

All source code related to LLM integration MUST comply with the following principles:

- **Structured Output:** API calls must be explicitly configured to enforce JSON format returns (e.g., `response_format={ "type": "json_object" }` for OpenAI or `response_mime_type="application/json"` for Gemini).
- **Strict Validation:** It is mandatory to use `Pydantic` to create data models that map exactly 100% to the schema defined in `llm-extraction-schema.md`. The raw data returned by the LLM MUST pass through Pydantic for validation before being passed to the Controller or Database.
- **Asynchronous Processing:** All LLM API functions must be implemented using `async def` and `await` to prevent blocking the FastAPI event loop.
- **Strict Security:** Absolutely no hardcoded API Keys in the source code. Credentials must be loaded from environment variables (e.g., via `.env` files using `os.getenv()` or FastAPI's `BaseSettings`).

---

## 3. Error Handling & Resilience

LLM APIs are prone to network latency, timeouts, and rate limits. The following resilience measures must be implemented:

- **Exception Wrapping:** Wrap all LLM API calls within `try-except` blocks.
- **Explicit Logging:** Explicitly catch, handle, and accurately log specific exceptions such as `Timeout`, `RateLimitError`, and `JSONDecodeError`.
- **Graceful Degradation:** If the LLM returns malformed JSON or fails, the system must log the specific `cleaned_text` for manual inspection and MUST NOT crash the entire application pipeline.

---

## 4. File Organization

Instead of fragmenting parsing logic across dozens of files, the LLM-based parsing logic should be cleanly consolidated:

```text
app/
 ├── schemas/
 │   └── cv_schema.py       # Contains Pydantic models mapping to llm-extraction-schema.md
 ├── services/
 │   └── llm_service.py     # Contains the core logic for calling OpenAI/Gemini/Claude APIs
 └── core/
     └── config.py          # Manages environment variables (API Keys, Model Names, etc.)
```
