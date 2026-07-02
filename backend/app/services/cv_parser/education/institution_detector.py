import re

from .patterns import INSTITUTION_KEYWORDS_PATTERN


class InstitutionDetector:
    @staticmethod
    def detect(lines: list[str]) -> str:
        for line in lines:
            if re.search(INSTITUTION_KEYWORDS_PATTERN, line, re.IGNORECASE):
                return line
        return ""
