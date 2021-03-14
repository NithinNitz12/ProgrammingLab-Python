## Read a string from the keyboard write a function to find the 
# sum of uppercase and lowercase letters present in the string

def count(st):
    countL = 0
    countU = 0
    for s in st:
        print(s)
        if s >= 'a':
            countL = countL + 1
        elif s >='A':
            countU = countU + 1
        else:
            pass
    print('Lower=',countL,"Upper=",countU)


str = input('Enter the string:')
count(str)