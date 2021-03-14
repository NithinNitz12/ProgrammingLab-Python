V = ['a','e','i','o','u','A','E','I','O','U']
print("V = ['a','e','i','o','u']")

w = str(input("Enter the word: "))

x = [x for x in w if any([v in x for v in V])]
x = list(x)
print ("Vowels in given word:",x)
      
      
