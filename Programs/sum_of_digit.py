n = int(input('Enter the number:'))
s = 0
while(n!=0):
    r = int(n%10)
    n = n/10
    s = r+s
print('Sum:',int(s))