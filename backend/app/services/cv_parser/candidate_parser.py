from urllib.parse import urlparse

from app.services.cv_parser.regex_utils import EMAIL_REGEX, PHONE_REGEX, GITHUB_REGEX, LINKEDIN_REGEX, URL_REGEX, find_first_match
import re


class CandidateParser:
    @staticmethod
    def parse(raw_text: str) -> dict:
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]

        name = lines[0] if lines else ""

        email_match = find_first_match(EMAIL_REGEX, raw_text)
        phone_match = find_first_match(PHONE_REGEX, raw_text)
        github_url = CandidateParser._extract_github(raw_text)
        linkedin_url = CandidateParser._extract_linkedin(raw_text)
        portfolio = CandidateParser._extract_portfolio(raw_text, github_url, linkedin_url)
        address = CandidateParser._extract_address(lines)

        return {
            "name": name or "",
            "email": email_match.group(0) if email_match else "",
            "phone": phone_match.group(0) if phone_match else "",
            "address": address,
            "github": github_url,
            "linkedin": linkedin_url,
            "portfolio": portfolio,
        }

    @staticmethod
    def _extract_github(raw_text: str) -> str:
        github_match = find_first_match(GITHUB_REGEX, raw_text)
        if not github_match:
            return ""
        candidate_url = github_match.group(0).strip()
        parsed = urlparse(candidate_url if "://" in candidate_url else f"https://{candidate_url}")
        if (parsed.netloc or "").lower().replace("www.", "") != "github.com":
            return ""
        path_segments = [segment for segment in parsed.path.split("/") if segment]
        if len(path_segments) != 1:
            return ""
        return candidate_url

    @staticmethod
    def _extract_linkedin(raw_text: str) -> str:
        linkedin_match = find_first_match(LINKEDIN_REGEX, raw_text)
        if not linkedin_match:
            return ""
        candidate_url = linkedin_match.group(0).strip()
        parsed = urlparse(candidate_url if "://" in candidate_url else f"https://{candidate_url}")
        if (parsed.netloc or "").lower().replace("www.", "") != "linkedin.com":
            return ""
        path_segments = [segment for segment in parsed.path.split("/") if segment]
        if len(path_segments) != 2 or path_segments[0] not in {"in", "pub"}:
            return ""
        return candidate_url

    @staticmethod
    def _extract_portfolio(raw_text: str, github_url: str = "", linkedin_url: str = "") -> str:
        for match in re.finditer(URL_REGEX, raw_text):
            url = match.group(0).strip()
            if CandidateParser._is_portfolio_url(url, github_url, linkedin_url):
                return url
        return ""

    @staticmethod
    def _is_portfolio_url(url: str, github_url: str = "", linkedin_url: str = "") -> bool:
        normalized_url = url.lower()
        if not normalized_url:
            return False
        if github_url and normalized_url == github_url.lower():
            return False
        if linkedin_url and normalized_url == linkedin_url.lower():
            return False
        if any(host in normalized_url for host in ("github.com", "gitlab.com", "bitbucket.org", "linkedin.com")):
            return False

        parsed = urlparse(url)
        host = (parsed.netloc or "").lower()
        path = (parsed.path or "").lower()

        if host.startswith("www."):
            host = host[4:]
        if host.startswith("docs.") or host.split(".")[0] == "docs":
            return False

        non_portfolio_paths = [
            "/demo",
            "/demos",
            "/project",
            "/projects",
            "/docs",
            "/documentation",
            "/guide",
            "/guides",
            "/video",
            "/videos",
            "/blog",
            "/post",
            "/posts",
            "/article",
            "/articles",
            "/download",
            "/downloads",
            "/source",
            "/repo",
            "/repository",
        ]
        if any(path.startswith(token) for token in non_portfolio_paths):
            return False

        if host.endswith(".dev") or host.endswith(".app") or host.endswith(".io") or host.endswith(".me") or host.endswith(".com") or host.endswith(".net"):
            if "portfolio" in host or "portfolio" in path:
                return True
        return False

    @staticmethod
    def _extract_address(lines: list[str]) -> str:
        address_keywords = ["address", "địa chỉ", "dia chi", "addr", "địa-chỉ"]
        street_indicators = ["street", "st", "road", "rd", "lane", "ln", "boulevard", "blvd", "avenue", "ave", "đường", "phố"]
        for line in lines:
            low = line.lower()
            if any(k in low for k in address_keywords):
                cleaned = CandidateParser._clean_address_line(line)
                if cleaned:
                    return cleaned
            if any(ind in low for ind in street_indicators) and any(char.isdigit() for char in line):
                cleaned = CandidateParser._clean_address_line(line)
                if cleaned:
                    return cleaned
        return ""

    @staticmethod
    def _clean_address_line(line: str) -> str:
        cleaned = re.sub(r"^(?:address|addr|current address|permanent address|địa chỉ|dia chi|địa-chỉ)\s*[:\-]?\s*", "", line, flags=re.IGNORECASE).strip()
        return re.sub(r"^[\-:;\s]+", "", cleaned).strip()
