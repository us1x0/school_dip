from sqlalchemy import (Column, Integer, String, BigInteger,
Boolean, ForeignKey, DateTime)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.operators import from_

from database import Base
from datetime import datetime

class Class(Base):
    __tablename__='classes'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name_of_class = Column(String, nullable=False, unique=True, index=True)
    class_rukovod = Column(String, nullable=False, unique=True)
    how_many_stud = Column(Integer, default=25)
    ugleblyonnost = Column(String, nullable=False)



class Teacher(Base):
    __tablename__='teachers'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age_year = Column(String, nullable=False)
    clas = Column(String, ForeignKey("classes.name_of_class"))
    kakoy_predmet = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    photo_path = Column(String, nullable=True)

    class_fk = relationship(Class, lazy="subquery", foreign_keys=[clas])

 # Изменено на subject

class Student(Base):
    __tablename__='students'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name_of_student = Column(String, nullable=False)
    age_year = Column(Integer, nullable=False)
    phone_number = Column(String, nullable=False)
    clas = Column(String, ForeignKey('classes.name_of_class'))
    klas_rukovodit = Column(String, ForeignKey("classes.class_rukovod"))
    subjects_today = Column(Integer, default=5)
    photo_path = Column(String, nullable=True)



    class_fk = relationship(Class, lazy="subquery", foreign_keys=[klas_rukovodit])
    class_fk_rukovod = relationship(Class, lazy="subquery", foreign_keys=[clas])


class Subjects(Base):
    __tablename__='subjects'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, ForeignKey('teachers.kakoy_predmet'))

    teacher_fk = relationship(Teacher, lazy="subquery", foreign_keys=[name])


