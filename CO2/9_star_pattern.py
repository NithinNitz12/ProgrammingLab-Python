size = int(input("enter the size of the pattern : "))

i=0
j=0

while(i<size):
    line = "*"
    j = 0
    while (j < i):
        line = line + "*"
        j = j + 1
    i=i+1
    print(line)

i=size

while(i>0):
    j = 0
    line = ""
    while (j < i):
        line = line + "*"
        j = j + 1
    i = i - 1
    print(line)