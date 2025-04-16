# tests/test_abstract_factory.py
from creational_patterns.abstract_factory import WindowsUIFactory, MacUIFactory

def test_windows_ui():
    factory = WindowsUIFactory()
    assert factory.create_button().render() == "Rendering Windows Button"
    assert factory.create_text_input().render() == "Rendering Windows Text Input"

def test_mac_ui():
    factory = MacUIFactory()
    assert factory.create_button().render() == "Rendering Mac Button"
    assert factory.create_text_input().render() == "Rendering Mac Text Input"