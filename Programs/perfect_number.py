## Write a function to check a number is perfect number or not

def perfect(n):
    sum = 0
    i = 1
    while(i<n):
        if n%i == 0:
            sum = sum + i
        i = i+1
    if sum == n:
        return 'Perfect'
    else:
        return 'Not Perfect'
n = int(input('Enter a number:'))
print(perfect(n))