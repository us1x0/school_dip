from tkinter.scrolledtext import example

from database.models import Class
from database import get_db
from fastapi import HTTPException

#функция для регистрации класса
def new_class_db(name_of_class, class_rukovod, how_many_stud, ugleblyonnost):
    if how_many_stud > 25:
        raise HTTPException(status_code=400, detail="Количество учеников в классе не может превышать 25.")

    with next(get_db()) as db:
        new_class = Class(name_of_class=name_of_class, class_rukovod=class_rukovod, how_many_stud=how_many_stud,
                              ugleblyonnost=ugleblyonnost)
        db.add(new_class)
        db.commit()
        return True


def get_all_classes_db():
    with next(get_db()) as db:
        all_classes = db.query(Class).all()
        return all_classes

def get_exact_class_db(class_id: int):
    with next(get_db()) as db:
        exact_class = db.query(Class).filter_by(id=class_id).first()
        if exact_class:
            return exact_class
        return f'Класс по id:{class_id} нету!'

def update_class_db(class_id, change_info, new_info):
    with next(get_db()) as db:
        update_class = db.query(Class).filter_by(id=class_id).first()
        if update_class:
            if change_info == "name_of_class":
                update_class.name_of_class = new_info
            elif change_info == "class_rukovod":
                update_class.class_rukovod = new_info
            elif change_info == "how_many_stud":
                update_class.how_many_stud = new_info
            elif change_info == "ugleblyonnost":
                update_class.ugleblyonnost = new_info
            db.commit()
            return True
        return f'Класс под id{class_id} не найден!'

def delete_class_db(class_id):
    with next(get_db()) as db:
        delete_class = db.query(Class).filter_by(id=class_id).first()
        if delete_class:
            db.delete(delete_class)
            db.commit()
            return  True
        return f'Класс под id:{class_id} не удалился!'


