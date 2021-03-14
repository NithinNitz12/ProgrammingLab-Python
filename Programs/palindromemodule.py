##Write a program to get a string from the keyboard and use that 
# module to check whether it is palindrome or not

def palindrome(str):
    rst = ''
    index = len(str)
    while(index>0):
        rst += str[index-1]
        index = index-1
    if(rst==str):
        print('Palindrome')
    else:
        print('Not Palindrome')