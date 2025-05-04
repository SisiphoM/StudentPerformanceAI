import pytest
from repositories.inmemory.inmemory_student_repository import InMemoryStudentRepository
from domain.student import Student

def test_save_and_find():
    repo = InMemoryStudentRepository()
    student = Student(id="1", name="Alice", grade=85)
    repo.save(student)
    assert repo.find_by_id("1") == student

def test_find_all():
    repo = InMemoryStudentRepository()
    repo.save(Student(id="1", name="Alice", grade=85))
    repo.save(Student(id="2", name="Bob", grade=90))
    all_students = repo.find_all()
    assert len(all_students) == 2

def test_delete():
    repo = InMemoryStudentRepository()
    student = Student(id="1", name="Alice", grade=85)
    repo.save(student)
    repo.delete("1")
    assert repo.find_by_id("1") is None
