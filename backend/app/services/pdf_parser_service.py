import fitz


class PDFParserService:

    @staticmethod
    def extract_text(file_content: bytes) -> str:
        pdf = fitz.open(
            stream=file_content,
            filetype="pdf"
        )

        text = ""

        for page in pdf:
            text += page.get_text()

        return text