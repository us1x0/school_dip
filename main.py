from fastapi import FastAPI

from api.student_api.student import student_router
from api.subjects_api.subjects import subject_router
from api.teacher_api.teachers import teacher_router
from database import engine, Base
from api.class_api.classes import class_router


app = FastAPI(docs_url='/')
Base.metadata.create_all(engine)
app.include_router(class_router)
app.include_router(teacher_router)
app.include_router(student_router)
app.include_router(subject_router)
