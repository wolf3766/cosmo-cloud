from pydantic import BaseModel, Field
from typing import Optional

class Address(BaseModel):
    city: str
    country: str

class Student(BaseModel):
    name: str
    age: int
    address: Address

class UpdateStudent(BaseModel):
    name: Optional[str]
    age: Optional[int]
    address: Optional[Address]
