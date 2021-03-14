def merge(dict1,dict2):
    return(dict1.update(dict2))

dict1 = {'Spider-Man':'Peter Parker', 'IronMan':'Tony Stark'}
dict2 = {'Doctor Strange':'Stephen Strange', 'Deadpool':'Wade Wilson'}
merge(dict1,dict2)
print(dict1)