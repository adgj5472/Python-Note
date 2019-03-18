# class
# define Student class
class Student:
    count = 0
    # constructor
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.count += 1
    # method
    def display_count(self):
        print("students = " + str(Student.count))

    def display_student(self):
        print("name = " + self.name)
        print("grade = " + str(self.grade))

# create object
s1 = Student("Lisk", 85)
s2 = Student("Mary", 75)
s3 = Student("Eric", 65)

# call method
s1.display_count()
s2.display_count()
s3.display_count()

print("Number of students = " + str(Student.count))
