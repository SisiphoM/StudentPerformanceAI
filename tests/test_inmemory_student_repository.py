# tests/test_inmemory_student_repository.py
import pytest
from repositories.inmemory.inmemory_student_repository import InMemoryStudentRepository # type: ignore
from src.models.student import Student

def test_save_and_find_student():
    repo = InMemoryStudentRepository()
    student = Student(student_id="1", name="Sisipho", email="sisipho@example.com")

    repo.save(student)
    retrieved = repo.find_by_id("1")

    assert retrieved is not None
    assert retrieved.name == "Sisipho"
    assert retrieved.email == "sisipho@example.com"

def test_find_all_students():
    repo = InMemoryStudentRepository()
    student1 = Student(student_id="1", name="Sisipho", email="sisipho@example.com")
    student2 = Student(student_id="2", name="Luxolo", email="luxolo@example.com")

    repo.save(student1)
    repo.save(student2)
    all_students = repo.find_all()

    assert len(all_students) == 2

def test_delete_student():
    repo = InMemoryStudentRepository()
    student = Student(student_id="1", name="Sisipho", email="sisipho@example.com")

    repo.save(student)
    repo.delete("1")
    retrieved = repo.find_by_id("1")

    assert retrieved is None
