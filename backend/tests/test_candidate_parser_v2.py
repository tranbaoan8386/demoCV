from app.services.cv_parser.parser import CVParser
from app.services.cv_parser_service import CVParserService


def test_candidate_parser_extracts_additional_fields():
    raw_text = """John Smith
john.smith@example.com
+841234567890
123 Main St, District 1, HCMC
https://github.com/johnsmith
https://www.linkedin.com/in/johnsmith
http://portfolio.example.com/john
"""

    expected_candidate = {
        "name": "John Smith",
        "email": "john.smith@example.com",
        "phone": "+841234567890",
        "address": "123 Main St, District 1, HCMC",
        "github": "https://github.com/johnsmith",
        "linkedin": "https://www.linkedin.com/in/johnsmith",
        "portfolio": "http://portfolio.example.com/john",
    }

    result = CVParserService.parse(raw_text)
    assert result["candidate"] == expected_candidate
    assert CVParser.parse(raw_text)["candidate"] == expected_candidate


def test_candidate_parser_handles_missing_fields():
    raw_text = """Alice
alice@example.com
"""

    expected_candidate = {
        "name": "Alice",
        "email": "alice@example.com",
        "phone": "",
        "address": "",
        "github": "",
        "linkedin": "",
        "portfolio": "",
    }

    result = CVParserService.parse(raw_text)
    assert result["candidate"] == expected_candidate
    assert CVParser.parse(raw_text)["candidate"] == expected_candidate


def test_candidate_parser_ignores_non_portfolio_urls():
    raw_text = """John Smith
john.smith@example.com
https://github.com/johnsmith/project
https://example.com/demo
https://docs.example.com/guide
"""

    expected_candidate = {
        "name": "John Smith",
        "email": "john.smith@example.com",
        "phone": "",
        "address": "",
        "github": "",
        "linkedin": "",
        "portfolio": "",
    }

    result = CVParserService.parse(raw_text)
    assert result["candidate"] == expected_candidate
    assert CVParser.parse(raw_text)["candidate"] == expected_candidate


def test_candidate_parser_normalizes_address_lines():
    raw_text = """Jane Doe
jane@example.com
Address: 123 Main St, District 1, HCMC
"""

    expected_candidate = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "phone": "",
        "address": "123 Main St, District 1, HCMC",
        "github": "",
        "linkedin": "",
        "portfolio": "",
    }

    result = CVParserService.parse(raw_text)
    assert result["candidate"] == expected_candidate
    assert CVParser.parse(raw_text)["candidate"] == expected_candidate
