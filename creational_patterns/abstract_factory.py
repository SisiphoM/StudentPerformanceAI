# creational_patterns/abstract_factory.py
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class TextInput(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        return "Rendering Windows Button"

class MacButton(Button):
    def render(self):
        return "Rendering Mac Button"

class WindowsTextInput(TextInput):
    def render(self):
        return "Rendering Windows Text Input"

class MacTextInput(TextInput):
    def render(self):
        return "Rendering Mac Text Input"

class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    @abstractmethod
    def create_text_input(self):
        pass

class WindowsUIFactory(UIFactory):
    def create_button(self):
        return WindowsButton()
    def create_text_input(self):
        return WindowsTextInput()

class MacUIFactory(UIFactory):
    def create_button(self):
        return MacButton()
    def create_text_input(self):
        return MacTextInput()
