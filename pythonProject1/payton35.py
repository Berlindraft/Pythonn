# Raymund Zyron Abella BSIT 2-B

# student record management system
# add, remove, update, display, average, total, search, exit

# pre defined values
student_record = [
    {"name": "Professor X", "roll_number": 101, "mark": 1.0},
    {"name": "Jean Grey", "roll_number": 102, "mark": 1.4},
    {"name": "Storm", "roll_number": 103, "mark": 1.5},
    {"name": "Gambit", "roll_number": 104, "mark": 2.6},
    {"name": "Cyclops", "roll_number": 105, "mark": 1.5}
]

# studentRecords = [
#     {"name": ["professor", "jean", "storm", "gambit"]}
#     {"roll_number": [101, 102, 103, 104]},
#     {"mark": [1.0, 1.4, 2.6, 1.5]}
# ]

while True:
    print('===============STUDENT RECORDS===============')
    print("[ 1 ] add a student ")
    print("[ 2 ] remove a student ")
    print("[ 3 ] update student mark ")
    print("[ 4 ] display all student records ")
    print("[ 5 ] display the average of students ")
    print("[ 6 ] display number of student  ")
    print("[ 7 ] search for a student ")
    print("[ 8 ] EXIT ")
    choice = int(input("ENTER CHOICE: ").strip())

    # adding a student function
    if choice == 1:
        name = input("Add name: ")
        roll_number = int(input("Add roll number: "))
        marks = float(input("Add marks: "))
        student_record.append({"name": name, "roll_number": roll_number, "mark": marks})
        print(f"Added Student:  \nName: {name} \nRoll Number: {roll_number} \nMarks: {marks}")

     # removing a student function
    elif choice == 2:
        roll_number = int(input("Enter roll number to remove: "))
        for student in student_record:
            if student['roll_number'] == roll_number:
                student_record.remove(student)
                print(f"Student with {roll_number} removed")

    # update student mark function
    elif choice == 3:
        roll_number = int(input("Enter roll number to update mark: "))
        for student in student_record:
            if student['roll_number'] == roll_number:
                newMark = float(input(f"Enter new mark for {student['name']}: "))
                student['mark'] = newMark
                print(f"Mark updated successfully")

    # display student function
    elif choice == 4:
        print("========STUDENTS========")
        for student in student_record:
            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Mark: {student['mark']}")

    # average of all student marks function
    elif choice == 5:
        total_marks = sum(student['mark'] for student in student_record)
        average_marks = total_marks / len(student_record)
        print(f"Average mark of all students: {average_marks:.2f}")

    # total number of students function
    elif choice == 6:
        print(f"Total number of students: {len(student_record)}")

    # searching student function
    elif choice == 7:
        roll_number = int(input("Enter roll number to search: "))
        for student in student_record:
            if student['roll_number'] == roll_number:
                print(f"Student found: Name: {student['name']}, Mark: {student['mark']}")
            else:
                print("Student not found...")
   
    # end program function
    elif choice == 8:
        print("Program End")
        break

    else:
        print("invalid input")
