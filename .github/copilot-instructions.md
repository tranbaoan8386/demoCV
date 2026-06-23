# DemoCV1 Project Instructions

## Project Purpose

DemoCV1 is a learning project focused on:

- AI Engineering workflows
- FastAPI backend development
- PostgreSQL
- MinIO object storage
- CV parsing and matching systems

## Development Philosophy

Prefer:

1. Prompt
2. Context
3. Skill
4. Instruction

Avoid over-engineering.

Only introduce Skill or Instruction when they provide reusable value.

## Current Architecture

Backend:

- FastAPI
- SQLAlchemy
- PostgreSQL
- MinIO

Frontend:

- React
- TypeScript

Infrastructure:

- Docker Compose

## Architecture Principles

Use separation of concerns.

Preferred layers:

- API Layer
- Service Layer
- Repository Layer
- Storage Layer

Avoid putting business logic directly in API routes.

## Existing Infrastructure

The following infrastructure already exists:

- PostgreSQL container
- MinIO container
- FastAPI application
- SQLAlchemy configuration

Do not recreate infrastructure unless explicitly requested.

## AI Engineering Workflow

Before implementing a feature:

1. Read project instructions.
2. Read relevant feature context.
3. Design the feature.
4. Validate architecture.
5. Implement incrementally.

Do not skip design for non-trivial features.
