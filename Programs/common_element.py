## Write a function to find the common elements present in 2 list

def com(l1,l2):
    comel = list()
    for el in l1:
        if el in l2:
            comel.append(el)
    return comel

l1 = ['apple','orange','cherry','mango']
l2 = ['watermelon','strawberry','bananan','apple','mango']
x = com(l1,l2)
print(x)