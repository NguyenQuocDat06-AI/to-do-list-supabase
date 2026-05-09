# To-Do List API with FastAPI & Supabase

Một ứng dụng To-Do List đơn giản sử dụng FastAPI cho Backend và Supabase để lưu trữ dữ liệu.

## Cấu trúc dự án

```text
├── .env           # Lưu trữ các biến môi trường (API Keys)
├── db.py          # Kết nối và cấu hình Supabase
├── main.py        # Các API routes (FastAPI)
├── requirements.txt # Danh sách thư viện
└── venv/          # Môi trường ảo Python
```

## Hướng dẫn cài đặt

1. Tạo môi trường ảo: `python -m venv venv`
2. Kích hoạt: `source venv/bin/activate`
3. Cài đặt thư viện: `pip install -r requirements.txt`
4. Cấu hình `.env` với các thông tin từ Supabase Dashboard.
5. Chạy server: `uvicorn main:app --reload`