from fastapi import FastAPI, APIRouter,UploadFile,File
import random
from pydantic import BaseModel
from typing import Optional
from database.student_service import (new_student_db, get_all_students_db, get_exact_student_db,
                                      update_student_db, delete_student_db, update_student_photo_db)

student_router = APIRouter(prefix='/students', tags=['Cтуденты'])

class Student(BaseModel):
    name_of_student: str
    age_year: int
    clas: str
    phone_number: str
    klas_rukovodit: Optional[str]=None
    subjects_today: int
    photo_path: Optional[str]=None

@student_router.post('/register-new-student')
async def register_student_api(student_data: Student):
    student_db = student_data.dict()
    result = new_student_db(**student_db)
    if result:
        return {"status": 1, "message": "Ученик успешно добавлен"}
    return {"status": 0, "message": "Ученик не добавлен!"}

@student_router.get('/get-exact-student')
async def get_exact_student_api(student_id: int):
    result = get_exact_student_db(student_id)
    return result

@student_router.get('/get-all-students')
async def get_all_students_api():
    return get_all_students_db()

@student_router.put('/update-student-info')
async def update_student_api(student_id: int, change_info: str, new_info: str):
    result = update_student_db(student_id, change_info, new_info)
    if result:
        return 'Данные ученик успешна изменены!'
    return result

@student_router.delete('/delete-student')
async def delete_student_api(student_id):
    return delete_student_db(student_id)

@student_router.post('/add_student_photo')
async def add_student_photo(student_id: int, photo_file: UploadFile = File(...)):
    file_id = random.randint(1, 10000000)
    if photo_file:
        with open(f"database/students_photo/students_photo_{file_id}_{student_id}.jpg", "wb") as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)

            return {"status":1, "message": "Успешно загружено"}
    return {"status":0, "message": "Ошибка!"}

@student_router.post('/add_student_photo')
async def update_student_photo(student_id: int, photo_file: UploadFile = File(...)):
    file_id = random.randint(1, 10000000)
    if photo_file:
        with open(f"database/students_photo/photo_photo_{file_id}_{student_id}.jpg", "wb") as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)
            update_student_photo_db(student_id, photo.name)
            return {"status":1, "message": "Успешно загружено"}
    return {"status":0, "message": "Ошибка!"}

@student_router.delete('/delete-student-photo')
async def delete_student_photo_db(student_id: int):
    result = delete_student_photo_db(student_id)
    if result:
        return {'status': 1, 'message': 'Фото успешно удален'}
    return {'status': 0, "message": result}