from fastapi import FastAPI
from database import add_patient_data
from pydantic_code import Patient

app = FastAPI()

@app.get('/')
def root():
    return "Ready To Go...."

@app.post("/v1/patient/{infos}")
def add_patient(infos: Patient):
    res = add_patient_data(infos)
    return res
