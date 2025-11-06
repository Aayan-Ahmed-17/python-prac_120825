from pydantic import BaseModel
from typing import List, Dict


class Patient(BaseModel):
    id: int
    name: str
    city: str
    age: int
    gender: str
    ismarried: bool = False
    height: float
    weight: float
    diseases: List[str]
    contact_details: Dict[str, str]


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

# --- Initialization and Validation ---
try:
    # Pydantic validates the data automatically when creating the instance
    patient_instance = Patient(**patient_data)

    print("✅ Model Initialization Successful!")
    print(patient_instance)     #type <class '__main__.Patient'>
    # print(patient_instance.__dict__)     # shows as a dict

except Exception as e:
    print(f"❌ Model Initialization Failed! Error: {e}")
