import csv
# create a students list
students = []
# open the payton.csv file
# csv means comma separated value
# with open and close the file
'''
with open('payton13.csv') as file:
    for line in file:
        # strips the line in the file to two parts separated by comma
        first_name, last_name = line.rstrip().split(",")
        # dictionary to store the key value pairs of the names
        student = {
            "first_name": first_name,
            "last_name": last_name
        }
        # appends the student dict to the list
        students.append(student)

'''
with open("payton13.csv") as file:
        reader = csv.reader(file)
        for first_name, last_name in reader:
            students.append({"first_name": first_name, "last_name": last_name})


# the function that returns first name of the student
# def get_name(student):
#     return student['first_name'].lower()
# the function above is not needed anymore because of the lambda function
# loops to the names in each line to print them in sorted alphabetically
# lambda an anonymous function
for student in sorted(students, key=lambda student: student['first_name'].lower(), reverse=False):
    print(f"Student name: {student['first_name']} {student['last_name']}")

'''
use the csv library to help handling csv files because there are errors that
are even hard to solve
'''

