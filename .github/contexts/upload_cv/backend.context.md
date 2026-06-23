# Upload CV Backend Context

## Feature Overview

Upload CV allows users to upload PDF resumes into the system.

## Current System State

Infrastructure already exists and is already configured:

- FastAPI
- PostgreSQL
- SQLAlchemy
- MinIO
- Docker Compose

Do not recreate infrastructure.

Do not redesign infrastructure.

Use the existing infrastructure.

---

## User Flow

1. User uploads a PDF file.
2. Backend validates file type.
3. Backend stores PDF in MinIO.
4. Backend creates a CV record in PostgreSQL.
5. Backend returns CV metadata.

---

## API

POST /cvs/upload

Request:

multipart/form-data

Field:

- file

Response:

{
"id": 1,
"original_filename": "cv.pdf",
"object_name": "cvs/uuid-cv.pdf",
"status": "UPLOADED",
"created_at": "2026-06-23T10:00:00"
}

---

## Database

Table:

cvs

Fields:

- id
- original_filename
- object_name
- status
- created_at

Status values:

- UPLOADED

---

## Storage

MinIO bucket:

cvbucket

Object path:

cvs/{uuid}-{filename}.pdf

---

## Non Goals

Do not implement:

- CV parsing
- AI extraction
- Candidate profile generation
- Matching
- Background jobs
- Queue systems

These belong to future phases.
