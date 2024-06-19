from helpers import (
    exit_program,
    list_students,
    find_student_by_name,
    find_student_by_id,
    create_student,
    update_student,
    delete_student,
    list_departments,
    find_department_by_name,
    find_department_by_id,
    create_department,
    update_department,  
    delete_department,
    list_teachers,
    find_teacher_by_name,
    find_teacher_by_id,
    create_teacher,
    update_teacher,
    delete_teacher,
    list_department_teachers
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_students()
        elif choice == "2":
            find_student_by_name()
        elif choice == "3":
            find_student_by_id()
        elif choice == "4":
            create_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            list_departments()
        elif choice == "8":
            find_department_by_name()
        elif choice == "9":
            find_department_by_id()
        elif choice == "10":
            create_department()
        elif choice == "11":
            update_department()  
        elif choice == "12":
            delete_department()
        elif choice == "13":
            list_teachers()
        elif choice == "14":
            find_teacher_by_name()
        elif choice == "15":
            find_teacher_by_id()
        elif choice == "16":
            create_teacher()
        elif choice == "17":
            update_teacher()
        elif choice == "18":
            delete_teacher()
        elif choice == "19":
            list_department_teachers()
        else:
            print("Oops! Review your choice")

def menu():
    print("Kindly Select an Option: ")
    print("0. Exit the program")
    print("1. List Students")
    print("2. Find student by name")
    print("3. Find student by id")
    print("4. Create student")
    print("5. Update student")
    print("6. Delete student")
    print("7. List departments") 
    print("8. Find department by name")  
    print("9. Find department by id")  
    print("10. Create department")
    print("11. Update department")
    print("12. Delete department")
    print("13. List teachers")
    print("14. Find teacher by name")
    print("15. Find teacher by id")
    print("16. Create teacher")
    print("17. Update teacher")
    print("18. Delete teacher")
    print("19. List department teachers")

if __name__ == "__main__":
    main()
