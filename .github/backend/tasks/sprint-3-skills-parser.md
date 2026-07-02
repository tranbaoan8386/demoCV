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

## Parsing Flow

The Skills Parser processes candidate skills using the following pipeline:

1. Extract explicitly declared skills from the Skills section.
2. Detect additional skills from other supported sections.
3. Remove duplicated skills between declared and detected.
4. Normalize skill names according to `parsing-rules.md`.
5. Produce the final structured output.

Pipeline:

Raw CV
│
├──────────────┐
│ │
Skills Other Sections
│ │
declared detected
│ │
└───┬────┘
▼
normalization
▼
normalized

### declared

Extract skills explicitly listed by the candidate within the **Skills** section.

Rules:

- Only parse the Skills section.
- Preserve the original spelling.
- Preserve the original casing.
- Preserve the original ordering.
- Do not normalize values in `declared`.

### detected

Detect skills from the following sections only:

- Summary
- Experience
- Projects
- Certifications

Rules:

- Never scan the Skills section.
- Only include skills not already present in `declared`.
- Preserve the first detected occurrence.
- Do not normalize values in `detected`.

### normalized

Normalization algorithm:

1. Combine `declared` and `detected`.
2. Remove duplicate skills.
3. Normalize each skill according to `parsing-rules.md`.
4. Remove duplicates introduced by normalization.
5. Return the normalized skill list.

The normalized output:

- must be lowercase where defined by the parsing rules;
- must contain unique values only;
- must not modify `declared` or `detected`.

Normalization Examples

Input

HTML5
HTML

↓

html

CSS3
CSS

↓

css

ReactJS
React.js
React

↓

react

NodeJS
Node.js
Node

↓

nodejs

NextJS
Next.js

↓

## nextjs

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

## Parser Responsibilities

The Skills Parser is responsible only for:

- extracting skills;
- detecting additional skills;
- normalizing skill names.

The Skills Parser must not:

- parse education;
- parse projects;
- parse experience;
- modify candidate information;
- modify parser orchestration.

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
