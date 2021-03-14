#Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to
# find sum of 2 time. 

class Time:
    __hour = 0
    __minute = 0
    __second = 0
    def __init__(self,h,m,s):
        self.__hour = h
        self.__minute = m
        self.__second = s
    def __add__(self,other):
        self.sh=self.__hour+other.__hour
        self.sm=self.__minute+other.__minute
        self.ss=self.__second+other.__second
        return(self.sh,self.sm,self.ss)

ob1 = Time(5,30,15)
ob2 = Time(2,10,50)
print(ob1+ob2)