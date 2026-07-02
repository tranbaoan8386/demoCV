from app.services.cv_parser.parser import CVParser
from app.services.cv_parser_service import CVParserService


def test_cv_parser_preserves_existing_output():
    raw_text = "Jane Doe\njane@example.com\n+84912345678"

    expected = {
        "candidate": {
            "name": "Jane Doe",
            "email": "jane@example.com",
            "phone": "+84912345678",
            "address": "",
            "github": "",
            "linkedin": "",
            "portfolio": "",
        },
        "skills": {
            "declared": [],
            "detected": [],
            "normalized": [],
        },
        "education": [],
        "projects": [],
        "experience": [],
        "certifications": [],
    }

    assert CVParserService.parse(raw_text) == expected
    assert CVParser.parse(raw_text) == expected
