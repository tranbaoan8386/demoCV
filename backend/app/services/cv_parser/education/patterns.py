import re

EDUCATION_SECTION_HEADERS = [
    r"^education\s*:??\s*$",
    r"^education\s+and\s+training\s*:??\s*$",
    r"^academic\s+background\s*:??\s*$",
    r"^academic\s+qualifications\s*:??\s*$",
    r"^education\s+history\s*:??\s*$",
]

SECTION_BREAK_PATTERNS = [
    r"^summary\s*:??\s*$",
    r"^experience\s*:??\s*$",
    r"^work\s+experience\s*:??\s*$",
    r"^projects?\s*:??\s*$",
    r"^certifications?\s*:??\s*$",
    r"^languages?\s*:??\s*$",
    r"^skills?\s*:??\s*$",
    r"^certificates?\s*:??\s*$",
]

DEGREE_PATTERN = r"\b(?:bachelor|master|associate|diploma|certificate|phd|mba|ba|bs|bsc|msc|ms|ma|doctor|engineer)\b"
DEGREE_OF_PATTERN = r"\b(?:Bachelor|Master|Associate|Diploma|Certificate|PhD|MBA|BA|BS|BSc|MSc|MS|MA)\b\s+of\s+([A-Za-z][A-Za-z0-9&+\s\-]{2,})"
MAJOR_LABEL_PATTERN = r"\b(?:major|special(?:i[sz]ation)?|field of study|specialized in|specialisation in|specializing in|specialising in)\b"
DATE_RANGE_PATTERN = r"(?P<start>(?:\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\b\s*)?\d{4})\s*(?:[-–—]|to)\s*(?P<end>(?:present|current|ongoing|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\b\s*)?\d{4})"
DATE_PATTERN = r"(?:\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\b\s*\d{4}|\d{4})"
GPA_PATTERN = r"\bGPA\s*[:\-]?\s*\d+(?:\.\d+)?(?:\s*(?:/|out of)\s*\d+(?:\.\d+)?)?\b"
LOCATION_LABEL_PATTERN = r"\b(?:location|campus|city|state|country|province|district|region)\b"
INSTITUTION_KEYWORDS_PATTERN = r"\b(?:university|institute|college|school|academy|faculty)\b"
DATE_CONTEXT_PATTERN = r"\bfrom\b|\bto\b|[-–—]"
