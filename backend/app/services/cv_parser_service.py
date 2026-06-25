from app.services.cv_parser.parser import CVParser


class CVParserService:

    @staticmethod
    def parse(raw_text: str) -> dict:
        return CVParser.parse(raw_text)