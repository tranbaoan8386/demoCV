---
name: develop-database
description: Design, modify, and maintain the persistence layer while preserving data integrity, consistency, and backward compatibility.
---

---

# Develop Database

This skill defines the standard capability for designing, modifying, and maintaining the persistence layer while ensuring data integrity, consistency, maintainability, and compatibility.

---

# When to Use

Use this skill when:

- Creating new database models.
- Modifying existing schemas.
- Designing relationships between entities.
- Implementing database migrations.
- Refactoring the persistence layer.
- Optimizing database access patterns.

Do not use this skill for project-specific database schemas or business entities. Refer to project contexts for domain-specific information.

---

# Capability

The AI agent should be able to:

- Design maintainable database schemas.
- Preserve data integrity.
- Maintain backward compatibility.
- Implement safe schema evolution.
- Optimize persistence without sacrificing maintainability.
- Keep database changes consistent with the application architecture.

---

# Approach

Approach database development by:

- Understanding existing data models before making changes.
- Preserving existing data whenever possible.
- Designing schema changes incrementally.
- Maintaining consistency between application models and persistence.
- Minimizing the impact of schema evolution.

---

# Database Design Principles

Every database change should:

- Represent the business domain clearly.
- Preserve referential integrity.
- Minimize data duplication.
- Support future extensibility.
- Avoid unnecessary complexity.
- Maintain stable data contracts whenever possible.

---

# Implementation Guidelines

During implementation:

- Keep schema changes focused.
- Design reversible database migrations.
- Preserve existing data whenever possible.
- Avoid destructive changes without explicit approval.
- Keep persistence logic separated from business logic.
- Maintain consistency between models, migrations, and repositories.
- Avoid introducing unnecessary database complexity.

---

# Validation

Before completion, verify that:

- Database schema is valid.
- Relationships are correctly defined.
- Existing data remains consistent.
- Migrations execute successfully.
- Rollback procedures are available when appropriate.
- Required database tests have passed successfully.

---

# Completion Criteria

A database change is complete when:

- Schema changes satisfy the requested requirements.
- Existing data integrity is preserved.
- Migrations execute successfully.
- Backward compatibility has been considered.
- Persistence remains consistent with the application architecture.

---

# Common Pitfalls

Avoid:

- Breaking existing schemas without approval.
- Creating unnecessary relationships.
- Introducing duplicated data.
- Embedding business logic inside the persistence layer.
- Writing irreversible migrations without justification.
- Optimizing prematurely.
- Ignoring migration compatibility across environments.

---

# Expected Outcome

The completed database implementation should:

- Preserve data integrity.
- Support future application growth.
- Integrate naturally with the existing architecture.
- Remain easy to maintain and evolve.
- Be suitable for production use.
