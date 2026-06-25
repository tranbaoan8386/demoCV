import re

EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
PHONE_REGEX = r"(?:\+84|0)\d{9,10}"


def find_first_match(pattern: str, raw_text: str):
    return re.search(pattern, raw_text)
