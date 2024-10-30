from database.models import Student
from database import get_db

def new_student_db(name_of_student, age_year, phone_number, clas, klas_rukovodit, subjects_today,photo_path):
    with next(get_db()) as db:
        new_student = Student(name_of_student=name_of_student, age_year=age_year, phone_number=phone_number,
                    clas=clas, klas_rukovodit=klas_rukovodit, subjects_today=subjects_today, photo_path=photo_path)
        db.add(new_student)
        db.commit()
        return 'Студент успешно зарегистрирован!'

def get_exact_student_db(student_id):
    with next(get_db()) as db:
        exact_student = db.query(Student).filter_by(id=student_id).first()
        if exact_student:
            return f'Найден студен с id:{student_id}'
        return 'Не найден такой студент!'

def get_all_students_db():
    with next(get_db()) as db:
        all_students = db.query(Student).all()
        return all_students

def update_student_db(student_id, change_info, new_info):
    with next(get_db()) as db:
        update_student_info = db.query(Student).filter_by(id=student_id).first()
        if update_student_info:
            if change_info == 'name_of_student':
                update_student_info.name = new_info
            elif change_info == 'age_year':
                update_student_info.age_year = new_info
            elif change_info == 'clas':
                update_student_info.clas = new_info
            elif change_info == 'phone_number':
                update_student_info.phone_number = new_info
            elif change_info == 'klas_rukovodit':
                update_student_info.klas_rukovodit = new_info
            db.commit()
            return 'Данные успешно изменены!'
        return f'Не найден учитель по id:{student_id}!'

def delete_student_db(student_id):
    with next(get_db()) as db:
        delete_student = db.delete(Student).filter_by(id=student_id).first()
        if delete_student:
            return  f'Студент с id:{student_id} удален!'
        return f'Студент под id:{student_id} не удалился!'

def update_student_photo_db(student_id, new_path):
    with next(get_db()) as db:
        photo = db.query(Student).filter_by(id=student_id).first()
        if photo:
            photo.photo_path = new_path
            db.commit()
            return f'Фотография ученика был успешно сохранен!'
        return False

def delete_student_photo_db(student_id: int):
    with next(get_db()) as db:
        photo = db.query(Student).filter(student_id).first()
        if photo:
            photo.file_path = None
            db.delete(photo)
            db.commit()
            return f"Фотография с ID {student_id} успешно удалена"
        return f"Фотография с ID {student_id} не найдена"