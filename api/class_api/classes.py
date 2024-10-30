from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import Optional
from database.classes_service import (new_class_db, get_all_classes_db, get_exact_class_db,
                                      update_class_db, delete_class_db)

class_router = APIRouter(prefix='/classes', tags=['Классы школы'])

class Class(BaseModel):
    name_of_class: str
    class_rukovod: str
    how_many_stud: Optional[int] = 25
    ugleblyonnost: Optional[str] = None

@class_router.post('/new-class')
async def new_class_api(class_data: Class):
    class_db = class_data.dict()
    result = new_class_db(**class_db)
    if result:
        return {"status": 1, "message": "Класс успешно добавлен"}
    return {"status": 0, "message": "Класс не добавлен!"}

@class_router.get('/get-exact-class')
async def get_exact_class_api(class_id: int):
    result = get_exact_class_db(class_id)
    return result

@class_router.get('/get-all-classes')
async def all_classes_api():
    return get_all_classes_db()

@class_router.put('/update-class')
async def update_class_api(class_id: int, change_info: str, new_info: str):
    result = update_class_db(class_id, change_info, new_info)
    if result:
        return 'Данные успешно изменены'
    return result

@class_router.delete('/delete-class')
async def delete_class_api(class_id):
    return delete_class_db(class_id)



