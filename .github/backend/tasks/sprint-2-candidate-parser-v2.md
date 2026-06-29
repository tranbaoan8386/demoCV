# Sprint 2 – Candidate Parser v2

## Objective

Extend the Candidate Parser to extract additional candidate information while preserving the existing parser behavior, architecture, and structured output contract.

The implementation must conform to the canonical structured output schema and parsing rules.

---

# Scope

The Candidate Parser is responsible for extracting candidate-related information only.

Fields within the Candidate section include:

- Name
- Email
- Phone
- Address
- GitHub
- LinkedIn
- Portfolio

The parser must not extract information that belongs to other parser domains.

---

# References

This sprint must follow the backend AI guidance.

Required documents:

## Instructions

- backend-engineering-rules.md
- backend-architecture-rules.md

## Skills

- develop-backend-feature
- develop-parser

## Contexts

- backend-project
- parser-architecture
- roadmap

## Schemas

- structured-output-schema
- parsing-rules

These documents define the engineering rules, architecture, project context, structured output, and semantic parsing rules.

---

# Requirements

The implementation must:

- Preserve existing parsing behavior.
- Preserve backward compatibility.
- Maintain the current parser architecture.
- Extend the existing Candidate Parser instead of replacing it.
- Conform to the structured output schema.
- Follow the semantic parsing rules.
- Follow all backend engineering and architecture rules.

---

# Development Process

Follow the standard backend development workflow.

1. Analyze
2. Design
3. Review
4. Approval
5. Implementation
6. Validation
7. Architecture Review
8. Commit

Implementation must not begin before the design has been reviewed and approved.

---

# Expected Deliverables

The sprint is complete when:

- Candidate Parser extracts all required fields.
- Existing extraction behavior is preserved.
- Structured output conforms to the schema.
- Parsing behavior conforms to the parsing rules.
- Required tests pass.
- Regression tests pass.
- Parser architecture remains unchanged.
- Code review has been completed.

---

# Current Status

- Analyze: Pending
- Design: Pending
- Review: Pending
- Approval: Pending
- Implementation: Pending
- Validation: Pending
- Architecture Review: Pending
- Commit: Pending
