import re

from .patterns import EDUCATION_SECTION_HEADERS, SECTION_BREAK_PATTERNS


class EducationSectionLocator:
    @staticmethod
    def locate(raw_text: str) -> str:
        lines = [line.rstrip() for line in raw_text.splitlines()]
        section_start = None

        for index, line in enumerate(lines):
            normalized = line.strip().lower()
            if any(re.match(pattern, normalized, re.IGNORECASE) for pattern in EDUCATION_SECTION_HEADERS):
                section_start = index + 1
                break

        if section_start is None:
            return ""

        section_end = len(lines)
        for index in range(section_start, len(lines)):
            normalized = lines[index].strip().lower()
            if any(re.match(pattern, normalized, re.IGNORECASE) for pattern in SECTION_BREAK_PATTERNS):
                section_end = index
                break

        return "\n".join(lines[section_start:section_end]).strip()
