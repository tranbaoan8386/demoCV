---
name: develop-backend-feature
description: Develop a backend feature while preserving architecture, maintainability, and backward compatibility.
---

# Develop Backend Feature

This skill provides guidance for developing backend features that integrate cleanly with the existing system while maintaining architectural consistency, code quality, and backward compatibility.

This skill defines the standard capability for developing backend features.

---

# When to Use

Use this skill when:

- Creating a new backend feature.
- Extending an existing feature.
- Modifying business logic.
- Introducing new application behavior.

Do not use this skill for project-specific implementation details. Refer to project contexts when domain knowledge is required.

---

# Capability

The AI agent should be able to:

- Analyze feature requirements.
- Design maintainable solutions.
- Preserve architectural consistency.
- Implement production-quality code.
- Validate functional correctness.
- Minimize technical debt.

---

# Approach

Approach every backend feature by:

- Understanding the existing implementation.
- Preserving established architectural patterns.
- Extending existing components whenever appropriate.
- Limiting changes to the requested scope.
- Maintaining consistency with the existing codebase.

---

# Design Principles

Every feature should:

- Solve a single business problem.
- Respect layer responsibilities.
- Minimize coupling.
- Maximize cohesion.
- Preserve stable interfaces.
- Maintain backward compatibility whenever possible.

---

# Implementation Guidelines

During implementation:

- Follow the project's engineering rules.
- Follow the project's architecture rules.
- Reuse existing components whenever appropriate.
- Keep changes localized.
- Avoid duplicated logic.
- Avoid unnecessary abstractions.
- Keep public interfaces stable unless changes are explicitly approved.
- Keep implementations deterministic and predictable.

---

# Validation

Before completion, verify that:

- Functional requirements are satisfied.
- Existing behavior is preserved.
- Error handling is appropriate.
- Input validation is complete.
- Architectural consistency is maintained.
- Required tests have been executed successfully.
- Architectural rules have been respected.

---

# Completion Criteria

A backend feature is complete when:

- The requested functionality has been implemented.
- Existing functionality remains unaffected.
- Architecture remains consistent.
- Code quality standards are satisfied.
- Required validation and testing have passed.
- No unnecessary architectural changes were introduced.

---

# Common Pitfalls

Avoid:

- Implementing before understanding the problem.
- Mixing responsibilities across layers.
- Introducing duplicated business logic.
- Breaking public interfaces.
- Refactoring unrelated modules.
- Introducing unnecessary dependencies.
- Increasing architectural complexity without justification.

---

# Expected Outcome

The completed feature should:

- Integrate naturally with the existing system.
- Preserve maintainability and extensibility.
- Follow established engineering and architectural conventions.
- Be suitable for production deployment.
