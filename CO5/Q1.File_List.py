fh = open("Text.txt")
lst = list()
for line in fh:
    # print(line)
    lst.append(line)
print(lst)