# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from datetime import date, time, datetime
from uuid import UUID
from pydantic import BaseModel
from db import supabase

app =  FastAPI(title = "Supabase task API")

class TaskCreate(BaseModel):
    title: str
    is_completed: bool
    day_create: date | None = None
    time_create: time | None = None

@app.get("/task")
async def get_tasks():
    try:
        response = supabase.table("todos").select("*").order("id", desc = True).execute()
        return {"success": True, "data": response.data}
    except Exception as e:
        return {"error": str(e)}

@app.post("/task")
async def create_task(task: TaskCreate):
    try:
        response = supabase.table("todos").insert({
            "title": task.title,
            "is_completed": task.is_completed,
            "day_create": str(date.today()),
            "time_create": datetime.now().strftime("%H:%M:%S")
        }).execute()
        return {"success": True, "data": response.data}
    except Exception as e:
        return {"error": str(e)}

class TaskUpdate(BaseModel):
    title: str | None = None
    is_completed: bool | None = None

@app.put("/task/{task_id}")
async def update_task(task_id: UUID, task: TaskUpdate):
    try:
        # Loc bo cac truong None de chi cap nhat nhung gi duoc gui len
        update_data = {k: v for k, v in task.model_dump().items() if v is not None}
        if not update_data:
            return {"success": False, "message": "Không có dữ liệu để cập nhật"}
            
        response = supabase.table("todos").update(update_data).eq("id", task_id).execute()
        return {"success": True, "data": response.data}
    except Exception as e:
        return {"error": str(e)}

@app.delete("/task/{task_id}")
async def delete_task(task_id: UUID):
    try:
        response = supabase.table("todos").delete().eq("id", task_id).execute()
        return {"success": True, "message": f"Đã xóa task {task_id}"}
    except Exception as e:
        return {"error": str(e)}
