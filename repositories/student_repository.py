from repositories.repository import Repository
from domain.student import Student

class StudentRepository(Repository[Student, str]):
    pass
