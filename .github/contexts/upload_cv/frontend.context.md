# Upload CV Frontend Context

## Feature Overview

Upload CV allows users to upload PDF resumes through the user interface.

## Existing Backend

Backend API already exists.

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

Use the real backend.

Do not use mock data.

---

## User Flow

1. User selects a PDF file.
2. User clicks Upload.
3. Frontend calls backend API.
4. Show loading state.
5. Show success state.
6. Show error state.

---

## UI Requirements

Display:

- selected filename
- upload status
- upload result
- error message

---

## Technical Stack

- React
- TypeScript
- Vite
- Tailwind CSS

Use:

VITE_API_URL

Do not hardcode backend URLs.

---

## Non Goals

Do not implement:

- CV List
- CV Detail
- CV Parsing
- AI Extraction
- Candidate Profile
- Matching
