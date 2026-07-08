import re

def clean_cv_text(raw_text: str) -> str:
    """Tiền xử lý văn bản CV trước khi phân tích."""
    if not raw_text:
        return ""

    # Đồng bộ hóa các ký tự xuống dòng
    text = raw_text.replace("\r\n", "\n").replace("\r", "\n")

    # TÌM VÀ CẮT BỎ RÁC (Sở thích, Tham chiếu...) từ điểm đó đến cuối file
    stop_pattern = re.compile(
        r"(?ims)(Sở thích cá nhân|Sở thích|Người tham chiếu|References|Hobbies|Interests)\b.*$"
    )
    text = stop_pattern.sub("", text)

    # Gom các dòng trắng thừa (3 dòng trở lên thành 2 dòng)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Gom khoảng trắng và tab lộn xộn
    text = re.sub(r"[ \t]+", " ", text)
    # Xóa khoảng trắng ở đầu/cuối mỗi dòng
    text = re.sub(r"[ \t]*\n[ \t]*", "\n", text)

    return text.strip()