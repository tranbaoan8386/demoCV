# Backend AI Guide

This directory contains the AI guidance used for backend development.

All backend development should follow the instructions, skills, contexts, schemas, and tasks defined in this directory.

---

# Repository Structure

```text
backend/
├── instructions/
├── skills/
├── contexts/
├── schemas/
└── tasks/
```

Each directory has a distinct responsibility and should not overlap with the others.

---

# Instructions

Instructions define project-independent engineering and architectural rules.

Always apply these rules during backend development.

Current instructions:

- backend-engineering-rules.md
- backend-architecture-rules.md

Instructions define:

- Engineering standards
- Architectural standards
- Preferred patterns
- Anti-patterns
- Decision rules

Instructions should remain stable and reusable across backend projects.

---

# Skills

Skills define reusable development capabilities.

Load the appropriate skill before implementing a task.

Current skills:

- develop-backend-feature
- develop-parser
- develop-api
- develop-database

Skills define:

- Capability
- Approach
- Design principles
- Implementation guidance
- Validation
- Completion criteria

Skills should remain independent from project-specific knowledge.

---

# Contexts

Contexts describe the current backend project.

Load the required context before making implementation decisions.

Current contexts:

- backend-project
- parser-architecture
- backend-roadmap
- development-environment

Contexts define:

- Current architecture
- Current implementation
- Project constraints
- Current development status
- Future direction

Contexts should evolve as the project evolves.

---

# Schemas

Schemas define the canonical data structures and semantic rules used by the backend.

Load the required schemas before implementing parser logic or modifying structured outputs.

Current schemas:

- structured-output-schema
- parsing-rules

Schemas define:

- Structured output
- Field definitions
- Field ownership
- Semantic meaning
- Data constraints
- Classification rules

Parser implementations must conform to the defined schemas.

Schemas represent the source of truth for structured data.

---

# tasks

tasks define the objective of the current task.

tasks are temporary and task-specific.

tasks should not duplicate engineering rules, reusable skills, or project contexts.

---

# Working Process

For every backend task:

1. Apply all relevant instructions.
2. Load the required development skills.
3. Load the required project contexts.
4. Load the required schemas.
5. Understand the task objective.
6. Analyze the existing implementation.
7. Design the solution.
8. Implement the requested changes.
9. Validate the implementation.
10. Preserve architectural consistency.
11. Preserve backward compatibility unless explicitly approved.

---

# Guiding Principles

Always:

- Preserve existing architecture.
- Follow established engineering rules.
- Reuse existing capabilities whenever possible.
- Maintain consistency across the codebase.
- Produce production-ready implementations.
- Follow the canonical data schemas.

Never:

- Ignore established instructions.
- Bypass architectural constraints.
- Duplicate project knowledge across multiple documents.
- Mix instructions, skills, contexts, schemas, and tasks.
- Introduce unnecessary architectural complexity.
