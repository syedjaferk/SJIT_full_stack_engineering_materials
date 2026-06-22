from typing import List, Optional
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field
import motor.motor_asyncio
from bson import ObjectId


app = FastAPI(title="Simple Student API")


client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.mydb
collection = db.students

class StudentBase(BaseModel):
    name: str
    age: int
    course: str

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    course: Optional[str] = None

class Student(StudentBase):
    id: str = Field(..., alias="_id")

    class Config:
        validate_by_name = True


def doc_to_student(doc):
    doc["_id"] = str(doc["_id"])
    return Student(**doc)

@app.get("/health", status_code=204)
async def health_check():
    # Check MongoDB connection
    try:
        await db.command("ping")
    except Exception:
        raise HTTPException(status_code=503, detail="Service unavailable")
    return Response(status_code=204)

# Create
@app.post("/students/", response_model=Student)
async def create_student(student: StudentCreate):
    result = await collection.insert_one(student.dict())
    doc = await collection.find_one({"_id": result.inserted_id})
    return doc_to_student(doc)

# Read all
@app.get("/students/", response_model=List[Student])
async def list_students():
    students = []
    async for doc in collection.find():
        students.append(doc_to_student(doc))
    return students

# Read one
@app.get("/students/{student_id}", response_model=Student)
async def get_student(student_id: str):
    doc = await collection.find_one({"_id": ObjectId(student_id)})
    if not doc:
        raise HTTPException(status_code=404, detail="Student not found")
    return doc_to_student(doc)

# Update (PUT)
@app.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: str, student: StudentCreate):
    await collection.update_one({"_id": ObjectId(student_id)}, {"$set": student.dict()})
    doc = await collection.find_one({"_id": ObjectId(student_id)})
    if not doc:
        raise HTTPException(status_code=404, detail="Student not found")
    return doc_to_student(doc)

# Partial update (PATCH)
@app.patch("/students/{student_id}", response_model=Student)
async def patch_student(student_id: str, student: StudentUpdate):
    update_data = {k: v for k, v in student.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    await collection.update_one({"_id": ObjectId(student_id)}, {"$set": update_data})
    doc = await collection.find_one({"_id": ObjectId(student_id)})
    if not doc:
        raise HTTPException(status_code=404, detail="Student not found")
    return doc_to_student(doc)

# Delete
@app.delete("/students/{student_id}", status_code=204)
async def delete_student(student_id: str):
    result = await collection.delete_one({"_id": ObjectId(student_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return None
