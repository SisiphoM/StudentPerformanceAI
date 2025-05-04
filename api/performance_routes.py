from fastapi import APIRouter
from services.performance_service import predict_performance

router = APIRouter()

@router.get("/predict")
def predict():
    return predict_performance()
