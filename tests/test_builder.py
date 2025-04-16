# tests/test_builder.py
from creational_patterns.builder import StudentBuilder

def test_student_builder():
    builder = StudentBuilder()
    student = (builder.set_name("John")
                     .set_age(22)
                     .set_email("john@example.com")
                     .add_course("AI")
                     .add_course("Math")
                     .build())
    assert student.name == "John"
    assert student.age == 22
    assert student.email == "john@example.com"
    assert len(student.courses) == 2