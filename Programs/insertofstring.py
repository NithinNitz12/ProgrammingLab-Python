#write a program to insert in the middle of a string
str = input("Enter a string:")
s = input("Enter a second string:")
n = int((len(str)/2))
print(str[0:n]+s+str[n:])