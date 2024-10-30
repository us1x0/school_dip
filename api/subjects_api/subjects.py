from sys import prefix

from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from database.subjects_service import add_subject_db, get_all_subjects_db, delete_subject_db

subject_router = APIRouter(prefix='/subjects', tags=['Предметы'])

class Subject(BaseModel):
    name: str


@subject_router.post('/new-subject')
async def new_subject_api(subject_data: Subject):
    subject_db = subject_data.dict()
    result = add_subject_db(*subject_db)
    if result:
        return {"status": 1, "message": "Предмет успешно добавлен"}
    return {"status": 0, "message": "Предмет не добавлен!"}

@subject_router.get('/get-all-subjects')
async def all_subjects_api():
    return get_all_subjects_db()

@subject_router.delete('/delete-subject')
async def delete_subject_api(subject_id):
    return delete_subject_db(subject_id)