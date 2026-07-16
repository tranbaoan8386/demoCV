from typing import Any, Dict, List


def _safe_get(d: Dict[str, Any], key: str, default=None):
    return d.get(key, default) if isinstance(d, dict) else default


def _normalize_text(parts: List[str]) -> str:
    # join non-empty parts with two newlines and normalize whitespace
    cleaned = []
    for p in parts:
        if p is None:
            continue
        s = str(p).strip()
        if not s:
            continue
        # collapse multiple whitespace
        s = " ".join(s.split())
        cleaned.append(s)
    return "\n\n".join(cleaned)


def flatten_cv_data(structured_data: dict) -> str:
    """
    Flatten structured CV JSON into a plaintext string following semantic
    hierarchy: Title -> Summary -> Skills -> Work Experience -> Projects.

    Handles missing/empty fields gracefully and strips obvious metadata.
    """
    if not isinstance(structured_data, dict):
        return ""

    parts: List[str] = []

    # Title: prefer full_name and job_title
    personal = _safe_get(structured_data, "personal_info", {}) or {}
    full_name = _safe_get(personal, "full_name")
    job_title = _safe_get(personal, "job_title")
    title_parts = []
    if full_name:
        title_parts.append(full_name)
    if job_title:
        title_parts.append(job_title)
    if title_parts:
        parts.append(" - ".join(title_parts))

    # Summary
    summary = _safe_get(structured_data, "summary")
    if summary:
        parts.append(summary)

    # Skills
    skills = _safe_get(structured_data, "skills", {}) or {}
    skill_lines: List[str] = []
    technical = _safe_get(skills, "technical_skills", []) or []
    soft = _safe_get(skills, "soft_skills", []) or []
    languages = _safe_get(skills, "languages", []) or []
    if technical:
        skill_lines.append("Technical Skills: " + ", ".join(map(str, technical)))
    if soft:
        skill_lines.append("Soft Skills: " + ", ".join(map(str, soft)))
    if languages:
        lang_parts = []
        for l in languages:
            if not isinstance(l, dict):
                continue
            name = l.get("language")
            prof = l.get("proficiency")
            if name and prof:
                lang_parts.append(f"{name} ({prof})")
            elif name:
                lang_parts.append(name)
        if lang_parts:
            skill_lines.append("Languages: " + ", ".join(lang_parts))
    if skill_lines:
        parts.append("; ".join(skill_lines))

    # Work Experience
    work_items = _safe_get(structured_data, "work_experience", []) or []
    work_lines: List[str] = []
    for w in work_items:
        if not isinstance(w, dict):
            continue
        company = w.get("company_name")
        title = w.get("job_title")
        start = w.get("start_date")
        end = w.get("end_date")
        desc = w.get("description")
        techs = w.get("technologies", []) or []

        header_parts = []
        if title:
            header_parts.append(title)
        if company:
            header_parts.append(f"at {company}")
        if start or end:
            header_parts.append(f"({start or '?'} - {end or 'Present'})")

        item_lines: List[str] = []
        if header_parts:
            item_lines.append(" ".join(header_parts))
        if desc:
            item_lines.append(desc)
        if techs:
            item_lines.append("Technologies: " + ", ".join(map(str, techs)))

        if item_lines:
            work_lines.append(" - ".join(item_lines))
    if work_lines:
        parts.append("Work Experience:\n" + "\n\n".join(work_lines))

    # Projects
    projects = _safe_get(structured_data, "projects", []) or []
    proj_lines: List[str] = []
    for p in projects:
        if not isinstance(p, dict):
            continue
        name = p.get("project_name") or p.get("name")
        role = p.get("role")
        desc = p.get("description")
        techs = p.get("technologies", []) or []

        item = []
        if name:
            item.append(name)
        if role:
            item.append(f"Role: {role}")
        if desc:
            item.append(desc)
        if techs:
            item.append("Technologies: " + ", ".join(map(str, techs)))

        if item:
            proj_lines.append(" - ".join(item))
    if proj_lines:
        parts.append("Projects:\n" + "\n\n".join(proj_lines))

    # Final assembly
    text = _normalize_text(parts)

    return text
