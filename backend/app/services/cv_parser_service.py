from app.services.cv_parser.text_cleaner import clean_cv_text

class CVParserService:
    @staticmethod
    def parse(raw_text: str) -> dict:
        """Tạm thời trả về text đã dọn dẹp để kiểm tra luồng upload."""
        cleaned_text = clean_cv_text(raw_text)
        # Trả về một dict đơn giản để Frontend dễ dàng đọc được
        return {"cleaned_text": cleaned_text}

    @staticmethod
    def process_cv(raw_text: str) -> dict:
        return CVParserService.parse(raw_text)