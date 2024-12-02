from .database import student_collection
from bson import ObjectId

def create_student(student: dict):
    result = student_collection.insert_one(student)
    return str(result.inserted_id)

def get_students(filters: dict = None, fields: list=None):
    query = {}
    projection = {field: 1 for field in fields} if fields else None

    if filters:
        if filters.get("country"):
            query["address.country"] = filters["country"]
        if filters.get("age"):
            query["age"] = {"$gte": filters["age"]}
    return list(student_collection.find(query, projection))

def get_student_by_id(student_id: str):
    return student_collection.find_one({"_id": ObjectId(student_id)})

def update_student(student_id: str, update_data: dict):
    student_collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": update_data}
    )

def delete_student(student_id: str):
    student_collection.delete_one({"_id": ObjectId(student_id)})
