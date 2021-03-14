## Write a program to check  a string is palindrome or not 
# without using reverse function available in the string

def palindrome(str):
    for i in range(0,int(len(str)/2)):
        if(str[i]!=str[len(str)-i-1]):
            return 0
    return 1
    
str = input('Enter the string:')
x = palindrome(str)
if(x==1):
    print("Palindrome")
else:
    print("Not Palindrome")
