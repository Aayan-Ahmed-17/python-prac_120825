from fastapi import FastAPI

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


#post todo item route
@app.post("/v1/todo")
def create_todo():
    todo_task = create_todo_item()

    return todo_task