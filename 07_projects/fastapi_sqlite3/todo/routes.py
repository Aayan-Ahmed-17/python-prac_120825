from fastapi import FastAPI

app = FastAPI()

#get_all_todos route
@app.get("/")
def healthCheck():
    return {
        "message": "Our todo api is running...."
    }