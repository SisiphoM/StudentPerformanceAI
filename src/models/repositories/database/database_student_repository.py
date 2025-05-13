# repositories/database/database_student_repository.py

from repositories.student_repository import StudentRepository
from domain.student import Student

class DatabaseStudentRepository(StudentRepository):
    def save(self, entity: Student) -> None:
        raise NotImplementedError

    def find_by_id(self, id: str) -> Student:
        raise NotImplementedError

    def find_all(self) -> list[Student]:
        raise NotImplementedError

    def delete(self, id: str) -> None:
        raise NotImplementedError
