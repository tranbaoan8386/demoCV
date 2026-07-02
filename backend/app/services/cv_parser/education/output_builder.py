import re


class OutputBuilder:
    @staticmethod
    def build(entries: list[dict]) -> list[dict]:
        return entries

    @staticmethod
    def build_entry(labeled_lines: list[dict]) -> dict:
        record = {
            "institution": "",
            "degree": "",
            "major": "",
            "start_date": "",
            "end_date": "",
            "gpa": "",
            "location": "",
            "description": "",
        }

        degree_text = ""
        description_parts = []

        for labeled_line in sorted(labeled_lines, key=lambda item: item["order"]):
            text = labeled_line["text"]
            labels = set(labeled_line["labels"])

            if "institution" in labels and not record["institution"]:
                record["institution"] = text

            if "degree" in labels and not record["degree"]:
                record["degree"] = text
                degree_text = text

            if "gpa" in labels and not record["gpa"]:
                record["gpa"] = text

            if "location" in labels and not record["location"]:
                record["location"] = text

            if "date" in labels:
                date_match = re.search(
                    r"(?P<start>\d{4}|[A-Za-z]{3,}\s*\d{4})\s*(?:-|–|—|to)\s*(?P<end>\d{4}|[A-Za-z]{3,}\s*\d{4}|present|current|ongoing)",
                    text,
                    re.IGNORECASE,
                )
                if date_match and not record["start_date"]:
                    record["start_date"] = date_match.group("start").strip()
                    record["end_date"] = date_match.group("end").strip()

            if "description" in labels:
                description_parts.append(text)

        if not record["major"] and degree_text:
            record["major"] = OutputBuilder._infer_major(degree_text)

        if description_parts and not record["description"]:
            record["description"] = " ".join(description_parts)

        return record

    @staticmethod
    def _infer_major(degree_text: str) -> str:
        match = re.search(r"\bin\s+([A-Za-z][A-Za-z0-9&+\s\-]{2,})$", degree_text, re.IGNORECASE)
        if match:
            return match.group(1).strip()

        match = re.search(r"\b(?:Bachelor|Master|Associate|Diploma|Certificate|PhD|MBA|BA|BS|BSc|MSc|MS|MA)\b\s+of\s+([A-Za-z][A-Za-z0-9&+\s\-]{2,})", degree_text, re.IGNORECASE)
        if match:
            return match.group(1).strip()

        words = degree_text.split()
        if len(words) >= 2:
            return words[-1]

        return ""
