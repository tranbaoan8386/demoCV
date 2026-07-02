import re

from .patterns import GPA_PATTERN


class GPADetector:
    @staticmethod
    def detect(lines: list[str]) -> str:
        for line in lines:
            match = re.search(GPA_PATTERN, line, re.IGNORECASE)
            if match:
                return match.group(0).strip()
        return ""
