import re

from .patterns import DATE_PATTERN, DATE_RANGE_PATTERN, DATE_CONTEXT_PATTERN


class DateDetector:
    @staticmethod
    def detect(lines: list[str]) -> tuple[str, str]:
        for line in lines:
            range_match = re.search(DATE_RANGE_PATTERN, line, re.IGNORECASE)
            if range_match:
                return range_match.group("start").strip(), range_match.group("end").strip()

        for line in lines:
            if re.search(r"\bfrom\b", line, re.IGNORECASE):
                date_match = re.search(DATE_PATTERN, line, re.IGNORECASE)
                if date_match:
                    return date_match.group(0).strip(), ""

        for line in lines:
            if re.search(DATE_CONTEXT_PATTERN, line, re.IGNORECASE):
                date_match = re.search(DATE_PATTERN, line, re.IGNORECASE)
                if date_match:
                    return "", date_match.group(0).strip()

        return "", ""
