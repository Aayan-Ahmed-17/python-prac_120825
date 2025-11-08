from pydantic import BaseModel, Field
from typing import Annotated


class Patient(BaseModel):
    id: Annotated[int, Field(..., description="ID  of the patient", examples="For Example P001")]
    name: Annotated[str, Field(..., description="Name of the patient", examples="John Doe")]
    city: Annotated[str, Field(..., description="City where patient lives in..", examples="Karachi")]
    age: Annotated[int, Field(..., description="Provide the age of patient in numbers")]
    gender: Annotated[str, Field(..., description="Gender of the patient", examples="Male or Female")]
    ismarried: Annotated[bool, Field(default=False, examples="True or False")]
    height: Annotated[float, Field(..., description="Enter height of the patient in Fts", examples="6.1")]
    weight: Annotated[float, Field(..., description="Enter in weights of patient in kgs")]


# --- Test Data ---
# This dictionary contains the necessary 'phone_no' and 'email_address'
# within the 'contact_details' field.
patient_data = {
    "id": 456,
    "name": "Robert Smith",
    "city": "London",
    "age": "45",
    "gender": "Male",
    "height": 5.9,
    "weight": 185.5,
    "diseases": ["Hypertension", "Asthma"],
    "contact_details": {
        "phone_no": "555-123-4567",
        "email_address": "robert.smith",
    },
}

""" --- Initialization and Validation ---"""
try:
    # Pydantic validates the data automatically when creating the instance
    patient_instance = Patient(**patient_data)

    # print("✅ Model Initialization Successful!")
    # print(patient_instance)     #type <class '__main__.Patient'>
    # print(patient_instance.__dict__)     # shows as a dict

except Exception as e:
    print(f"❌ Model Initialization Failed! Error: {e}")
