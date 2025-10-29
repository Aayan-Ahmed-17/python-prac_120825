from fastapi import FastAPI

app = FastAPI()

"""ex01: Hello API: Create a FastAPI app with a single GET endpoint / that returns {"message": "Hello FastAPI"}"""


@app.get("/")
def root():
    return {"message": "Hello World"}


"""ex02: Greet User: Create an endpoint /greet/{name} that returns a personalized greeting with the name from the path parameter
"""


@app.get("/v1/greet/{name}")
def greetUser(name):
    return {"greet": f"Hello {name}"}


"""ex03: Calculator Basic: Build endpoints for basic math operations:
/add?a=5&b=3 → returns sum
/subtract?a=10&b=4 → returns difference
"""


@app.get("/v1/add/{num1}/{num2}")
def sum_two_num(num1: int, num2: int):
    return {"sum_result": f"the sum of {num1} & {num2} is {num1 + num2}"}


"""=====================smit class work================================"""


@app.get("/v1/items")
def all_items():
    return [
        {"message": "All items has been fetched"},
        {"id": 1, "item": "mobile"},
        {"id": 2, "item": "laptop"},
    ]


@app.get("v1/items/{item_id}")
def get_single_item(item_id: int):
    return [
        {"message": "Your single item is here"},
        {"id": item_id, "item": f"Item {item_id}"},
    ]
