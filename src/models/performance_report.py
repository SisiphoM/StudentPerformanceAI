# src/models/performance_report.py
class PerformanceReport:
    def __init__(self, report_id, student_id, prediction_score, risk_level):
        self.report_id = report_id
        self.student_id = student_id
        self.prediction_score = prediction_score
        self.risk_level = risk_level

    def generate_report(self):
        # TODO: Logic to generate a report
        pass

    def export_to_pdf(self):
        # TODO: Export the report to PDF
        pass