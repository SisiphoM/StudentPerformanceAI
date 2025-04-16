# tests/test_singleton.py
from creational_patterns.singleton import DatabaseConnection

def test_singleton_instance():
    db1 = DatabaseConnection.get_instance()
    db2 = DatabaseConnection.get_instance()
    assert db1 is db2
    assert db1.connection == "Connected to DB"