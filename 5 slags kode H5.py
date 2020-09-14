class Employee:
    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def fullname(self):
        return self.firstname + self.lastname

emp_1 = Employee("John", "Smith", "@company")
emp_2 = Employee("Mary", "Sue", "@company")
emp_3 = Employee("Antony", "Walker", "@company")

print(emp_1.fullname)
