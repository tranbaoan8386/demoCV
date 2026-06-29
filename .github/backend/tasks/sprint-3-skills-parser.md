# Sprint 3 – Skills Parser

## Objective

Implement the Skills Parser to extract, detect, and normalize candidate skills while preserving the existing parser architecture and behavior.

---

## Scope

The Skills Parser should produce the following structured output:

```json
{
  "skills": {
    "declared": [],
    "detected": [],
    "normalized": []
  }
}
```

---

## Parsing Requirements

The implementation must follow:

- `structured-output-schema.md`
- `parsing-rules.md`

### declared

Extract skills explicitly listed by the candidate within the **Skills** section.

### detected

Detect skills from other CV sections, including:

- Summary
- Experience
- Projects
- Certifications

Do not duplicate skills that already exist in `declared`.

### normalized

Produce a normalized skill set derived from both:

- declared
- detected

Normalization must:

- Merge both collections.
- Remove duplicate skills.
- Convert equivalent skill names into the normalized identifier defined by the parsing rules.
- Produce a stable output suitable for search, filtering, and future matching.

---

## Requirements

The implementation must:

- Preserve the existing parser architecture.
- Preserve backward compatibility.
- Extend the existing Skills Parser instead of replacing it.
- Keep parser responsibilities independent.
- Follow all backend engineering and architecture rules.
- Follow the structured output schema exactly.
- Follow the parsing rules exactly.

---

## Development Process

Follow the standard backend development workflow:

- Analyze
- Design
- Review
- Approval
- Implementation
- Validation
- Architecture Review
- Commit

Implementation must not begin before the design has been reviewed and approved.

---

## Expected Deliverables

The sprint is complete when:

- Declared skills are extracted correctly.
- Detected skills are extracted correctly.
- Normalized skills are generated correctly.
- Existing parser behavior is preserved.
- Regression tests pass.
- Parser architecture remains unchanged.
- Code review has been completed.
- Structured output conforms to structured-output-schema.md.\
- Parsing behavior conforms to parsing-rules.md.

---

## Out of Scope

The following are not part of this sprint:

- AI/LLM-based skill extraction.
- Skill confidence scoring.
- Skill proficiency estimation.
- JD matching.
- Skill ranking or recommendation.
- Machine learning models.

---

## Files Expected to Change

Typical files include:

- skill_parser.py
- regex_utils.py (if shared parsing utilities are required)
- parser.py (only if parser registration is required)
- test_skill_parser.py
- test_cv_parser_architecture.py (if regression coverage needs to be extended)

Changes should remain localized to the Skills Parser whenever possible.

---

## Current Status

- Analyze: Pending
- Design: Pending
- Review: Pending
- Approval: Pending
- Implementation: Pending
- Validation: Pending
- Architecture Review: Pending
- Commit: Pending
