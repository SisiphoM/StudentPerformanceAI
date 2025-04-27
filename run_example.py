# run_example.py
from factories.repository_factory import RepositoryFactory
from src.models.student import Student

def main():
    student_repo = RepositoryFactory.get_student_repository()

    student = Student(student_id="1", name="Sisipho", email="sisipho@example.com")
    student_repo.save(student)

    retrieved = student_repo.find_by_id("1")
    if retrieved:
        print(f"Retrieved Student: {retrieved.name} - {retrieved.email}")

    all_students = student_repo.find_all()
    print(f"Total Students: {len(all_students)}")

if __name__ == "__main__":
    main()
