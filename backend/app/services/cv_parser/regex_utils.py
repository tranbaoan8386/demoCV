import re

EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
PHONE_REGEX = r"(?:\+84|0)\d{9,10}"

# URL patterns
GITHUB_REGEX = r"(?:https?://)?(?:www\.)?github\.com/[A-Za-z0-9\-._/]+"
LINKEDIN_REGEX = r"(?:https?://)?(?:www\.)?linkedin\.com/(?:in|pub)/[A-Za-z0-9\-._/]+"
URL_REGEX = r"(?:https?://)?(?:www\.)?[A-Za-z0-9\-._]+\.[A-Za-z]{2,}(?:/[^\s]*)?"


def find_first_match(pattern: str, raw_text: str):
    return re.search(pattern, raw_text)
