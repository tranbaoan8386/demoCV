import re
from .skill_dictionary import SKILL_NORMALIZATION


class SkillParser:
    SKILL_SECTIONS = [
        r"^skills?\s*:?\s*$",
        r"^technical skills\s*:?\s*$",
        r"^skill set\s*:?\s*$",
        r"^technical competencies\s*:?\s*$",
        r"^skillset\s*:?\s*$",
    ]

    SECTION_BREAKS = [
        r"^summary\s*:?\s*$",
        r"^experience\s*:?\s*$",
        r"^work experience\s*:?\s*$",
        r"^projects?\s*:?\s*$",
        r"^certifications?\s*:?\s*$",
        r"^education\s*:?\s*$",
        r"^languages?\s*:?\s*$",
        r"^certificates?\s*:?\s*$",
    ]

  
    @staticmethod
    def parse(raw_text: str) -> dict:
        declared = SkillParser._extract_declared_skills(raw_text)
        declared_normalized = [
            normalized
            for skill in declared
            if (normalized := SkillParser._normalize_skill(skill))
        ]
        declared_norm_set = set(declared_normalized)

        detected = SkillParser._extract_detected_skills(raw_text, declared_norm_set)
        normalized = SkillParser._build_normalized_skills(declared, detected)

        return {
            "declared": declared,
            "detected": detected,
            "normalized": normalized,
        }

    @staticmethod
    def _extract_declared_skills(raw_text: str) -> list[str]:
        lines = [line.strip() for line in raw_text.splitlines()]
        section_start = None
        for index, line in enumerate(lines):
            if SkillParser._is_section_header(line, SkillParser.SKILL_SECTIONS):
                section_start = index
                break
            if re.search(r"^skills?\s*:\s*(.+)$", line, re.IGNORECASE):
                return SkillParser._split_skill_line(re.search(r"^skills?\s*:\s*(.+)$", line, re.IGNORECASE).group(1))

        if section_start is None:
            return []

        declared = []
        section_lines = lines[section_start + 1 :]
        for line in section_lines:
            if not line.strip():
                break
            if SkillParser._is_section_header(line, SkillParser.SECTION_BREAKS):
                break
            declared.extend(SkillParser._split_skill_line(line))

        return SkillParser._dedupe_preserve_order(declared)

    @staticmethod
    def _extract_detected_skills(raw_text: str, declared_norm_set: set[str]) -> list[str]:
        without_skills = SkillParser._remove_skills_section(raw_text)
        normalized_seen = set(declared_norm_set)
        raw_matches = []

        for variant, canonical in sorted(SKILL_NORMALIZATION.items(), key=lambda item: -len(item[0])):
            pattern = re.compile(rf"\b{re.escape(variant)}\b", re.IGNORECASE)
            for match in pattern.finditer(without_skills):
                ignored = canonical in normalized_seen
                raw_matches.append((match.start(), match.end(), match.group(0).strip(), canonical, ignored))
                break

        raw_matches.sort(key=lambda item: (item[0], -(item[1] - item[0])))
        detected = []
        occupied = []

        for start, end, original, canonical, ignored in raw_matches:
            if any(start < o_end and end > o_start for o_start, o_end in occupied):
                continue
            occupied.append((start, end))
            if ignored:
                continue
            if canonical in normalized_seen:
                continue
            normalized_seen.add(canonical)
            detected.append(original)

        return detected

    @staticmethod
    def _build_normalized_skills(declared: list[str], detected: list[str]) -> list[str]:
        normalized = []
        seen = set()
        for skill in declared + detected:
            canonical = SkillParser._normalize_skill(skill)
            if not canonical or canonical in seen:
                continue
            seen.add(canonical)
            normalized.append(canonical)
        return normalized

    @staticmethod
    def _normalize_skill(skill: str) -> str:
        normalized = skill.strip().lower()
        return SKILL_NORMALIZATION.get(normalized, normalized)

    @staticmethod
    def _split_skill_line(line: str) -> list[str]:
        # 1. Replace non-breaking space
        line = line.replace("\u00A0", " ").replace("\xa0", " ")

        # 2. Remove bullet characters
        line = re.sub(r"^[•\-*\u2022\u2023\u25E6\s]+", "", line)

        # 3. Collapse multiple spaces
        line = re.sub(r"[ \t]+", " ", line).strip()

        # 4. Remove category label if present
        # Example:
        # Programming Languages : HTML5, CSS3
        # -> HTML5, CSS3
        if ":" in line:
            line = line.split(":", 1)[1].strip()

        # 5. Split skills
        parts = re.split(r"[\|;,]+", line)

        # 6. Clean each skill
        skills = []
        for part in parts:
            skill = part.strip()

            # Remove trailing punctuation
            skill = skill.rstrip(".,;:")

            if skill:
                skills.append(skill)

        return skills

    @staticmethod
    def _remove_skills_section(raw_text: str) -> str:
        lines = [line.rstrip() for line in raw_text.splitlines()]
        section_start = None
        for index, line in enumerate(lines):
            if SkillParser._is_section_header(line, SkillParser.SKILL_SECTIONS):
                section_start = index
                break
            if re.search(r"^skills?\s*:\s*", line, re.IGNORECASE):
                return "\n".join(lines[:index] + lines[index + 1 :])

        if section_start is None:
            return raw_text

        section_end = len(lines)
        for index, line in enumerate(lines[section_start + 1 :], start=section_start + 1):
            if not line.strip():
                section_end = index
                break
            if SkillParser._is_section_header(line, SkillParser.SECTION_BREAKS):
                section_end = index
                break

        return "\n".join(lines[:section_start] + lines[section_end:])

    @staticmethod
    def _is_section_header(line: str, patterns: list[str]) -> bool:
        if not line or line.startswith("-") or line.startswith("*"):
            return False
        normalized = line.strip().lower()
        return any(re.match(pattern, normalized, re.IGNORECASE) for pattern in patterns)

    @staticmethod
    def _dedupe_preserve_order(values: list[str]) -> list[str]:
        seen = set()
        result = []
        for value in values:
            normalized = value.lower()
            if normalized in seen:
                continue
            seen.add(normalized)
            result.append(value)
        return result
