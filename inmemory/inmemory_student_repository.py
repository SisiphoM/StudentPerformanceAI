# repositories/inmemory/inmemory_student_repository.py
from repositories.base_repository import Repository
from typing import Optional, List
from src.models.student import Student

class InMemoryStudentRepository(Repository[Student, str]):
    def __init__(self):
        self._storage = {}

    def save(self, student: Student) -> None:
        self._storage[student.student_id] = student

    def find_by_id(self, student_id: str) -> Optional[Student]:
        return self._storage.get(student_id)

    def find_all(self) -> List[Student]:
        return list(self._storage.values())

    def delete(self, student_id: str) -> None:
        self._storage.pop(student_id, None)
