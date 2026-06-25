# Backend AI Guide

This directory contains the AI guidance used for backend development.

All backend development should follow the instructions, skills, and contexts defined in this directory.

---

# Repository Structure

```text
backend/
├── instructions/
├── skills/
├── contexts/
└── prompts/
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

Contexts define:

- Current architecture
- Current implementation
- Project constraints
- Current development status
- Future direction

Contexts should evolve as the project evolves.

---

# Prompts

Prompts define the objective of the current task.

Prompts are temporary and task-specific.

Prompts should not duplicate engineering rules, reusable skills, or project contexts.

---

# Working Process

For every backend task:

1. Apply all relevant instructions.
2. Load the required development skill.
3. Load the required project contexts.
4. Understand the task objective.
5. Analyze the existing implementation.
6. Design the solution.
7. Implement the requested changes.
8. Validate the implementation.
9. Preserve architectural consistency.
10. Preserve backward compatibility unless explicitly approved.

---

# Guiding Principles

Always:

- Preserve existing architecture.
- Follow established engineering rules.
- Reuse existing capabilities whenever possible.
- Maintain consistency across the codebase.
- Produce production-ready implementations.

Never:

- Ignore established instructions.
- Bypass architectural constraints.
- Duplicate project knowledge across multiple documents.
- Mix instructions, skills, contexts, and prompts.
- Introduce unnecessary architectural complexity.
