# Backend Project Context

## Project Overview

DEMOCV1 is an AI-powered backend system for extracting structured information from uploaded CV documents.

The backend receives uploaded PDF files, extracts raw text, transforms unstructured content into structured data, and stores the results for future processing.

The project is designed with modularity, maintainability, and extensibility as primary goals.

---

# Technology Stack

## Backend

- Python
- FastAPI

## Database

- PostgreSQL

## Object Storage

- MinIO

## PDF Processing

- PyMuPDF

## Containerization

- Docker
- Docker Compose

---

# Architecture Overview

The backend follows a layered architecture.

Application responsibilities are separated into:

- API Layer
- Service Layer
- Repository Layer
- Infrastructure Layer

Business logic should remain independent from infrastructure concerns.

---

# Core Backend Responsibilities

The backend is responsible for:

- Receiving uploaded CV files.
- Persisting uploaded files.
- Extracting raw text from PDF documents.
- Transforming raw text into structured information.
- Persisting structured data.
- Providing structured data through APIs.

---

# Processing Pipeline

The current document processing pipeline is:

PDF Upload

↓

Store File

↓

Extract Raw Text

↓

Parse Structured Data

↓

Persist Structured Data

↓

Return Processing Result

Every stage should remain independent and replaceable.

---

# Data Storage

The backend stores:

- Uploaded file metadata.
- Raw extracted text.
- Structured parsing results.
- Processing status.

Structured data should remain independent from raw extracted text.

---

# Project Structure

The project is organized around clear architectural boundaries.

Key areas include:

- API
- Services
- Repositories
- Database Models
- Parser Modules
- Infrastructure
- Configuration

Each area has a single primary responsibility.

---

# Design Principles

The backend is designed to support:

- Incremental feature development.
- Independent module evolution.
- Backward compatibility.
- Testability.
- Long-term maintainability.

New functionality should extend the existing architecture rather than replace it.

---

# Integration Principles

Backend components should communicate through well-defined interfaces.

Implementation details should remain encapsulated within their respective layers.

Dependencies should remain predictable and consistent.

---

# Current Development State

The backend currently supports:

- File upload.
- PDF text extraction.
- Raw text persistence.
- Structured data persistence.
- Modular parser architecture.

Additional extraction capabilities will be introduced incrementally without redesigning the existing architecture.

---

# Long-Term Direction

The backend is intended to evolve into a modular AI document processing platform capable of supporting:

- Additional document parsers.
- AI-assisted extraction.
- Intelligent document analysis.
- Candidate evaluation.
- Search and matching capabilities.

Future development should preserve architectural consistency while allowing incremental expansion.
