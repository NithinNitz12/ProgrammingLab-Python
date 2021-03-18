newFile = open("content.txt","w")
newFile.write("Pizza \nNuggets \nShawarma \nNoodles \nSteak")
newFile.close()

readFile = open("content.txt","r")
lines = readFile.readlines()
readFile.close()

oddFile = open("oddcontent.txt","w")
for i in range(0,len(lines),2):
    oddFile.write(lines[i])
oddFile.close()