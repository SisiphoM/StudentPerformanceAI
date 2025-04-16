# tests/test_factory_method.py
from creational_patterns.factory_method import PDFExporter, CSVExporter

def test_pdf_export():
    exporter = PDFExporter()
    result = exporter.export("Test Data")
    assert result == "Exporting report to PDF: Test Data"

def test_csv_export():
    exporter = CSVExporter()
    result = exporter.export("Test Data")
    assert result == "Exporting report to CSV: Test Data"