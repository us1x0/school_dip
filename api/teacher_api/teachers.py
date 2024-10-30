from fastapi import FastAPI, APIRouter, UploadFile, File
import random
from pydantic import BaseModel
from typing import Optional
from database.teacher_service import (get_new_teacher_db, get_exact_teacher_db, get_all_teachers_db,
                                      change_info_teacher_db, delete_teacher_db)

teacher_router = APIRouter(prefix='/students', tags=['Учителя'])

class Teacher(BaseModel):
    name: str
    age_year: int
    clas: str
    phone_number: str
    kakoy_predmet: str

@teacher_router.post('/register-new-teacher')
async def register_teacher_api(teacher_data: Teacher):
    teacher_db = dict(teacher_data)
    result =get_new_teacher_db(**teacher_db)
    if result:
        return {"status": 1, "message": "Учитель успешно добавлен"}
    return {"status": 0, "message": "Учитель не добавлен!"}

@teacher_router.get('/get-exact-teacher')
async def get_exact_teacher_api(teacher_id: int):
    result = get_exact_teacher_db(teacher_id)
    return result

@teacher_router.get('/get-all-teachers')
async def get_all_teacher_api():
    return get_all_teachers_db()

@teacher_router.put('/update-teacher-info')
async def update_teacher_api(teacher_id: int, change_info: str, new_info: str):
    result = change_info_teacher_db(teacher_id, change_info, new_info)
    if result:
        return 'Данные учителя успешна изменены!'
    return result

@teacher_router.delete('/delete-teacher')
async def delete_teacher_api(teacher_id):
    return delete_teacher_db(teacher_id)

@teacher_router.post('/add_teacher_photo')
async def add_teacher_photo(teacher_id: int, photo_file: UploadFile = File(...)):
    file_id = random.randint(1, 10000000)
    if photo_file:
        with open(f"database/teachers_photo/photo_photo_{file_id}_{teacher_id}.jpg", "wb") as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)
            return {"status":1, "message": "Успешно загружено"}
    return {"status":0, "message": "Ошибка!"}

@teacher_router.delete('/delete-teacher-photo')
async def delete_teacher_photo_db(teacher_id: int):
    result = delete_teacher_photo_db(teacher_id)
    if result:
        return {'status': 1, 'message': 'Фото успешно удален'}
    return {'status': 0, "message": result}