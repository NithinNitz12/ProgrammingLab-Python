print("Enter 3 numbers:")
n1 = input()
n2 = input()
n3 = input()
if n1 > n2 and n1 > n3:
    print(n1," is greater")
elif n2 > n1 and n2 > n3:
    print(n2," is greater")
else:
    print(n3," is greater")