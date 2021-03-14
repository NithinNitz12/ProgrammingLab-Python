class Student:
    "information about the class"
    studentcount = 0
    def __init__(self,roll,name,course):
        self.roll = roll
        self.name = name
        self.course = course
        Student.studentcount = Student.studentcount+1
    def displaycount():
        print("No. of student objects",Student.studentcount)
    def display(self):
        print("Roll no.=",self.roll)
        print("Name=",self.name)
        print("Course Name=",self.course)
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,"Destroyed")
s1 = Student(123,'PETER','MCA')
s2 = Student(456,'BRUCE','MCA')
s1.display()
s2.display()
Student.displaycount()
del s1