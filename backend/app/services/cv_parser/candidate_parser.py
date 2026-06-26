from app.services.cv_parser.regex_utils import EMAIL_REGEX, PHONE_REGEX, GITHUB_REGEX, LINKEDIN_REGEX, URL_REGEX, find_first_match
import re


class CandidateParser:
    @staticmethod
    def parse(raw_text: str) -> dict:
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]

        name = lines[0] if lines else ""

        email_match = find_first_match(EMAIL_REGEX, raw_text)
        phone_match = find_first_match(PHONE_REGEX, raw_text)
        github_match = find_first_match(GITHUB_REGEX, raw_text)
        linkedin_match = find_first_match(LINKEDIN_REGEX, raw_text)

        # portfolio: first URL that is not github or linkedin
        portfolio = ""
        url_match = find_first_match(URL_REGEX, raw_text)
        if url_match:
            url = url_match.group(0)
            if "github.com" not in url and "linkedin.com" not in url:
                portfolio = url

        # address heuristic: look for lines containing address keywords or street indicators with numbers
        address = ""
        address_keywords = ["address", "địa chỉ", "dia chi", "addr", "địa-chỉ"]
        street_indicators = ["street", "st", "road", "rd", "lane", "ln", "boulevard", "blvd", "avenue", "ave", "đường", "phố"]
        for line in lines:
            low = line.lower()
            if any(k in low for k in address_keywords):
                address = line
                break
            if any(ind in low for ind in street_indicators) and any(char.isdigit() for char in line):
                address = line
                break

        return {
            "name": name or "",
            "email": email_match.group(0) if email_match else "",
            "phone": phone_match.group(0) if phone_match else "",
            "address": address,
            "github": github_match.group(0) if github_match else "",
            "linkedin": linkedin_match.group(0) if linkedin_match else "",
            "portfolio": portfolio,
        }
