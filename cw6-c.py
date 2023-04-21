import math

n = 5
n = int(n)


e1 = ((1+(1/n))**n)
print(e1)


k = 0
e2 = 0

for x in range(0, n):
    e2 += 1/math.factorial(k)

print(e2)
print(e1-math.e)
print(e2-math.e)
print(math.fabs(e1-math.e))
print(math.fabs(e2-math.e))
