number = int(input("enter a number : "))
factors = []

for i in range(number):
    if(number%(i+1)==0):
        factors.append(i+1)

print("The factors of "+str(number)+" : ")
print(factors)