class Employee:
    empcount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1

    def display_count(self):
        print ("Total Employee {}"
            .format(Employee.empcount))

    def display_employee(self):
        print("Name : ", self.name,  ", Salary: ",
            self.salary)

emp1 = Employee("Lisk", 22000)
emp2 = Employee("Mary", 55000)

emp1.display_employee()
emp2.display_employee()

print(hasattr(emp1, 'salary'))
print(getattr(emp1, 'salary'))

emp1.display_count()
emp2.display_count()
