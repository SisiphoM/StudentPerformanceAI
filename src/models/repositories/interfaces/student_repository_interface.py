# repositories/interfaces/student_repository_interface.py

from abc import ABC, abstractmethod
from domain.student import Student
from typing import List, Optional

class StudentRepositoryInterface(ABC):
    @abstractmethod
    def add_student(self, student: Student) -> None:
        pass

    @abstractmethod
    def get_student_by_id(self, student_id: str) -> Optional[Student]:
        pass

    @abstractmethod
    def list_students(self) -> List[Student]:
        pass

    @abstractmethod
    def delete_student(self, student_id: str) -> bool:
        pass
