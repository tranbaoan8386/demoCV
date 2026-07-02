# Structured Output Schema

## Overview

This document defines the canonical structured output of the CV parsing system.

The schema represents the normalized data model shared across all backend services, frontend applications, and AI components.

Parser implementations may change over time, but the structured output schema should remain stable unless explicitly approved.

---

# Root Object

The structured output consists of the following sections:

- candidate
- summary
- skills
- education
- experience
- projects
- certifications
- languages
- metadata

Each section represents an independent domain object.

---

# Candidate

## Description

Represents information belonging to the candidate.

## Fields

- name
- email
- phone
- address
- github
- linkedin
- portfolio

---

# Summary

Represents the candidate's professional summary.

---

# Skills

Represents the candidate's skills.

Structure:

- declared
- detected
- normalized

---

# Education

## Description

Represents the candidate's educational history.

## Structure

Education is represented as an array of education entries.

Each education entry contains:

```json
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
```

## Fields

- institution
- degree
- major
- start_date
- end_date
- gpa
- location
- description

---

# Experience

Represents work experience.

---

# Projects

Represents software or personal projects.

---

# Certifications

Represents certifications.

---

# Languages

Represents spoken languages.

---

# Metadata

Represents parser metadata.

Typical fields:

- parser_version
- parser_type
