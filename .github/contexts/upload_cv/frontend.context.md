# Upload CV Frontend Context

## Feature Overview

Upload CV allows users to upload PDF resumes to the backend system.

## Existing Backend API

POST /cvs/upload

Request:

- multipart/form-data
- field name: file

Response:

- id
- original_filename
- object_name
- status
- created_at

## Current Frontend Stack

- React
- TypeScript
- Vite

## Architecture Requirements

Use:

- Page Component
- Custom Hook
- Service Layer
- Presentational Components

Keep business logic out of UI components.

## User Flow

1. User selects a PDF file.
2. User clicks Upload.
3. Frontend calls POST /cvs/upload.
4. Show loading state.
5. Show upload success result.

## Success State

Display:

- original_filename
- status
- created_at

## Error State

Display upload error message.

## Non Goals

- No CV List
- No CV Detail
- No CV Parsing
- No AI Extraction
