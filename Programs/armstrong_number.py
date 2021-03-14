##    Write a function to display the armstrong numbers from 1 and 500
def arm(n):
    s = 0
    t = n
    while(n!=0):
        r = n%10
        n = int(n/10)
        s = s+(r*r*r)
    if s == t:    
        print(s)
    return s
i = 1
while(i<=500):
    x = arm(i)
    i = i+1

    #not solved