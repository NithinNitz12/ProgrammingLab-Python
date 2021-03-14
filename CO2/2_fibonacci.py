list = [0,1]
length = int(input("Enter length for Fibonacci series : "))

if(length == 1):
    print(str([0]))

if(length == 2):
    print(str([0,1]))

if(length>=3):
    i = 2
    while(i<length):
        term = list[i-2]+list[i-1]
        list.append(term)
        i=i+1
print(list)
