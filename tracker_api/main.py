from fastapi import FastAPI, HTTPException
from datetime import date
from typing import Optional, Literal, List, Annotated
from pydantic import BaseModel, EmailStr, constr, validator

app = FastAPI()

# Root route
@app.get("/")
def home():
    return {"message": "✅ Task Tracker API is running"}

# Global storage
USERS: dict[int, dict] = {}
TASKS: dict[int, dict] = {}

# ID counters
user_id_counter = 1
task_id_counter = 1

# -------------------- Models --------------------

# Reusable due_date validator
class DueDateValidator(BaseModel):
    due_date: date

    @validator('due_date')
    def validate_due_date(cls, value):
        if value < date.today():
            raise ValueError("Due date cannot be in the past.")
        return value

class UserCreate(BaseModel):
    username: Annotated[str, constr(min_length=3, max_length=20)]
    email: EmailStr

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

class TaskCreate(DueDateValidator):
    title: str
    description: Optional[str] = None
    user_id: int

class Task(TaskCreate):
    id: int
    status: Literal['pending', 'in_progress', 'completed']

class TaskStatusUpdate(BaseModel):
    status: Literal['pending', 'in_progress', 'completed']

# -------------------- Endpoints --------------------

# Create a user
@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    global user_id_counter
    user_data = user.dict()
    user_data["id"] = user_id_counter
    USERS[user_id_counter] = user_data
    user_id_counter += 1
    return user_data

# Get a user
@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return USERS[user_id]

# Create a task
@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter
    if task.user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")

    task_data = task.dict()
    task_data["id"] = task_id_counter
    task_data["status"] = "pending"
    TASKS[task_id_counter] = task_data
    task_id_counter += 1
    return task_data

# Get a task
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    return TASKS[task_id]

# Update task status
@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, status_update: TaskStatusUpdate):
    if task_id not in TASKS:
        raise HTTPException(status_code=404, detail="Task not found")
    TASKS[task_id]["status"] = status_update.status
    return TASKS[task_id]

# List all tasks for a user
@app.get("/users/{user_id}/tasks", response_model=List[Task])
def get_user_tasks(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    user_tasks = [task for task in TASKS.values() if task["user_id"] == user_id]
    return user_tasks
