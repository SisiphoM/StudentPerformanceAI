# factories/repository_factory.py
from repositories.inmemory.inmemory_student_repository import InMemoryStudentRepository # type: ignore
from repositories.database.database_student_repository import DatabaseStudentRepository

class RepositoryFactory:
    @staticmethod
    def get_student_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryStudentRepository()
        elif storage_type == "DATABASE":
            return DatabaseStudentRepository()
        else:
            raise ValueError("Unsupported storage type")
