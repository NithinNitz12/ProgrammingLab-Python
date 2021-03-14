class Rectangle:
    __length = 0
    __width = 0
    __area = 0
    def __init__(self,l,b):
        self.__length = l
        self.__width = b
    def area1(self):
        self.__area = self.__length*self.__width
    def __lt__(self,other):
        if(self.__area < other.__area):
            return True
        else:
            return False
ob1 = Rectangle(5,10)
ob1.area1()
ob2 = Rectangle(4,2)
ob2.area1()
if(ob1<ob2):
    print("Second rectangle is greater")
else:
    print("First rectangle is greater")