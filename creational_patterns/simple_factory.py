# creational_patterns/simple_factory.py
class AIModel:
    def train(self):
        pass

class LinearRegressionModel(AIModel):
    def train(self):
        return "Training Linear Regression"

class NeuralNetworkModel(AIModel):
    def train(self):
        return "Training Neural Network"

class PredictionFactory:
    @staticmethod
    def get_model(model_type):
        if model_type == "linear":
            return LinearRegressionModel()
        elif model_type == "neural":
            return NeuralNetworkModel()
        else:
            raise ValueError("Unknown model type")