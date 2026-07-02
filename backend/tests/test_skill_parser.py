from app.services.cv_parser.skill_parser import SkillParser


def test_skill_parser_extracts_declared_skills():
    raw_text = """Skills
- Python, Django, Flask
- ReactJS
"""

    expected = {
        "declared": ["Python", "Django", "Flask", "ReactJS"],
        "detected": [],
        "normalized": ["python", "django", "flask", "react"],
    }

    assert SkillParser.parse(raw_text) == expected


def test_skill_parser_detects_skills_from_other_sections():
    raw_text = """Summary
Experienced Python developer with AWS and Docker.

Experience
Built web services using Flask and ReactJS.
"""

    expected = {
        "declared": [],
        "detected": ["Python", "AWS", "Docker", "Flask", "ReactJS"],
        "normalized": ["python", "aws", "docker", "flask", "react"],
    }

    assert SkillParser.parse(raw_text) == expected


def test_skill_parser_does_not_detect_skills_from_skills_section():
    raw_text = """Skills
Python, JavaScript

Experience
Developed applications using React and Node.js.
"""

    expected = {
        "declared": ["Python", "JavaScript"],
        "detected": ["React", "Node.js"],
        "normalized": ["python", "javascript", "react", "nodejs"],
    }

    assert SkillParser.parse(raw_text) == expected


def test_skill_parser_normalizes_equivalent_skill_names():
    raw_text = """Skills:
ReactJS; TS; AWS

Projects
Built a React.js app with TypeScript on AWS.
"""

    expected = {
        "declared": ["ReactJS", "TS", "AWS"],
        "detected": [],
        "normalized": ["react", "typescript", "aws"],
    }

    assert SkillParser.parse(raw_text) == expected
