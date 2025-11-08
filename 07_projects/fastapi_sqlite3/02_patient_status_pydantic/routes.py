from fastapi import FastAPI, HTTPException
from database import add_patient_data, get_patients_data
from pydantic_code import Patient

app = FastAPI()


@app.get("/")
def root():
    return "Ready To Go...."


# post route to insert a patient in db
@app.post("/v1/patient")
def add_patient(patient: Patient):
    try:
        res = add_patient_data(patient)
        return {"message": "Patient added successfully", "date": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"myError: {e}")


# get route to get_all patient from db
@app.get("/v1/patient")
def get_patients():
    res = get_patients_data()

    return {"message": "All todo has been fetched", "result": res}
