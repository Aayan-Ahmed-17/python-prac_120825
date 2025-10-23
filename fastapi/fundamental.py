from fastapi import FastAPI

app = FastAPI()

"""ex01: Hello API: Create a FastAPI app with a single GET endpoint / that returns {"message": "Hello FastAPI"}"""


@app.get("/")
def root():
    return {"message": "Hello World"}


"""ex02: Greet User: Create an endpoint /greet/{name} that returns a personalized greeting with the name from the path parameter
"""
@app.get('/greet/{name}')
def greetUser(name):
    return {"greet": f"Hello {name}"}