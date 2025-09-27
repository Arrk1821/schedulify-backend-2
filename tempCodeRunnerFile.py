from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class Faculty(BaseModel):
    id: str
    name: str
    available: List[str]  
    max_load: Optional[int] = Field(default=20)

class Room(BaseModel):
    id: str
    name: str
    type: str
    capacity: int

class Course(BaseModel):
    code: str
    name: str
    credits: int
    faculty_ids: List[str]

class Batch(BaseModel):
    id: str
    name: str
    students: int
    required_courses: List[str]
    elective_courses: Optional[List[str]] = []

class Constraint(BaseModel):
    type: str
    details: Dict

class GenerateRequest(BaseModel):
    faculties: List[Faculty]
    rooms: List[Room]
    courses: List[Course]
    batches: List[Batch]
    constraints: Optional[List[Constraint]] = []

class SlotAssignment(BaseModel):
    course_code: str
    batch_id: str
    faculty_id: str
    room_id: str
    day: str
    slot: str

class TimetableResponse(BaseModel):
    assignments: List[SlotAssignment]
    success: bool
    message: Optional[str] = None

class Conflict(BaseModel):
    type: str
    details: Dict

class ConflictCheckResponse(BaseModel):
    conflicts: List[Conflict]
    success: bool