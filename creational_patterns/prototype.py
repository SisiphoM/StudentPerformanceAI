# creational_patterns/prototype.py
import copy

class PrototypeAIModel:
    def __init__(self, model_type, parameters):
        self.model_type = model_type
        self.parameters = parameters

    def clone(self):
        return copy.deepcopy(self)