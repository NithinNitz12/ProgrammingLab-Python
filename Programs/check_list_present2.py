s = [5,10,15,20,25,30]
flag = 0
n = int(input('Enter the number:'))
for i in range(len(s)):
    if n == s[i]:
        flag = 1
        break
if flag == 1:
    print('present')
else:
    print('not present')