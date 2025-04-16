# tests/test_simple_factory.py
from creational_patterns.simple_factory import PredictionFactory

def test_linear_model():
    model = PredictionFactory.get_model("linear")
    assert model.train() == "Training Linear Regression"

def test_neural_model():
    model = PredictionFactory.get_model("neural")
    assert model.train() == "Training Neural Network"