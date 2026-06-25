# Backend Architecture Rules

## Role

You are responsible for maintaining a clean, extensible, and maintainable backend architecture.

Every implementation must respect the existing architecture before introducing new abstractions.

Architecture consistency is more important than individual implementation preferences.

---

# Architecture Philosophy

The backend should be designed for long-term maintainability.

Every component should have a clear responsibility.

Avoid unnecessary complexity.

Favor predictable and explicit designs.

Prefer extending the current architecture over replacing it.

---

# Design Principles

Always follow these principles.

## Single Responsibility Principle

Each module should solve one problem.

Avoid modules that mix multiple responsibilities.

---

## Separation of Concerns

Separate:

- API
- Business Logic
- Data Access
- Infrastructure

Each layer should focus on its own responsibility.

---

## Low Coupling

Reduce dependencies between modules.

Modules should communicate through stable interfaces.

Avoid tightly coupled implementations.

---

## High Cohesion

Keep related logic together.

Do not scatter responsibilities across unrelated modules.

---

# Layer Responsibilities

## API Layer

Responsible for:

- HTTP requests
- Request validation
- Response generation
- Dependency injection

The API layer should not contain business logic.

---

## Service Layer

Responsible for:

- Business rules
- Workflow orchestration
- Domain logic

Services coordinate operations.

Services should not perform direct infrastructure work when abstraction already exists.

---

## Repository Layer

Responsible for:

- Data persistence
- Database queries
- CRUD operations

Repositories should not contain business rules.

---

## Infrastructure Layer

Responsible for:

- Storage
- External services
- File systems
- Cloud services
- Messaging
- Third-party integrations

Infrastructure should remain isolated from business logic.

---

## Dependency Rules

Dependencies must always flow inward.

- API may depend on Services.
- Services may depend on Repositories.
- Repositories may depend on Infrastructure.
- Infrastructure must not depend on higher layers.
- Circular dependencies are prohibited.

---

# Module Design

Every module should have a clear purpose.

Before creating a new module, determine whether the functionality belongs to an existing one.

Avoid creating utility modules that become collections of unrelated functions.

---

# Extensibility

Design for extension rather than modification.

New functionality should require minimal changes to existing modules.

Prefer adding new modules instead of rewriting stable components.

---

# Interface Stability

Public interfaces should remain stable.

Avoid changing:

- Function signatures
- Response structures
- Data contracts

unless explicitly approved.

Backward compatibility should be preserved whenever possible.

---

# Data Flow

Data should flow through clearly defined stages.

Every request must be:

- Validated
- Processed by business logic
- Persisted when necessary
- Returned through a well-defined response model

Avoid hidden transformations between layers.

---

# Error Propagation

Errors should propagate through defined layers.

Infrastructure errors should not leak implementation details to API consumers.

Translate internal exceptions into meaningful application responses.

---

# Reusability

Common logic should be extracted only when duplication becomes meaningful.

Avoid premature abstraction.

Do not create generic utilities without multiple real use cases.

---

# Configuration

Configuration should be externalized.

Avoid hardcoded:

- URLs
- Credentials
- Environment-specific values

Use environment variables or configuration management.

---

# Scalability

Architect components so they can evolve independently.

New features should integrate without requiring large architectural changes.

Favor modular growth over monolithic expansion.

---

## Architectural Change Policy

Architectural changes require clear justification.

Before introducing a new pattern, abstraction, or layer, evaluate:

- Existing architectural consistency.
- Long-term maintainability.
- Backward compatibility.
- Impact on dependent modules.

Prefer evolving the current architecture over redesigning it.

---

# Refactoring

Refactor only when it improves:

- Maintainability
- Readability
- Testability
- Extensibility

Avoid refactoring solely for personal preference.

---

## Preferred Architecture Patterns

Prefer:

- Layered architecture.
- Feature-oriented modules.
- Dependency injection.
- Service and repository separation.
- Stable public interfaces.
- Composition over inheritance.
- Explicit dependencies.
- Incremental architectural evolution.
- Stable interfaces.
- Feature-based organization.
- Incremental refactoring.

---

## Architecture Anti-Patterns

Do not:

- Mix responsibilities across layers.
- Bypass service or repository boundaries.
- Introduce circular dependencies.
- Create God objects or God services.
- Couple business logic to infrastructure.
- Introduce unnecessary abstraction.
- Break public interfaces without approval.
- Add architecture that exceeds current requirements.

---

## Architecture Decision Rules

When architectural decisions are required:

- Preserve existing architectural conventions.
- Extend existing modules before introducing new ones.
- Prefer incremental changes over large rewrites.
- Minimize architectural impact.
- Preserve backward compatibility.
- Avoid unnecessary abstractions.
- Prefer explicit dependencies.
- Prioritize maintainability over optimization.

---

# AI Agent Behavior

Before introducing architectural changes:

- Understand the current architecture.
- Identify affected modules.
- Evaluate impact on existing components.
- Preserve established patterns.
- Minimize breaking changes.
- Explain architectural decisions when introducing new abstractions.

Architecture should evolve deliberately, not accidentally.

---

## Non-Goals

This instruction does not:

- Define project-specific implementation details.
- Describe feature requirements.
- Replace project contexts.
- Replace development skills.
- Define project-specific workflows.
