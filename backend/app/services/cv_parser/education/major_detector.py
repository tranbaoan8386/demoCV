import re

from .patterns import DEGREE_PATTERN, MAJOR_LABEL_PATTERN


class MajorDetector:
    @staticmethod
    def detect(lines: list[str]) -> str:
        for line in lines:
            match = re.search(rf"{MAJOR_LABEL_PATTERN}\s*[:\-]?\s*(.+)", line, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        for line in lines:
            match = re.search(r"\b(?:Bachelor|Master|Associate|Diploma|Certificate|PhD|MBA|BA|BS|BSc|MSc|MS|MA)\b\s+(?:of\s+[A-Za-z&+\s\-]+\s+)?in\s+(.+)", line, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        for line in lines:
            match = re.search(r"\b(?:Bachelor|Master|Associate|Diploma|Certificate|PhD|MBA|BA|BS|BSc|MSc|MS|MA)\b\s+of\s+([A-Za-z][A-Za-z0-9&+\s\-]{2,})", line, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        for line in lines:
            match = re.search(r"\bin\s+([A-Za-z][A-Za-z0-9&+\s\-]{2,})", line, re.IGNORECASE)
            if match:
                return match.group(1).strip()

        return ""
