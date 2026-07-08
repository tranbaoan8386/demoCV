import pytest
from app.services.cv_parser.text_cleaner import clean_cv_text


def test_clean_cv_text_removes_extra_whitespace_and_stop_sections():
    raw_text = (
        "Nguyễn Văn A\n\n\n"
        "Kỹ năng: Python, SQL\n"
        "  \n"
        "Mô tả: Làm việc với dữ liệu.\n\n\n"
        "Sở thích cá nhân: Đá bóng\n"
        "Người tham chiếu: Anh A\n"
    )

    cleaned = clean_cv_text(raw_text)

    assert "Sở thích cá nhân" not in cleaned
    assert "Người tham chiếu" not in cleaned
    assert "Đá bóng" not in cleaned
    assert "Anh A" not in cleaned
    assert "  " not in cleaned
    assert "\n\n\n" not in cleaned
    assert cleaned.endswith("Mô tả: Làm việc với dữ liệu.")
    
def test_clean_cv_text_removes_english_stop_sections():
    raw_text = (
        "John Doe\n"
        "Frontend Developer\n"
        "Experience: 2 years of building UI.\n\n\n"
        "Hobbies: Reading, Coding\n"
        "References: Available upon request\n"
    )

    cleaned = clean_cv_text(raw_text)

    assert "Hobbies" not in cleaned
    assert "References" not in cleaned
    assert "Reading" not in cleaned
    assert "Available" not in cleaned
    assert cleaned.endswith("Experience: 2 years of building UI.")
