from typing import List
from schemas import SlotAssignment, GenerateRequest

def generate_timetable(request: GenerateRequest) -> List[SlotAssignment]:
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    slots = ["9AM", "11AM", "1PM", "3PM"]
    
    assignments: List[SlotAssignment] = []
    
    course_index = 0
    for batch in request.batches:
       
        for course_code in batch.required_courses:
            
            course = next((c for c in request.courses if c.code == course_code), None)
            if not course:
                continue
            
            
            faculty_id = course.faculty_ids[course_index % len(course.faculty_ids)]
            room = request.rooms[course_index % len(request.rooms)]
            day = days[course_index % len(days)]
            slot = slots[course_index % len(slots)]
            
            assignments.append(
                SlotAssignment(
                    course_code=course.code,
                    batch_id=batch.id,
                    faculty_id=faculty_id,
                    room_id=room.id,
                    day=day,
                    slot=slot
                )
            )
            course_index += 1
        
        
        for course_code in batch.elective_courses:
            course = next((c for c in request.courses if c.code == course_code), None)
            if not course:
                continue
            
            faculty_id = course.faculty_ids[course_index % len(course.faculty_ids)]
            room = request.rooms[course_index % len(request.rooms)]
            day = days[course_index % len(days)]
            slot = slots[course_index % len(slots)]
            
            assignments.append(
                SlotAssignment(
                    course_code=course.code,
                    batch_id=batch.id,
                    faculty_id=faculty_id,
                    room_id=room.id,
                    day=day,
                    slot=slot
                )
            )
            course_index += 1
            
    return assignments
