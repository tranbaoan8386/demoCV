from app.services.cv_parser.candidate_parser import CandidateParser
from app.services.cv_parser.certificate_parser import CertificateParser
from app.services.cv_parser.education import EducationParser
from app.services.cv_parser.experience_parser import ExperienceParser
from app.services.cv_parser.language_parser import LanguageParser
from app.services.cv_parser.project_parser import ProjectParser
from app.services.cv_parser.skill_parser import SkillParser
from app.services.cv_parser.summary_parser import SummaryParser


class CVParser:
    @staticmethod
    def parse(raw_text: str) -> dict:
        candidate = CandidateParser.parse(raw_text)

        return {
            "candidate": candidate,
            "skills": SkillParser.parse(raw_text),
            "education": EducationParser.parse(raw_text),
            "projects": ProjectParser.parse(raw_text),
            "experience": ExperienceParser.parse(raw_text),
            "certifications": CertificateParser.parse(raw_text),
        }
