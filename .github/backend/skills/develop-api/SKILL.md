---
name: develop-api
description: Design and implement backend APIs that are consistent, maintainable, secure, and backward compatible.
---

---

# Develop API

This skill defines the standard capability for designing, implementing, and evolving backend APIs while maintaining consistency, reliability, and compatibility.

---

# When to Use

Use this skill when:

- Creating a new API endpoint.
- Extending an existing API.
- Modifying request or response models.
- Introducing new API functionality.
- Refactoring API implementations while preserving behavior.

Do not use this skill for project-specific API contracts. Refer to project contexts for API specifications and business requirements.

---

# Capability

The AI agent should be able to:

- Design clear API contracts.
- Validate incoming requests.
- Produce consistent responses.
- Preserve API compatibility.
- Implement reliable endpoint behavior.
- Maintain API quality over time.

---

# Approach

Approach API development by:

- Understanding the business requirements.
- Designing the API contract before implementation.
- Keeping request and response models explicit.
- Preserving existing API behavior whenever possible.
- Maintaining consistency across all endpoints.

---

# API Design Principles

Every API should:

- Have a clearly defined responsibility.
- Follow consistent request and response structures.
- Validate all external input.
- Return meaningful status codes.
- Handle errors consistently.
- Preserve stable public contracts.

---

# Implementation Guidelines

During implementation:

- Keep business logic outside API handlers.
- Delegate business operations to the service layer.
- Validate input before processing.
- Return standardized responses.
- Avoid exposing internal implementation details.
- Keep endpoint behavior predictable.
- Preserve existing API contracts unless changes are explicitly approved.

---

# Validation

Before completion, verify that:

- Requests are validated correctly.
- Responses follow the expected contract.
- Error handling is consistent.
- Existing API behavior is preserved.
- Security considerations have been addressed.
- Required API tests have passed successfully.

---

# Completion Criteria

An API implementation is complete when:

- Functional requirements have been implemented.
- Request validation is complete.
- Response contracts remain consistent.
- Existing API behavior remains unaffected.
- Required validation and testing have passed.

---

# Common Pitfalls

Avoid:

- Embedding business logic inside API handlers.
- Returning inconsistent response formats.
- Exposing internal exceptions.
- Skipping request validation.
- Breaking existing API contracts.
- Introducing endpoint-specific behavior that violates project conventions.

---

# Expected Outcome

The completed API should:

- Provide a stable public interface.
- Integrate naturally with the existing backend architecture.
- Be easy to maintain and extend.
- Preserve backward compatibility.
- Be suitable for production use.
