from models import Department, Student, Teacher, Session

def seed_departments(session):
    Department.create(session, "Computer", "Alexa Hall")
    Department.create(session, "Mathematics", "Gretsa Hall")
    Department.create(session, "English", "Dreamland Hall")
    Department.create(session, "History", "Moi Hall")
    Department.create(session, "Chemistry", "Anita Hall")

def seed_students(session):
    Student.create(session, "Alpha Matara", 20, "Male", "Alphamisma@gmail.com", "07895454")
    Student.create(session, "Simpson Rafiki", 22, "Female", "rafikisimpson@gmail.com", "07897654")
    Student.create(session, "Drake Kipchirchir", 19, "Male", "chirchirdrake@gmail.com", "078934213")
    Student.create(session, "Samuel Kamau", 21, "Male", "skamau@gmail.com", "07324567")
    Student.create(session, "Fred Tracy", 23, "Female", "tracy@example.com", "0745123456")

def seed_teachers(session):
    computer_science_dept = Department.find_by_name(session, "Computer")
    mathematics_dept = Department.find_by_name(session, "Mathematics")
    english_dept = Department.find_by_name(session, "English")
    history_dept = Department.find_by_name(session, "History")
    chemistry_dept = Department.find_by_name(session, "Chemistry")

    Teacher.create(session, "Kevin Mkali", "Programming", computer_science_dept.id)
    Teacher.create(session, "Martial Munene", "Algorithms", computer_science_dept.id)
    Teacher.create(session, "Wyclif Bazuu", "Matrices", mathematics_dept.id)
    Teacher.create(session, "Juddie Juliana", "Literature", english_dept.id)
    Teacher.create(session, "Frank Faulu", "World History", history_dept.id)
    Teacher.create(session, "Grace Gikonyo", "Organic Chemistry", chemistry_dept.id)

def seed_data():
    session = Session()
    seed_departments(session)
    seed_students(session)
    seed_teachers(session)
    session.close()

if __name__ == "__main__":
    seed_data()
    print("Database seeded 👍️")
