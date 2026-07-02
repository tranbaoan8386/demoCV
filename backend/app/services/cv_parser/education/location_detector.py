import re

from .patterns import DEGREE_PATTERN, GPA_PATTERN, LOCATION_LABEL_PATTERN


class LocationDetector:
    @staticmethod
    def detect(lines: list[str]) -> str:
        for line in lines:
            if re.search(LOCATION_LABEL_PATTERN, line, re.IGNORECASE):
                return line

        for line in lines:
            if "," in line and not re.search(DEGREE_PATTERN, line, re.IGNORECASE) and not re.search(GPA_PATTERN, line, re.IGNORECASE):
                return line

        return ""
