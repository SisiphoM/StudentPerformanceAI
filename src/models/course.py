# src/models/course.py
class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.enrolled_students = []

    def assign_student(self, student):
        self.enrolled_students.append(student)

    def calculate_average(self):
        # TODO: Implement average calculation across students
        pass