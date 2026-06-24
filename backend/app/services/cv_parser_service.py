import re


class CVParserService:

    @staticmethod
    def parse(raw_text: str) -> dict:

        lines = [
            line.strip()
            for line in raw_text.splitlines()
            if line.strip()
        ]

        name = lines[0] if lines else None

        email_match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            raw_text
        )

        phone_match = re.search(
            r"(?:\+84|0)\d{9,10}",
            raw_text
        )

        return {
            "candidate": {
                "name": name,
                "email": email_match.group(0)
                if email_match else None,
                "phone": phone_match.group(0)
                if phone_match else None
            },
            "skills": [],
            "education": [],
            "projects": [],
            "experience": [],
            "certifications": []
        }