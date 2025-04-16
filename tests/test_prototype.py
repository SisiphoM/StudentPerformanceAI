# tests/test_prototype.py
from creational_patterns.prototype import PrototypeAIModel

def test_model_clone():
    original = PrototypeAIModel("linear", {"alpha": 0.01})
    clone = original.clone()
    assert clone is not original
    assert clone.model_type == original.model_type
    assert clone.parameters == original.parameters