from fastapi import FastAPI
from database import create_todo_items, get_todo_item, update_todo_Item

app = FastAPI()


# health check '/' route
@app.get("/")
def healthCheck():
    return {"message": "Our todo api is running...."}


# get_all_todos route
@app.get("/v1/todo")
def get_todo():
    res = get_todo_item()

    return res


# post todo item route
@app.post("/v1/todo/{task}")
def create_todo(task):
    todo_task = create_todo_items(task)

    return todo_task


# update todo item route
@app.put("/v1/todo")
def update_todo(task: str, todo_id: int):
    updated_task = update_todo_Item(task, todo_id)
    
    if updated_task:
        return {"message": "Task updated successfully"}
