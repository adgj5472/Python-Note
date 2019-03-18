# class
# define Student class
class Student:
    # construtor
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    # method
    def display_student(self):
        print("name = " + self.name)
        print("grade = " + str(self.grade))
        
    def show_name(self):
        return self.name

# create object
s1 = Student("Python", 85)

# call method
s1.display_student()
print("s1.show_name() = " + s1.show_name())

# get data member
print("s1.name = " + s1.name)
print("s1.grade = " + str(s1.grade))
