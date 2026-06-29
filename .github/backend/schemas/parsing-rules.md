# Parsing Rules

## Purpose

This document defines the semantic rules used when mapping extracted information into the structured output schema.

These rules are independent of the parsing implementation.

Every parser must follow these rules.

---

# Candidate Rules

## name

Represents the candidate's full legal or preferred name.

---

## email

Represents the primary contact email.

Only one email should be returned.

---

## phone

Represents the primary contact phone number.

---

## github

Must represent the candidate's personal GitHub profile.

Do not extract:

- Repository URLs
- Organization URLs

---

## linkedin

Must represent the candidate's personal LinkedIn profile.

Do not extract:

- Company pages
- Job posts

---

## portfolio

Must represent the candidate's personal portfolio website.

Examples:

- https://john.dev
- https://portfolio.john.dev
- https://john.vercel.app

Do not extract:

- Project live demos
- GitHub repositories
- Documentation sites
- Video links

---

# Project Rules

## live_demo

Represents the deployed application of the project.

Examples:

- https://capture-ck.vercel.app

---

## source_code

Represents the source repository of the project.

Examples:

- https://github.com/user/project

---

# Skills Rules

## declared

Represents the skills explicitly listed by the candidate in the Skills section.

Extract only skills that appear within the Skills section.

Preserve the order in which the candidate declares the skills.

Do not infer additional skills.

---

## detected

Represents skills detected from other sections of the CV.

Possible sources include:

- Summary
- Experience
- Projects
- Certifications

Do not extract skills from the Skills section into `detected`.

Only include skills that can be confidently identified.

---

## normalized

Represents the normalized skill set used for search, filtering, and matching.

The normalized list is derived from both `declared` and `detected`.

Normalization should:

- Merge `declared` and `detected`.
- Remove duplicate skills.
- Convert equivalent skill names to a single canonical search key.
- Use a consistent format suitable for indexing and matching.

Examples:

- ReactJS → react
- React.js → react
- React → react
- Node.js → nodejs
- TS → typescript
- JS → javascript

The normalized list is intended for internal processing rather than preserving the candidate's original wording.

---

# General Rules

Information must be stored in the domain it belongs to.

Candidate information must not contain project information.

Project information must not contain candidate information.

If a value cannot be confidently classified, leave the field empty rather than making assumptions.
