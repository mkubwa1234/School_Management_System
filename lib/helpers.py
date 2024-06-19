from models.department import Department
from models.student import Student
from models.teacher import Teacher

def exit_program():
    print("Welcome Back! 🙋️")
    exit()

# Functions for Department model
def list_departments():
    departments = Department.get_all()
    if not departments:
        print("No departments found.")
    else:
        for department in departments:
            print(department)

def find_department_by_name():
    name = input("Enter department name: ")
    department = Department.find_by_name(name)
    if department:
        print(department)
    else:
        print(f"No department found with the name '{name}'.")

def find_department_by_id():
    department_id = int(input("Enter department ID: "))
    department = Department.find_by_id(department_id)
    if department:
        print(department)
    else:
        print(f"No department found with the ID '{department_id}'.")

def create_department():
    name = input("Enter department name: ")
    location = input("Enter department location: ")
    head = input("Enter department head: ")
    department = Department.create(name, location, head)
    print(f"Department created: {department}")

def update_department():  
    department_id = int(input("Enter department ID: "))
    department = Department.find_by_id(department_id)
    if department:
        name = input(f"Enter new name (current: {department.name}): ") or None
        location = input(f"Enter new location (current: {department.location}): ") or None
        head = input(f"Enter new head (current: {department.head}): ") or None
        if name:
            department.name = name
        if location:
            department.location = location
        if head:
            department.head = head
        department.update()
        print(f"Department updated: {department}")
    else:
        print(f"No department found with the ID '{department_id}'.")

def delete_department():
    department_id = int(input("Enter department ID: "))
    department = Department.find_by_id(department_id)
    if department:
        department.delete()
        print(f"Department deleted: {department}")
    else:
        print(f"No department found with the ID '{department_id}'.")

# Functions for Student model
def list_students():
    students = Student.get_all()
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(student)

def find_student_by_name():
    name = input("Enter student name: ")
    student = Student.find_by_name(name)
    if student:
        print(student)
    else:
        print(f"Error,No student found with the name '{name}'.")

def find_student_by_id():
    student_id = int(input("Enter student ID: "))
    student = Student.find_by_id(student_id)
    if student:
        print(student)
    else:
        print(f"Error, No student found with the ID '{student_id}'.")

def create_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    gender = input("Enter student gender: ")
    email = input("Enter student email: ")
    contact = input("Enter student contact: ")
    student = Student.create(name, age, gender, email, contact)
    print(f"Student created: {student}")

def update_student():
    student_id = int(input("Enter student ID: "))
    student = Student.find_by_id(student_id)
    if student:
        updates = {}

        name = input(f"Enter new name (current: {student.name}): ").strip()
        if name:
            updates['name'] = name

        age = input(f"Enter new age (current: {student.age}): ").strip()
        if age:
            updates['age'] = int(age)

        gender = input(f"Enter new gender (current: {student.gender}): ").strip()
        if gender:
            updates['gender'] = gender

        email = input(f"Enter new email (current: {student.email}): ").strip()
        if email:
            updates['email'] = email

        contact = input(f"Enter new contact (current: {student.contact}): ").strip()
        if contact:
            updates['contact'] = contact

        for key, value in updates.items():
            setattr(student, key, value)

        student.update()
        print(f"Student updated: {student}")
    else:
        print(f"No student found with the ID '{student_id}'.")

def delete_student():
    student_id = int(input("Enter student ID: "))
    student = Student.find_by_id(student_id)
    if student:
        student.delete()
        print(f"Student deleted: {student}")
    else:
        print(f"No student found with the ID '{student_id}'.")

# Functions for Teacher model
def list_teachers():
    teachers = Teacher.get_all()
    if not teachers:
        print("No teachers found.")
    else:
        for teacher in teachers:
            print(teacher)

def find_teacher_by_name():
    name = input("Enter teacher name: ")
    teacher = Teacher.find_by_name(name)
    if teacher:
        print(teacher)
    else:
        print(f"No teacher found with the name '{name}'.")

def find_teacher_by_id():
    teacher_id = int(input("Enter teacher ID: "))
    teacher = Teacher.find_by_id(teacher_id)
    if teacher:
        print(teacher)
    else:
        print(f"No teacher found with the ID '{teacher_id}'.")

def create_teacher():
    name = input("Enter teacher name: ")
    gender = input("Enter teacher gender: ")
    subject = input("Enter teacher subject: ")
    email = input("Enter teacher email: ")
    department_id = int(input("Enter department ID: "))
    department = input("Enter department name: ")
    teacher = Teacher.create(name, gender, subject, email, department_id, department)
    print(f"Teacher created: {teacher}")

def update_teacher():
    teacher_id = int(input("Enter teacher ID: "))
    teacher = Teacher.find_by_id(teacher_id)
    if teacher:
        name = input(f"Enter new name (current: {teacher.name}): ") or None
        gender = input(f"Enter new gender (current: {teacher.gender}): ") or None
        subject = input(f"Enter new subject (current: {teacher.subject}): ") or None
        email = input(f"Enter new email (current: {teacher.email}): ") or None
        department_id = input(f"Enter new department ID (current: {teacher.department_id}): ") or None
        department = input(f"Enter new department name (current: {teacher.department}): ") or None
        if name:
            teacher.name = name
        if gender:
            teacher.gender = gender
        if subject:
            teacher.subject = subject
        if email:
            teacher.email = email
        if department_id:
            teacher.department_id = int(department_id)
        if department:
            teacher.department = department
        teacher.update()
        print(f"Teacher updated: {teacher}")
    else:
        print(f"No teacher found with the ID '{teacher_id}'.")

def delete_teacher():
    teacher_id = int(input("Enter teacher ID: "))
    teacher = Teacher.find_by_id(teacher_id)
    if teacher:
        teacher.delete()
        print(f"Teacher deleted: {teacher}")
    else:
        print(f"No teacher found with the ID '{teacher_id}'.")

def list_department_teachers():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        for teacher in department.teachers():
            print(teacher)
    else:
        print(f'Department {id_} not found')