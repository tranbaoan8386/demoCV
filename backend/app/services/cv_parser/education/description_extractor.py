import re

from .patterns import DATE_PATTERN, DATE_RANGE_PATTERN, DEGREE_PATTERN, GPA_PATTERN, LOCATION_LABEL_PATTERN, MAJOR_LABEL_PATTERN, INSTITUTION_KEYWORDS_PATTERN


class DescriptionExtractor:
    @staticmethod
    def extract(lines: list[str]) -> str:
        description_lines = []

        for line in lines:
            if re.search(INSTITUTION_KEYWORDS_PATTERN, line, re.IGNORECASE):
                continue
            if re.search(DEGREE_PATTERN, line, re.IGNORECASE):
                continue
            if re.search(MAJOR_LABEL_PATTERN, line, re.IGNORECASE):
                continue
            if re.search(DATE_RANGE_PATTERN, line, re.IGNORECASE):
                continue
            if re.search(GPA_PATTERN, line, re.IGNORECASE):
                continue
            if re.search(LOCATION_LABEL_PATTERN, line, re.IGNORECASE):
                continue
            if re.search(DATE_PATTERN, line, re.IGNORECASE) and re.search(r"\bfrom\b|\bto\b|[-–—]", line, re.IGNORECASE):
                continue
            description_lines.append(line)

        return " ".join(description_lines).strip()
