from fastapi import FastAPI, HTTPException
from database import add_patient_data
from pydantic_code import Patient

app = FastAPI()

@app.get('/')
def root():
    return "Ready To Go...."

@app.post("/v1/patient")
def add_patient(patient: Patient):
    try:
        res = add_patient_data(patient)
        return {"message": "Patient added successfully", "date": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail="error aa rha ahi")
