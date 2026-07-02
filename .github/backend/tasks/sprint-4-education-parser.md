# Sprint 4 – Education Parser

## Objective

Implement the Education Parser to extract structured education information while preserving the existing parser architecture and behavior.

---

## Scope

The Education Parser should produce the following structured output:

```json
{
  "education": [
    {
      "institution": "",
      "degree": "",
      "major": "",
      "start_date": "",
      "end_date": "",
      "gpa": "",
      "location": "",
      "description": ""
    }
  ]
}
```

---

## Parsing Requirements

The implementation must follow:

- Backend Engineering Rules
- Parser Engineering Rules
- Parser Architecture
- Develop Parser Skill
- structured-output-schema.md
- parsing-rules.md

---

## Expected Parser Composition

The Education Parser should act as an orchestrator.

Processing flow:

Education Section
↓
Section Locator
↓
Entry Splitter
↓
Entry Preprocessor
↓
Line Labeler
↓
Output Builder

The parser must remain modular and easy to extend.

Individual detectors should not build the final output directly.
Instead, detectors are responsible only for identifying whether a normalized line represents a specific field.

---

## Internal Data Flow

Each education entry should be processed through the following stages:

Raw Education Entry
↓
Entry Preprocessor
↓
Normalized Lines
↓
Line Labeler
↓
Labeled Lines
↓
Output Builder
↓
Structured Education Record

Each stage has a single responsibility and should not bypass later stages.

---

## Supported Fields

Each education entry may contain:

- institution
- degree
- major
- start_date
- end_date
- gpa
- location
- description

Rules:

- Preserve the original text.
- Preserve the original ordering.
- Do not infer missing values.
- Use empty strings for unavailable fields.
- Ignore unsupported information.

---

### Education Section

Locate the candidate's education section.

Rules:

- Only parse the Education section.
- Ignore unrelated sections.
- Support common education section titles.
- Preserve the original order of entries.

---

### Education Entries

Split the Education section into one or more education records.

Rules:

- Support single education entry.
- Support multiple education entries.
- Preserve the original ordering.

---

### Field Extraction

Extract supported fields from each education entry.

Supported fields:

- institution
- degree
- major
- start_date
- end_date
- gpa
- location
- description

Rules:

- Extract only information explicitly present in the CV.
- Missing fields must be returned as empty strings.
- Never infer or hallucinate values.
- Preserve original text unless normalization is required by parsing rules.

---

## Requirements

The implementation must:

- Extend the existing Education Parser.
- Preserve backward compatibility.
- Follow all parser engineering documentation.
- Conform to the structured output schema.
- Conform to the parsing rules.

---

## Expected Deliverables

The sprint is complete when:

- Education entries are extracted correctly.
- Multiple education records are supported.
- Missing optional fields are handled correctly.
- Supported education fields are extracted correctly.
- Existing parser behavior is preserved.
- Regression tests pass.
- Code review has been completed.
- Structured output conforms to `structured-output-schema.md`.
- Parsing behavior conforms to `parsing-rules.md`.

---

## Out of Scope

The following are not part of this sprint:

- AI/LLM-based education extraction.
- Degree normalization.
- School normalization.
- GPA scoring.
- Education ranking.
- Academic evaluation.
- Machine learning models.

---

## Files Expected to Change

Typical files include:

- parser.py
- entry_parser.py
- entry_preprocessor.py
- line_labeler.py
- output_builder.py
- institution_detector.py
- degree_detector.py
- major_detector.py
- date_detector.py
- gpa_detector.py
- location_detector.py
- description_extractor.py
- test_education_parser.py

Changes should remain localized to the Education Parser whenever possible.

---

### Entry Preprocessor

Responsibilities:

- Normalize an education entry.
- Remove empty lines.
- Normalize whitespace.
- Split inline separators when appropriate (e.g. '|', '•').
- Produce an ordered list of normalized lines.

---

### Line Labeler

Responsibilities:

For every normalized line:

- determine whether it represents
  - institution
  - degree
  - major
  - date
  - GPA
  - location
  - description

The Line Labeler coordinates all detectors.

Detectors should not modify parser output directly.

---

### Detector Responsibilities

Each detector evaluates a single normalized line.

A detector is responsible only for determining whether a line matches its own field.

Detectors must not:

- build the final education record
- modify parser output
- infer values for other fields

The Line Labeler coordinates all detectors and assigns labels to each normalized line.

---

### Output Builder

Responsibilities:

Transform labeled lines into the structured Education schema.

Output Builder is the only component responsible for constructing the final JSON.

---

### Conflict Resolution

When multiple detectors classify the same normalized line.
The Line Labeler coordinates the conflict resolution process.

Conflict resolution determines the final label(s) assigned to each normalized line before they are consumed by the Output Builder.

Conflict resolution may use:

- detector priority
- rule precedence
- contextual information
- confidence scores (future extension)

The Output Builder should consume resolved labels only and
must not perform conflict resolution itself.
