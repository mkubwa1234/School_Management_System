from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    @classmethod
    def create(cls, session, name, location):
        department = cls(name=name, location=location)
        session.add(department)
        session.commit()
        return department

    @classmethod
    def find_by_name(cls, session, name):
        return session.query(cls).filter_by(name=name).first()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    @classmethod
    def create(cls, session, name, age, gender, email, phone):
        student = cls(name=name, age=age, gender=gender, email=email, phone=phone)
        session.add(student)
        session.commit()
        return student

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)
    department = relationship("Department")

    @classmethod
    def create(cls, session, name, subject, department_id):
        teacher = cls(name=name, subject=subject, department_id=department_id)
        session.add(teacher)
        session.commit()
        return teacher

# Database setup
engine = create_engine('sqlite:///school_database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
