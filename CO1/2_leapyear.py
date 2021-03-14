current = int(input("Enter current year: "))
final = int(input("Enter final year: "))

if current < final:
  print ("Here is a list of leap years between " + str(current) + " and " + str(final)  + ":")
  
while current < final:  
    if current % 4 == 0:
        print(current)
    if current % 100 == 0 and current % 400 == 0:
        print(current)
    current +=1
