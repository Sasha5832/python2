import math


names = ['apple', 'banana', 'pomergranate', 'plum', 'orange', 'melon', 'cherry', 'watermelon']

names3 = [x for x in names if 'u' in x or 'o' in x]
print(names3)

lenz = [len(i) for i in names3]

print(lenz)
