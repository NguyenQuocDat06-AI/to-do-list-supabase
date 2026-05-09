import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

if not URL or not KEY:
    print("Vui lòng thiết lập biến môi trường SUPABASE_URL và SUPABASE_SERVICE_ROLE_KEY trong file .env")
    

supabase: Client = create_client(URL, KEY)
print("Kết nối thành công với Supabase")