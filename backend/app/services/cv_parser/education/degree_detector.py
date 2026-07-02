import re

from .patterns import DEGREE_PATTERN


class DegreeDetector:
    @staticmethod
    def detect(lines: list[str]) -> str:
        for line in lines:
            if re.search(DEGREE_PATTERN, line, re.IGNORECASE):
                return line
        return ""
