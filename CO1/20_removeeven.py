list = [1,2,3,4,5,6,7,8,9,10]
nlist = []

# for l in list:
#     if l%2!=0:
#         nlist.append(l)

nlist = [item for item in list if(item%2!=0)]
print(nlist)