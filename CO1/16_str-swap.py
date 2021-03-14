str1 = input("Enter the first string:")
str2 = input("Enter the second string:")
x = str1[0]
str1 = str1.replace(str1[0],str2[0])
str2 = str2.replace(str2[0],x)
print(str1,str2)