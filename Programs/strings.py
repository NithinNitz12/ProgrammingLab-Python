#Python Notes

str = "It is easy to learn python"
print("Swapcase:",str.swapcase())
print("Capitalize:",str.capitalize())
print("Title:",str.title())
print("Replace:",str.replace("is","was"))

print("*****")

str2 = "How easy is python to learn, Java is not so easy, c not at all easy to code"
print(str2.replace("is","was"))
print(str2.replace("is","was",1))
print(str2.count("is"))

print("*****")

s = "Hello"
print(s + " All")
print(s*3)

print("*****")

s = "Python Programming Lab"
l = s.split()
print("Split:",l)
print("Length:",len(l))
print("Upper:",s.isupper())
print("Digit:",s.isdigit())

print("*****")

s = "Hello All"
print(s.find("e"))
print(s.find("All"))
print(s.find("l",4,8))

print("*****")

print(max(5,20,30))
print(min(12,4,100))

print("*****")

import math
print(math.sqrt(25))

print("*****")

li = [1,2,3]
l1 = [1,"apple",3.4,20]
print("List:",l1)
print(l1*3)
print(l1[1:4])
l = [20,1,12.5,0,100]
print("Length:",len(l))
print("Max:",max(l))
print("Min:",min(l))

print("*****")

s = "1 2 3 0"
l = list(map(int,s.split()))
print(l)
l = max(list(map(int,s.split())))
print(l)

print("*****")

l = [1,2,3.5]
l.append(100)
print(l)
l.append(2)
print("Count:",l.count(2))
l.remove(2)
print(l)
del l[3]
print(l)

print("*****")

a = [1,2,5]
b = [3,4]
a.extend(b)
print("Extended:",a)

print("*****")

a.reverse()
print(a)

print("*****")

a = [1,2,3,4]
a.insert(2,100)
a[4] = 300
print(a)

print("*****")

a.sort()
print(a)
a.sort(reverse=True)
print("Reversed:",a)

print("*****")

a.clear()
print(a)

print("*****")

l = [1,2,3.5,2+9j]
a = l.copy()
print(a)

#H.W - 16,13,12,6

print("*****")

t = (1,2,3) #Tuple
print("Tuple:",t[1:])
t = (1,2.5,20)
print("Min:",min(t))
print(list(t))
l = ["Hello","All"]
s = tuple(l)    #Conversion list to tuple
print("s=",s)
t = "apple",1,100
print(t)

print("*****")

x,y,z = t
print("x=",x)
print("y=",y)
print("z=",z)

print("*****")

#set --- No duplication
s = {1,2,3,4}
print(s)
s = {1,14,3,1} #Duplication ignored
print(s)
print("Len=",len(s))
print(sum(s))
print(sorted(s))
s.add(100)
print(s)
s.remove(100)   #If the element is not present in the set it shows error
print(s)
s.discard(35)   #No error by using discard()
print(s)

print("*****")

#Math functions
    #Union
s = {1,2,3}
t = {20,2,100}
u = s.union(t)  #No change in s
print("Union:",u)
print(s|t)
print(s.update(t))  #Change in s
print(s)
a = {1,2,3}
b = {5}
print(a.union(b))
print(a)
print(b)
    #Intersection
a = {1,2,3}
b = {2,3,5}
print("Intersection:",a.intersection(b))
a.intersection_update(b)
print(a)
print("a&b=",a&b)
print(a.difference(b))
a = {2,3,5,10}
b = {6,5,10,12,45}
print(a-b)
print(b-a)
print("Symmetric Difference:",a.symmetric_difference(b))
l = [1,2,3,4,5]
m = [10,13]
a = set(l)
b = set(m)
print(a.isdisjoint(b))

s = frozenset({1,2,3})  #Elements cannot be altered
print(s)

print("*****")

#Dictionary
dict = {}
dict['one'] = "Hello All"
dict['two'] = "Stay Safe"
dict['three'] = "Stay Healthy"
print(dict)
dict2 = {'name=':'Tony Stark','age':50,}
print(dict2)
print(dict['one'])
print(dict.keys())
print(dict.values())
print(dict.items())
dict.update(dict2)
print("After update function",dict)

d = {'m1':20, 'm2':30}
d1 = {'name':'Peter Parker'}
s = d.copy()
print(s)
d.update(d1)
print(d)
d1['age'] = 24
print(d1)
print(sorted(d1.items()))
print(sorted(d1.keys()))

print("*****")

#name of the students and total marks display the result in desecending
#order
#H.W 17,18

##n = int(input("Enter a number:"))
##if n==0:
 ##   print("Zero")

print("*****")

n = [1,2,3,4,5,6,7,8,9,10]
s = 0
for i in n:
    s = s + i
    print("sum=",s)

print("*****")

flowers = ['rose','lotus','jasmine']
for flower in flowers:
    print(flower)

for letter in 'program':
    print(letter)

s = 0
for i in range(11):
    s = s + i
print('sum=',s)

print("*****")

s = 0
for i in range(2,12,2):
    s = s + i
    print('sum=',s)

#Write a program to check whether a number is present in the list of given numbers

s = [1,2,3]
for i in range(len(s)):
    print(s[i])

print("*****")

'''n = int(input("Enter the limit:"))
s = 0
i = 1
while(i<=n):
    s = s+i
    i = i+1
print("Sum of first ",n," natural numbers is ",s)'''

##Factorial of a number
##Write a program to find the sum of the digit of a number
##Write a program to find number that are divisible by 7 and multiple of 5 
# within the range 1000 and 2000 both included
##Write a 
##To print true If 2 given numbers are equal or their sum is equal to 
##

s = [x**2 for x in range(11)]
print(s)

s = {x for x in 'abcdefghijklmnopqrstuvwxyz' if x not in 'aeiou'}
print(s)

s = [x for x in [20,23,45,26,72] if x%2==0]
print(s)

#Functions---------

'''def sum(a,b):
    s = a+b
    return s
a = int(input('Enter the first number:'))
b = int(input('Enter the second number:'))
r = sum(a,b)
print(r)'''

def calc(a,b):
    s = a+b
    d = a-b
    p = a*b
    q = a/b
    return s,d,p,q
s1,d1,p1,q1 = calc(20,10)
print(s1)
print(d1)
print(p1)
print(q1)

#HW   Write a prgm the value of equation 1+3/3!+5/5!+7/7!.........
##    Write a function to display the armstrong numbers from 1 and 500

print("*****")

# Lambda function......
x=lambda a,b,c:a*b*c
print(x(2,3,5))

l = [1,2,3,4,5]
print(l)
n = list(map(lambda x:x+2,l))
print(n)
n = list(filter(lambda x:x+2,l))
print(n)
n = list(filter(lambda x:(x%2!=0),l))
print(n)

## Read a string from the keyboard write a function to find the 
# sum of uppercase and lowercase letters present in the string
## Write a program to check  a string is palindrome or not 
# without using reverse function available in the string
## Write a function to find the common elements present in 2 list
## Write a function to check a number is perfect number or not

print("*****")

#Reverse_Module
def reverse(st):
    rst = ''
    index = len(st)
    while(index>0):
        rst += st[index-1]
        index = index-1
    return rst
print(reverse('hello'))

print("*****")

import math
print('Pi=',math.pi)
print(math.sqrt(625))

##Write a program to get a string from the keyboard and use that 
# module to check whether it is palindrome or not
##Write a python program to create a dictionary with values as
# the squares of the numbers, import this module to create a 
# dictionary between the range of numbers

