# Upload CV Context

## Feature Overview

Upload CV allows users to upload PDF resumes into the system.

## Current System State

Infrastructure already exists:

- FastAPI backend is running.
- PostgreSQL is running in Docker.
- Database name: cvdb.
- SQLAlchemy is configured and connected.
- MinIO is running in Docker.
- Basic CV model already exists for testing.

Do not create infrastructure from scratch.

## User Flow

1. User selects a PDF file.
2. User clicks Upload.
3. Backend validates file type.
4. Backend uploads file to MinIO.
5. Backend creates a CV record in PostgreSQL.
6. Backend returns uploaded file metadata.

## Database

Table: cvs

Fields:

- id
- original_filename
- object_name
- status
- created_at

Status values:

- UPLOADED

## API Requirements

POST /cvs/upload

Request:

- PDF file

Response:

- id
- original_filename
- object_name
- status
- created_at

## Technical Requirements

- Use existing FastAPI application.
- Use existing SQLAlchemy configuration.
- Use existing PostgreSQL database (cvdb).
- Use existing MinIO instance.
- Do not create Docker configuration.
- Do not create database infrastructure.

## Non Goals

- No CV parsing.
- No AI extraction.
- No candidate profile creation.
- No background jobs.

These features will be implemented in later phases.
