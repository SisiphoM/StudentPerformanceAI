from fastapi import APIRouter
from services.course_service import get_all_courses

router = APIRouter()

@router.get("/")
def list_courses():
    return get_all_courses()
