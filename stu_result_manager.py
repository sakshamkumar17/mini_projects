student = {}
while True:
    print("\n---Student Result Manager---")
    print("1. Add Student and marks")
    print("2. View all students")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ").strip().title()
        marks = int(input("Enter marks: "))
        student[name] = marks
        print("Student Added successfully")
    elif choice == "2":
        if not student:
            print("No Student found!!")
        for name, marks in student.items():
            print(f"{name} : {marks}")
    elif choice == "3":
        name = input("Enter name to show result: ").strip().title()
        if name in student:
            marks = student[name]
            print(f"{name} : {marks}")
            if marks > 40:
                print("Pass")
            else:
                print("Fail")
        else:
            print("Student not found!!")
 
    elif choice == "4":
        print("Program Terminated!!")
        break
    else:
        print("Invalid Value")