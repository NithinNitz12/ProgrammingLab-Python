#HW   Write a prgm the value of equation 1+3/3!+5/5!+7/7!.........

def fact(n):
    i = 1
    fact = 1
    while(i<=n):
        fact = i * fact
        i = i+1
    return fact
x = int(input('Enter the number:'))
i = 3
val = 0
while(i<=x):
    val = x/fact(x) + val
    i = i+2
print(1+val)