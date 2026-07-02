import re


class EntryPreprocessor:
    @staticmethod
    def preprocess(entry_text: str) -> list[dict]:
        normalized_lines = []

        for raw_line in entry_text.splitlines():
            cleaned = raw_line.strip()
            cleaned = re.sub(r"^[\-\*•\u2023\u25E6]\s*", "", cleaned)
            if not cleaned:
                continue

            parts = re.split(r"\s*[|•]\s*", cleaned)
            for part in parts:
                normalized = re.sub(r"\s+", " ", part).strip()
                if normalized:
                    normalized_lines.append({
                        "text": normalized,
                        "order": len(normalized_lines),
                    })

        return normalized_lines
