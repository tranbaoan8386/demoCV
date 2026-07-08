# TASK: Xây dựng Pre-processor (Dọn rác văn bản CV)

## 1. Mục tiêu

- Tạo một module dùng Python (Regex) để tiền xử lý `raw_text` sau khi đọc từ file PDF.
- Mục đích: Xóa bỏ các ký tự thừa (\n, \t) và cắt bỏ các phần rác không có giá trị phân tích (Sở thích, Người tham chiếu...).
- CHƯA tích hợp LLM. Chỉ trả về chuỗi văn bản đã được làm sạch để kiểm tra.

## 2. Các bước thực hiện

### Step 2.1: Tạo file `text_cleaner.py`

Tạo file mới tại đường dẫn: `backend/app/services/cv_parser/text_cleaner.py`.
Viết một hàm `clean_cv_text(raw_text: str) -> str` thực hiện các logic sau:

1. Chuyển đổi các khoảng trắng, tab lặp lại thành 1 khoảng trắng duy nhất.
2. Chuyển đổi nhiều dấu xuống dòng (\n\n\n) thành tối đa 1 hoặc 2 dấu xuống dòng.
3. Dùng Regex để tìm các từ khóa báo hiệu kết thúc CV (Ví dụ: "Sở thích cá nhân", "Sở thích", "Người tham chiếu", "References", "Hobbies"). Nếu gặp các từ này, hãy mạnh tay CẮT BỎ toàn bộ nội dung từ đó đến cuối file.
4. Trả về `cleaned_text` đã được `.strip()`.

### Step 2.2: Cập nhật `cv_parser_service.py` để test luồng

Trong file `backend/app/services/cv_parser_service.py`:

1. Import hàm `clean_cv_text` vừa tạo.
2. Tạm thời chỉnh sửa luồng xử lý: Sau khi lấy được `raw_text` từ PDF, hãy truyền nó qua `clean_cv_text()`.
3. (Tạm thời) Trả về kết quả JSON có chứa trường `"cleaned_text"` để frontend (hoặc API response) có thể xem trực tiếp kết quả text đã dọn dẹp.
