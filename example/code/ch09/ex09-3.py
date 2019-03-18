# class
# define Student class
class Student:
    # constructor
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade
    # method
    def display_student(self):
        print("name = " + self.name)
        print("grade = " + str(self.__getgrade()))
        
    def __getgrade(self):
        return self.__grade

# create object
s1 = Student("Python", 85)

# call method
s1.display_student()
# print("s1.__getgrade() = " + str(s1.__getgrade()))

# get data member
print("s1.name = " + s1.name)
# print(s1.__grade)