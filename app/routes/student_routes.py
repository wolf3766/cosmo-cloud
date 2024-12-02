from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.crud import create_student, get_students, get_student_by_id, update_student, delete_student
from app.models import Student, UpdateStudent

router = APIRouter()

def serialize_student(student):
    student["_id"] = str(student["_id"])  # Convert ObjectId to string
    return student

@router.post("/students", status_code=201)
def create_student_endpoint(student: Student):
    student_data = student.dict()
    student_id = create_student(student_data)
    return {"id": student_id}

@router.get("/students")
def list_students(country: str = None, age: int = None):
    fields = ["name", "age"]
    filters = {"country": country, "age": age}
    students = get_students(filters, fields)

    serialized_students = [serialize_student(student) for student in students]
    return {"data": students}

@router.get("/students/{id}")
def get_student(id: str):
    student = serialize_student(get_student_by_id(id))
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.patch("/students/{id}", status_code=204)
def update_student_endpoint(id: str, student: UpdateStudent):
    update_data = {k: v for k, v in student.dict().items() if v is not None}
    update_student(id, update_data)

@router.delete("/students/{id}")
def delete_student_endpoint(id: str):
    delete_student(id)
    return {"message": "Student deleted successfully"}
