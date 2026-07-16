---
name: develop-embedding
description: Process post-extraction CV data by flattening JSONB, generating 768-dimensional vector embeddings via Google Gemini API, and handling asynchronous persistence in PostgreSQL using pgvector.
---

# Develop Embedding

This skill defines the standard capability for handling post-extraction resume data, transforming structured JSONB data into meaningful text, generating vector representations using advanced LLM embedding models, and managing vector persistence in PostgreSQL.

---

# When to Use

Use this skill when:

- Creating new vector database models or extending tables to store embeddings.
- Implementing data flattening logic for structured JSON payloads (CV/JD).
- Integrating Google GenAI SDK for `text-embedding-004` model interactions.
- Writing asynchronous pipelines to bridge data extraction and vector persistence.
- Setting up vector similarity indexes (e.g., HNSW) within the persistence layer.

Do not use this skill for raw PDF text parsing or high-level matching interface logic. Refer to `develop-parser` or project-specific matching handlers for those capabilities.

---

# Capability

The AI agent should be able to:

- Design decoupled vector tables maintaining a strict relation to source entities.
- Transform complex nested JSON data into clean, semantic text strings optimized for LLM token efficiency.
- Handle asynchronous network requests to Google GenAI API efficiently without blocking the event loop.
- Apply transactional integrity practices (`try-except` with rollback) when writing heavy vector arrays to PostgreSQL.
- Maintain consistency across ORM models, schemas, and indexing structures.

---

# Approach

Approach embedding development by:

- Adopting a decoupled table strategy (1-1 or 1-N relationship) to isolate heavy vector arrays from operational text data.
- Enforcing semantic parsing hierarchy (Title -> Summary -> Skills -> Work Experience -> Projects) to ensure text alignment with AI models.
- Executing database interactions asynchronously (`async/await`) to support high-concurrency workloads.
- Applying strict transactional control to guarantee zero orphan embeddings.

---

# Data Pipeline Principles

Every vector pipeline change should:

- **Be Decoupled:** Keep administrative data tables light; isolate vector writes.
- **Be Type-Safe:** Validate the fixed 768-dimensional array constraint required by the model.
- **Ensure Idempotency:** Support safe re-runs or updates to the same source ID without corrupting state.
- **Fail Gracefully:** Isolate external API exceptions without halting core database processes.

---

# Implementation Guidelines

### Technical Specifications

- **Target Table:** `cv_embeddings` (Linked to `cvs.id` via Foreign Key `ON DELETE CASCADE`).
- **Data Field:** `embedding vector(768)` using `pgvector.sqlalchemy`.
- **Index Strategy:** `HNSW` using `vector_cosine_ops`.
- **Model Target:** Google GenAI SDK -> `text-embedding-004`.

### Code Implementation Tasks

- **Task 1 (ORM Definition):** Create the `CVEmbedding` class model with an explicit foreign key pointing to the existing `CV` model.
- **Task 2 (Flattening Logic):** Write a utility function `flatten_cv_data(structured_data: dict) -> str` that recursively builds an optimized plaintext block.
- **Task 3 (Inference Execution):** Implement the client logic to retrieve embeddings from `client.models.embed_content`.
- **Task 4 (Workflow Hook):** Integrate the final service method inside a FastAPI background execution pipeline or sequential route logic, triggered right after a CV status shifts to `COMPLETED`.

---

# Validation

Before completion, verify that:

- The `CVEmbedding` ORM entity is mapped correctly with no linting or type violations.
- Empty or incomplete fields within `structured_data` are handled without raising script exceptions.
- Database rollback procedures successfully discard partial transactions if the Gemini API errors out.
- The vector format stored in PostgreSQL matches the expected array shape and can be queried via DBeaver.

---

# Completion Criteria

An embedding feature task is complete when:

- The operational model successfully logs the 768-dimension values.
- Table indexing structures are correctly declared to ensure ultra-low lookup latency.
- The implementation cleanly merges with the project's existing Clean Architecture design conventions.

---

# Common Pitfalls

Avoid:

- Mutating the current `cvs` database table schema schema.
- Running heavy model APIs synchronously inside production FastAPI handlers.
- Letting failing external network loops corrupt local database states (missing rollbacks).
- Including generic metadata (timestamps, UUIDs) inside the semantic flattening layer.

---

# Expected Outcome

The completed embedding service implementation should:

- Effortlessly encode raw parsed components into mathematical coordinates.
- Maintain optimal database sizing and performance scaling thresholds.
- Provide an accessible, scalable vector substrate ready for cross-table matching operations.
