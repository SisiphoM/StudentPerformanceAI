# domain/student.py

from dataclasses import dataclass

@dataclass
class Student:
    student_id: str
    name: str
    email: str
    performance_score: float
