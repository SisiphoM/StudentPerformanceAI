from repositories.student_repository import StudentRepository
from domain.student import Student

class InMemoryStudentRepository(StudentRepository):
    def __init__(self):
        self._students = {}

    def save(self, entity: Student) -> None:
        self._students[entity.id] = entity

    def find_by_id(self, id: str) -> Student | None:
        return self._students.get(id)

    def find_all(self) -> list[Student]:
        return list(self._students.values())

    def delete(self, id: str) -> None:
        if id in self._students:
            del self._students[id]
