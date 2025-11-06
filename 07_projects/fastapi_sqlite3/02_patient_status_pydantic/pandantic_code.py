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