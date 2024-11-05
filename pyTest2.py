# raymund zyron abella

class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        
    def display_info(self):
        pass

class Department(Hospital):
    def __init__(self, name, location, dept_name, dept_head):
        super().__init__(name, location)
        self.dept_name = dept_name
        self.dept_head = dept_head
    
    

class Doctor(Department):
    def __init__(self, name, location, dept_name, dept_head, doctor_name, specialization):
        super().__init__(name, location, dept_name, dept_head)
        self.doctor_name = doctor_name
        self.specialization = specialization