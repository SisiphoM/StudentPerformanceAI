from fastapi import FastAPI
from api.student_routes import router as student_router
from api.course_routes import router as course_router
from api.performance_routes import router as performance_router

app = FastAPI(title="Student Performance Prediction API")

app.include_router(student_router, prefix="/students")
app.include_router(course_router, prefix="/courses")
app.include_router(performance_router, prefix="/performance")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Performance API"}
