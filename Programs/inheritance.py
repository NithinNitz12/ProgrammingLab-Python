class Student:
    #information about the class
    def getdata(self,roll,name,course):
        self.roll = roll
        self.name = name
        self.course = course
    def display(self):
        print("Roll no=",self.roll)
        print("Name=",self.name)
        print("Course Name=",self.course)
class Test(Student):                            #Inherited
    def getmarks(self,mark):
        self.mark = mark
    def displaymarks(self):
        self.display()
        print("Mark=",self.mark)
s1 = Test()
s1.getdata(501,"Tony Stark","MCA")
s1.getmarks(200)
s1.displaymarks()