from database.models import Subjects
from database import get_db

def add_subject_db(name):
    with next(get_db()) as db:
        new_subject = Subjects(name=name)
        db.add(new_subject)
        db.commit()
        return 'Предмет успешно добавлен!'

def get_all_subjects_db():
    with next(get_db()) as db:
        all_subjects = db.query(Subjects).all()
        return all_subjects

def delete_subject_db(subject_id):
    with next(get_db()) as db:
        subject = db.query(Subjects).filter_by(id=subject_id).first()
        if subject:
            db.delete(subject)
            db.commit()
            return f'Предмет с id:{subject_id} удален!'
        return f'Предмет с id:{subject_id} не найден!'
