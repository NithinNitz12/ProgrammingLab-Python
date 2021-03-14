num=int(input("enter number of words to be stored : "))

longest = 0
for i in range(num):
    word = input("enter a word : ")
    length = len(word)
    if(length>longest):
        longest=length

print("Longest word is : "+str(longest)+" letters long.")

