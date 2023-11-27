from itertools import combinations
 
letters ="1234567890"
 
a = combinations(letters, 4)
y = [' '.join(i) for i in a]
 
print(y)