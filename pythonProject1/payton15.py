class Student:
    def __init__(self, first_name, middle_name, last_name):
        # __init__ takes in the argument of self(which can be any name) and other arguments to
        # store them in a student variable
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
''' the function of this class is to assign the names of the students into a student object '''
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

''' the main function creates the student method/object the accesses the get_student function'''
def main():
    student = get_student()
    print(f'{student.last_name}, {student.first_name} {student.middle_name}')
    print(student)


''' get_student() function get the input from the user and sends/returns their values to the Student class '''


def get_student():
    # commented code below is a more tedious way instantiate access the class in the code
    # student = Student()
    # student.first_name = input("First Name: ")
    # student.middle_name = input("Middle Name: ")
    # student.last_name = input("Last Name: ")
    first_name = input("First name: ")
    middle_name = input("Middle name: ")
    last_name = input("Last name: ")

    return Student(first_name, middle_name, last_name)
# Student class gets the arguments of firstname, middlename, and lastname

if __name__ == "__main__":
    main()
