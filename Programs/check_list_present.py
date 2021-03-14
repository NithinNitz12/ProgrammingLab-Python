li = [1,2,3,4,5,6,7,8,9,10]
flag = 0
n = int(input('Enter the number:'))
for l in li:
    print(l)
    if n == l:
        flag = 1
if flag == 1:
    print('present')
else:
    print('not present')