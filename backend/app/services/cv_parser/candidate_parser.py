from app.services.cv_parser.regex_utils import EMAIL_REGEX, PHONE_REGEX, find_first_match


class CandidateParser:
    @staticmethod
    def parse(raw_text: str) -> dict:
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]

        name = lines[0] if lines else None

        email_match = find_first_match(EMAIL_REGEX, raw_text)
        phone_match = find_first_match(PHONE_REGEX, raw_text)

        return {
            "name": name,
            "email": email_match.group(0) if email_match else None,
            "phone": phone_match.group(0) if phone_match else None,
        }
