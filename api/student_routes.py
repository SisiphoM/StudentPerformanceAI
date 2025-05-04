from fastapi import APIRouter
from services.student_service import get_all_students

router = APIRouter()

@router.get("/")
def list_students():
    return get_all_students()
