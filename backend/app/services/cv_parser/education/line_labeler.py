from .date_detector import DateDetector
from .degree_detector import DegreeDetector
from .gpa_detector import GPADetector
from .institution_detector import InstitutionDetector
from .location_detector import LocationDetector
from .major_detector import MajorDetector


class LineLabeler:
    @staticmethod
    def label(normalized_lines: list[dict]) -> list[dict]:
        labeled_lines = []

        for normalized_line in normalized_lines:
            labels = []
            text = normalized_line["text"]

            if not text:
                continue

            if GPADetector.detect([text]):
                labels.append("gpa")

            if InstitutionDetector.detect([text]):
                labels.append("institution")

            if DegreeDetector.detect([text]):
                labels.append("degree")

            if MajorDetector.detect([text]):
                labels.append("major")

            if LocationDetector.detect([text]):
                labels.append("location")

            if DateDetector.detect([text])[0] or DateDetector.detect([text])[1]:
                labels.append("date")

            if not labels:
                labels.append("description")

            labeled_lines.append({
                "text": text,
                "order": normalized_line["order"],
                "labels": labels,
            })

        return labeled_lines
