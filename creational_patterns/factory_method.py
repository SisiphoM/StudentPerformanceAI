# creational_patterns/factory_method.py
from abc import ABC, abstractmethod

class ReportExporter(ABC):
    @abstractmethod
    def export(self, data):
        pass

class PDFExporter(ReportExporter):
    def export(self, data):
        return f"Exporting report to PDF: {data}"

class CSVExporter(ReportExporter):
    def export(self, data):
        return f"Exporting report to CSV: {data}"