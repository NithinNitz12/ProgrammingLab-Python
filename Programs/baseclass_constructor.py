class Student:
    #information about the class
    def __init__(self,roll,name,course):
        self.roll = roll
        self.name = name
        self.course = course
    def display(self):
        print('Roll no. =',self.roll)
        print('Name =',self.name)
        print('Course name =',self.course)
class Test(Student):
    def __init__(self,roll,name,course,mark):
        Student.__init__(self,roll,name,course)
        self.mark = mark
    def displaymarks(self):
        self.display()
        print('Mark =',self.mark)
s1 = Test(501,'Steve','History',500)
s1.displaymarks()