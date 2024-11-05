
class Employee:
    def __init__(self, name, age, salary):
        self.name = name if name else "unknown"
        self.age = age if age >= 18 and age <= 65 else 18
        self.salary = salary if salary > 0 else "cannot be negative"
        
    def display_details(self):
        return f'name: {self.name} \nage: {self.age} \nsalary: {self.salary}'
    def calculate_annual_salary(self):
        return f'annual salary: {self.salary * 12}'
    

class Manager(Employee):
    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.team_size = team_size
        
    def display_details(self):
        return f'name: {self.name} \nage: {self.age} \nsalary: {self.salary}\nteam size: {self.team_size}'
        
    def calculate_bonus(self):
        return f'Bonus: {self.salary + (self.salary * 0.1) if self.team_size > 5 else self.salary + (self.salary * 0.03)}'
    

class Developer(Employee):
    def __init__(self, name, age, salary, programming_langauge):
        super().__init__(name, age, salary)
        self.programming_language = programming_langauge
    
    def display_details(self):
        return f'name: {self.name} \nage: {self.age} \nsalary: {self.salary}\nprogramming language: {self.programming_language}'

    def calculate_overtime_pay(self, extra_hours):
        overtime_pay = extra_hours * 50
        return f'Overtime pay: {overtime_pay}'    

class SeniorDeveloper(Developer):
    def __init__(self,name , age, salary, years_of_experience):
        super().__init__(name, age, salary, "None")
        self.years_of_experience = years_of_experience
    
    def display_details(self):
        return f'name: {self.name} \nage: {self.age} \nsalary: {self.salary}\nyears of experience: {self.years_of_experience}'    
    
    def calculate_experience_bonus(self):
        return f'Experience Bonus: {self.salary + (self.years_of_experience * 200) if self.years_of_experience > 5 else "not five years"}'

    

zyron = Employee('zyron', 20, 10000)
print('=============EMPLOYEE=============')
print(zyron.display_details())
print(zyron.calculate_annual_salary())

raymund = Manager('raymund', 20, 10000, 7)
print('=============MANAGER=============')
print(raymund.display_details())
print(raymund.calculate_bonus())

raymundo = Developer('raymundo', 20, 10000, 'Java')
print('=============DEVELOPER=============')
print(raymundo.display_details())
print(raymundo.calculate_overtime_pay(100))

zeron = SeniorDeveloper('zeron', 20, 10000, 10)
print('=============SENIOR DEVELOPER=============')
print(zeron.display_details())
print(zeron.calculate_experience_bonus())

