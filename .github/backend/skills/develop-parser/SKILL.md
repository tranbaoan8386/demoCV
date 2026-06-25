---
name: develop-parser
description: Develop parser modules that extract structured information accurately while preserving maintainability, extensibility, and backward compatibility.
---

---

# Develop Parser

This skill defines the standard capability for designing, implementing, and extending parser modules that transform unstructured input into structured data.

---

# When to Use

Use this skill when:

- Creating a new parser.
- Extending an existing parser.
- Improving extraction accuracy.
- Supporting new document formats.
- Refactoring parser logic while preserving behavior.

Do not use this skill for project-specific parser implementations. Refer to project contexts for parser architecture, data schemas, and project requirements.

---

# Capability

The AI agent should be able to:

- Analyze unstructured input.
- Design maintainable extraction strategies.
- Produce consistent structured output.
- Preserve parser reliability.
- Extend existing parsers safely.
- Maintain backward compatibility.

---

# Approach

Approach parser development by:

- Understanding the structure of the input data.
- Identifying reliable extraction patterns.
- Prioritizing deterministic extraction over heuristic assumptions.
- Extending existing parser behavior whenever appropriate.
- Maintaining consistent output structures.

---

# Parser Design Principles

Every parser should:

- Focus on a single extraction responsibility.
- Produce deterministic results whenever possible.
- Remain independent from unrelated parsing logic.
- Handle incomplete or missing data gracefully.
- Avoid assumptions that cannot be validated.
- Preserve stable output contracts.

---

# Implementation Guidelines

During implementation:

- Reuse existing parsing utilities whenever appropriate.
- Keep extraction logic modular and easy to extend.
- Separate pattern matching from data transformation.
- Avoid duplicated parsing logic.
- Avoid embedding project-specific business rules.
- Keep parser behavior predictable and transparent.
- Preserve existing parser interfaces unless changes are explicitly approved.

---

# Validation

Before completion, verify that:

- Extraction results are accurate.
- Structured output remains consistent.
- Existing parser behavior is preserved.
- Edge cases are handled appropriately.
- Invalid or incomplete input is handled safely.
- Required parser tests have passed successfully.

---

# Completion Criteria

A parser is complete when:

- Required information is extracted correctly.
- Structured output matches the expected schema.
- Existing extraction behavior remains unaffected.
- Parser quality and maintainability standards are satisfied.
- Required validation and testing have passed.

---

# Common Pitfalls

Avoid:

- Mixing multiple parsing responsibilities.
- Creating fragile extraction patterns.
- Duplicating parsing logic.
- Embedding business logic inside parsers.
- Changing output structures without approval.
- Ignoring malformed or incomplete input.
- Introducing unnecessary parser complexity.

---

# Expected Outcome

The completed parser should:

- Produce reliable structured output.
- Integrate naturally with the existing parser architecture.
- Be easy to extend and maintain.
- Preserve backward compatibility.
- Be suitable for production use.
