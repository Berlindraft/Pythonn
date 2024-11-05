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

    if choice == 1:
        name = input("Enter student name: ")
        roll_number = int(input('Enter student roll number: ').strip())
        marks = int(input('Enter student marks: ').strip())
        student_record.append(
            {"name": name,
             "roll_number": roll_number,
             "mark": marks
             })
        print(f"student with roll number {roll_number} added to records")
    elif choice == 2:
        rmv = int(input('Enter roll number of student to remove: ').strip())
        for student in student_record:
            if student["roll_number"] == rmv:
                student_record.remove(student)
    elif choice == 3:
        roll_number = int(input('Enter roll number of student to update mark: ').strip())
        new_mark = int(input('Enter new mark: ').strip())
        for student in student_record:
            if student['roll_number'] == roll_number:
                student['mark'] == new_mark
            else:
                print('student not found')
        print('student updated successfully')
    elif choice == 4:
        for student in student_record:
            print(student)
    elif choice == 5:
        total = 0
        for student in student_record:
            if student['mark'] > -1:
                total += student['mark']
        average = total/len(student_record)
        print(f' the average marks of the students is {average: .2f}')
    elif choice == 6:
        print(f' the total number of students is {len(student_record)}')
    elif choice == 7:
        search = int(input('Enter roll number of student: ').strip())
        for student in student_record:
            if student['roll_number'] == search:
                print(f'student found {student['name']}')
    elif choice == 8:
        print('Exiting the program... ')
        break