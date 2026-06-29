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

# General Rules

Information must be stored in the domain it belongs to.

Candidate information must not contain project information.

Project information must not contain candidate information.

If a value cannot be confidently classified, leave the field empty rather than making assumptions.