from fastapi import FastAPI, HTTPException
from database import add_patient_data, get_patients_data, get_single_patient_data, update_patient_data, delete_patient_data
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


# get patient by id
@app.get("/v1/patient/{patient_id}")
def get_single_patient(patient_id: int):
    res = get_single_patient_data(patient_id)
    if not res:
        raise HTTPException(status_code=400, detail="Id not found, please find valid id")

    return {"message": "Patient data found", "Patient": res}

@app.put("/v1/patient/{patient_id}")
def update_patient(patient_id, patient: Patient):
    res = update_patient_data(patient_id, patient)

    return res

@app.delete("/v1/patient/{patient_id}")
def delete_patient(patient_id : int):
    res = delete_patient_data(patient_id)
    return res