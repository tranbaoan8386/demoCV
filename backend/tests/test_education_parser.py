from app.services.cv_parser.education import EducationParser
from app.services.cv_parser.education.entry_preprocessor import EntryPreprocessor
from app.services.cv_parser.education.line_labeler import LineLabeler


def test_entry_preprocessor_normalizes_and_preserves_order():
    entry_text = "University of Example | Bachelor of Science\n2016 - 2020"

    normalized = EntryPreprocessor.preprocess(entry_text)

    assert normalized[0]["text"] == "University of Example"
    assert normalized[1]["text"] == "Bachelor of Science"
    assert normalized[2]["text"] == "2016 - 2020"
    assert normalized[0]["order"] == 0


def test_line_labeler_assigns_expected_labels():
    normalized_lines = [
        {"text": "University of Example", "order": 0},
        {"text": "Bachelor of Science in Computer Science", "order": 1},
        {"text": "GPA: 3.8", "order": 2},
    ]

    labeled = LineLabeler.label(normalized_lines)

    assert labeled[0]["labels"] == ["institution"]
    assert labeled[1]["labels"] == ["degree", "major"]
    assert labeled[2]["labels"] == ["gpa"]


def test_education_parser_returns_empty_when_no_section():
    raw_text = "Name\nEmail\n"

    assert EducationParser.parse(raw_text) == []


def test_education_parser_extracts_single_entry_fields():
    raw_text = """Education\nUniversity of Example\nBachelor of Science in Computer Science\n2016 - 2020\nGPA: 3.8\nLocation: Example City\nHonors: Cum Laude\n"""

    expected = [
        {
            "institution": "University of Example",
            "degree": "Bachelor of Science in Computer Science",
            "major": "Computer Science",
            "start_date": "2016",
            "end_date": "2020",
            "gpa": "GPA: 3.8",
            "location": "Location: Example City",
            "description": "Honors: Cum Laude",
        }
    ]

    assert EducationParser.parse(raw_text) == expected


def test_education_parser_extracts_multiple_entries_in_order():
    raw_text = """Education\nUniversity A\nMaster of Engineering\n2018 - 2020\n\nCollege B\nBachelor of Science in Electrical Engineering\n2014 - 2018\n"""

    expected = [
        {
            "institution": "University A",
            "degree": "Master of Engineering",
            "major": "Engineering",
            "start_date": "2018",
            "end_date": "2020",
            "gpa": "",
            "location": "",
            "description": "",
        },
        {
            "institution": "College B",
            "degree": "Bachelor of Science in Electrical Engineering",
            "major": "Electrical Engineering",
            "start_date": "2014",
            "end_date": "2018",
            "gpa": "",
            "location": "",
            "description": "",
        },
    ]

    assert EducationParser.parse(raw_text) == expected


def test_education_parser_ignores_non_education_sections():
    raw_text = """Summary\nExperienced developer.\n\nEducation\nExample University\nBSc in Physics\n2012 - 2016\n\nExperience\nWorked at Example Corp.\n"""

    expected = [
        {
            "institution": "Example University",
            "degree": "BSc in Physics",
            "major": "Physics",
            "start_date": "2012",
            "end_date": "2016",
            "gpa": "",
            "location": "",
            "description": "",
        }
    ]

    assert EducationParser.parse(raw_text) == expected


def test_education_parser_preserves_backward_compatibility_in_cv_parser():
    raw_text = """Jane Doe\njane@example.com\n+84912345678\n"""

    from app.services.cv_parser.parser import CVParser
    from app.services.cv_parser_service import CVParserService

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
        "skills": {"declared": [], "detected": [], "normalized": []},
        "education": [],
        "projects": [],
        "experience": [],
        "certifications": [],
    }

    assert CVParser.parse(raw_text) == expected
    assert CVParserService.parse(raw_text) == expected
