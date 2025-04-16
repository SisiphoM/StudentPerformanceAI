# creational_patterns/builder.py
class StudentProfile:
    def __init__(self):
        self.name = None
        self.age = None
        self.email = None
        self.courses = []

    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, email={self.email}, courses={self.courses})"

class StudentBuilder:
    def __init__(self):
        self.profile = StudentProfile()

    def set_name(self, name):
        self.profile.name = name
        return self

    def set_age(self, age):
        self.profile.age = age
        return self

    def set_email(self, email):
        self.profile.email = email
        return self

    def add_course(self, course):
        self.profile.courses.append(course)
        return self

    def build(self):
        return self.profile