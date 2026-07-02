# Parser Engineering Rules

## Purpose

This document defines the engineering standards for implementing all parsers in the project.

These rules ensure that every parser remains maintainable, extensible, testable, and consistent across the entire parsing pipeline.

All parser implementations must follow these rules.

---

# 1. Parser Responsibilities

A parser is responsible for transforming unstructured text into structured data.

A parser must:

- locate the target information;
- extract supported fields;
- return structured output defined by the project schema.

A parser must not:

- infer unsupported information;
- modify unrelated parser outputs;
- contain business logic unrelated to parsing;
- modify parser orchestration outside its own responsibility.

---

# 2. Parser Architecture

Every parser must follow the same high-level architecture.

```
Raw Text
    │
    ▼
Section Locator
    │
    ▼
Entry Splitter
    │
    ▼
Field Parsers
    │
    ▼
Structured Output
```

Responsibilities must remain separated.

---

# 3. Parser Composition

The top-level parser is an orchestration layer.

Its responsibility is limited to:

- locating sections;
- splitting entries;
- coordinating field parsers;
- assembling the final output.

The top-level parser should not contain complex extraction logic.

---

# 4. Single Responsibility

Each parsing component must have only one responsibility.

Examples:

- Date Parser
- Institution Parser
- Degree Parser
- Major Parser
- GPA Parser

Each component extracts only its own field.

A component must not extract multiple unrelated fields.

---

# 5. Progressive Parsing

Parsing should be performed progressively.

Recommended workflow:

1. Identify the parsing scope.
2. Split into entries.
3. Parse fields independently.
4. Assemble the final object.

Avoid implementing large monolithic parsing functions.

---

# 6. Reusable Components

Common parsing logic should be reusable.

Reusable responsibilities include:

- section detection;
- entry splitting;
- date parsing;
- normalization;
- shared regex utilities.

Duplicate implementations should be avoided.

---

# 7. Parser Independence

Each parser must remain independent.

A parser must not:

- call another parser;
- modify another parser's output;
- depend on implementation details of another parser.

Parsers communicate only through the parser orchestrator.

---

# 8. Scalability

Parser architecture must support incremental extension.

New parsing capabilities should be added by introducing new parsing components instead of modifying existing ones whenever possible.

Architecture should follow the Open/Closed Principle.

---

# 9. File Organization

Simple parsers may remain in a single file.

When parsing complexity grows, responsibilities should be separated into dedicated parser components.

Example:

```
education/

    education_parser.py

    institution_parser.py

    degree_parser.py

    major_parser.py

    date_parser.py

    gpa_parser.py
```

The top-level parser remains responsible only for orchestration.

---

# 10. Naming Convention

Parser classes should use consistent naming.

Preferred examples:

- CandidateParser
- SkillParser
- EducationParser
- InstitutionParser
- DegreeParser
- DateParser

Avoid inconsistent naming such as:

- Detector
- Resolver
- Analyzer
- Manager

unless required by project-wide architecture.

---

# 11. Complexity Guidelines

A parser should remain small and readable.

If a parser begins to contain multiple independent extraction responsibilities, those responsibilities should be moved into dedicated parser components.

Large parser files should be decomposed before adding additional functionality.

---

# 12. Code Quality

Parser implementations should:

- be deterministic;
- avoid duplicated parsing logic;
- avoid duplicated regular expressions;
- keep methods focused on a single task;
- preserve backward compatibility whenever possible.

---

# 13. Testing

Every parser should be independently testable.

Each parser component should be testable in isolation.

Regression tests should verify that parser changes do not affect existing parsing behavior.

---

# 14. Anti-Patterns

Avoid the following:

- monolithic parser classes;
- duplicated parsing algorithms;
- duplicated section detection logic;
- duplicated regular expressions;
- deeply nested parsing logic;
- large methods with multiple responsibilities;
- cross-parser dependencies.

---

# 15. Engineering Principle

Parser architecture should prioritize:

- readability;
- maintainability;
- extensibility;
- composability;
- deterministic behavior;
- separation of responsibilities.

Parser quality is measured by architecture and maintainability, not by file count.
