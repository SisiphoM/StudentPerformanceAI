# src/models/assignment.py
class Assignment:
    def __init__(self, assignment_id, title, due_date, max_score):
        self.assignment_id = assignment_id
        self.title = title
        self.due_date = due_date
        self.max_score = max_score
        self.submitted = False

    def submit(self):
        self.submitted = True

    def grade_assignment(self, score):
        # TODO: Grade logic
        pass