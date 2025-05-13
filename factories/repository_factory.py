from repositories.inmemory.inmemory_student_repository import InMemoryStudentRepository
from repositories.student_repository import StudentRepository

class RepositoryFactory:
    @staticmethod
    def get_student_repository(storage_type: str) -> StudentRepository:
        if storage_type == "MEMORY":
            return InMemoryStudentRepository()
        elif storage_type == "DATABASE":
            raise NotImplementedError("Database support not implemented yet.")
        else:
            raise ValueError("Invalid storage type")
