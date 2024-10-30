from database.models import Teacher
from database import get_db

#функция для регистрации учителя
def get_new_teacher_db(name, age_year, clas, kakoy_predmet, phone_number):
    with next(get_db()) as db:
        new_teacher = Teacher(name=name, age_year=age_year, clas=clas, kakoy_predmet=kakoy_predmet,
                            phone_number=phone_number)
        db.add(new_teacher)
        db.commit()
        return True

def get_all_teachers_db():
    with next(get_db()) as db:
        all_teachers = db.query(Teacher).all()
        return all_teachers

def get_exact_teacher_db(teacher_id: int):
    with next(get_db()) as db:
        exact_teacher = db.query(Teacher).filter_by(id=teacher_id).first()
        if exact_teacher:
            return f'Найден учитель c id:{teacher_id}'
        return f'Не найден учитель с id:{teacher_id}!'

def change_info_teacher_db(teacher_id, change_info, new_info):
    with next(get_db()) as db:
        change_teacher_info = db.query(Teacher).filter_by(id=teacher_id).first()
        if change_teacher_info:
            if change_info == 'name':
                change_teacher_info.name = new_info
            elif change_info == 'age_year':
                change_teacher_info.age_year = new_info
            elif change_info == 'klas':
                change_teacher_info.klas = new_info
            elif change_info == 'kakoy_predmet':
                change_teacher_info.kakoy_predmet = new_info
            elif change_info == 'phone_number':
                change_teacher_info.phone_number = new_info
            db.commit()
            return 'Данные успешно изменены!'
        return f'Не найден учитель по id:{teacher_id}!'

def delete_teacher_db(teacher_id):
    with next(get_db()) as db:
        delete_teacher = db.delete(Teacher).filter_by(id=teacher_id).first()
        if delete_teacher:
            return  f'Учитель с id:{teacher_id} удален!'
        return f'Учитель под id:{teacher_id} не удалился!'

def update_teacher_photo(teacher_id: int, new_path: str):
    with next(get_db()) as db:
        photo = db.query(Teacher).filter_by(id=teacher_id).first()
        if photo:
            photo.photo_path = new_path
            db.commit()
            return f'Фотография учителя был успешно сохранен!'
        return False


def delete_teacher_photo_db(teacher_id: int):
    with next(get_db()) as db:
        photo = db.query(Teacher).filter(id=teacher_id).first()
        if photo:
            photo.file_path = None
            db.delete(photo)
            db.commit()
            return f"Фотография учителя с ID {teacher_id} успешно удалена"
        return f"Фотография учителя с ID {teacher_id} не найдена"
