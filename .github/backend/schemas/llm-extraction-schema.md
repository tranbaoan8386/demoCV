# Cấu trúc JSON bóc tách từ CV (LLM Extraction Schema)

Khi Agent viết code gọi LLM API (OpenAI/Gemini/Claude) để bóc tách thông tin từ `cleaned_text`, BẮT BUỘC phải yêu cầu LLM trả về định dạng JSON (Structured Output) tuân thủ CHÍNH XÁC Schema toàn diện sau đây.

## QUY TẮC XỬ LÝ DỮ LIỆU THIẾU:

Hệ thống phải xử lý được mọi loại CV. Nếu CV không chứa thông tin cho một trường cụ thể:

1. Đối với kiểu `string` hoặc `object`: Gán giá trị là `null`.
2. Đối với kiểu mảng (`array`): Gán giá trị là mảng rỗng `[]`.
3. TUYỆT ĐỐI KHÔNG tự bịa đặt, suy đoán hoặc điền nội dung giả (hallucination) vào các trường bị thiếu.

## SCHEMA:

```json
{
  "personal_info": {
    "full_name": "string | null (Họ và tên đầy đủ)",
    "job_title": "string | null (Vị trí ứng tuyển hoặc chức danh hiện tại)",
    "date_of_birth": "string | null (Ngày sinh)",
    "gender": "string | null (Giới tính)",
    "phone_number": "string | null (Số điện thoại)",
    "email": "string | null (Địa chỉ email)",
    "address": "string | null (Địa chỉ sinh sống)",
    "linkedin_url": "string | null (Link LinkedIn)",
    "github_url": "string | null (Link Github)",
    "portfolio_url": "string | null (Link Website cá nhân/Portfolio)"
  },
  "summary": "string | null (Đoạn tóm tắt mục tiêu nghề nghiệp hoặc giới thiệu bản thân)",
  "skills": {
    "technical_skills": [
      "string (Mảng chứa các kỹ năng chuyên môn/công nghệ, ví dụ: React, Python, AWS)"
    ],
    "soft_skills": [
      "string (Mảng chứa các kỹ năng mềm, ví dụ: Giao tiếp, Làm việc nhóm)"
    ],
    "languages": [
      {
        "language": "string | null (Tên ngôn ngữ, ví dụ: Tiếng Anh, Tiếng Nhật)",
        "proficiency": "string | null (Trình độ, ví dụ: IELTS 7.0, N3, Giao tiếp tốt)"
      }
    ]
  },
  "work_experience": [
    {
      "company_name": "string | null (Tên công ty)",
      "job_title": "string | null (Vị trí công tác)",
      "start_date": "string | null (Thời gian bắt đầu)",
      "end_date": "string | null (Thời gian kết thúc hoặc 'Hiện tại')",
      "description": "string | null (Mô tả công việc và thành tựu)",
      "technologies": ["string (Mảng các công nghệ đã sử dụng tại công ty này)"]
    }
  ],
  "education": [
    {
      "school_name": "string | null (Tên trường học/tổ chức)",
      "degree": "string | null (Loại bằng cấp, ví dụ: Cử nhân, Thạc sĩ)",
      "major": "string | null (Chuyên ngành học)",
      "start_date": "string | null (Thời gian bắt đầu)",
      "end_date": "string | null (Thời gian kết thúc)",
      "gpa": "string | null (Điểm trung bình hoặc xếp loại)"
    }
  ],
  "projects": [
    {
      "project_name": "string | null (Tên dự án)",
      "role": "string | null (Vai trò trong dự án)",
      "start_date": "string | null (Thời gian bắt đầu)",
      "end_date": "string | null (Thời gian kết thúc)",
      "description": "string | null (Mô tả chi tiết dự án)",
      "technologies": ["string (Các công nghệ sử dụng trong dự án)"],
      "project_url": "string | null (Link demo hoặc source code)"
    }
  ],
  "certifications": [
    {
      "name": "string | null (Tên chứng chỉ)",
      "issuer": "string | null (Tổ chức cấp)",
      "date": "string | null (Thời gian cấp)"
    }
  ],
  "awards": [
    {
      "name": "string | null (Tên giải thưởng/danh hiệu)",
      "issuer": "string | null (Tổ chức trao tặng)",
      "date": "string | null (Thời gian đạt được)"
    }
  ],
  "activities": [
    {
      "organization": "string | null (Tên tổ chức/câu lạc bộ)",
      "role": "string | null (Vai trò tham gia)",
      "start_date": "string | null (Thời gian bắt đầu)",
      "end_date": "string | null (Thời gian kết thúc)",
      "description": "string | null (Mô tả hoạt động)"
    }
  ]
}
```
