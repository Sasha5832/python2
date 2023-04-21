import math

a = input("Podaj liczbe 1: ")
b = input("Podaj liczbe 2: ")
a = int(a)
b = int(b)

nwd = math.gcd(a, b)
p = a/nwd
q = b/nwd
print(p)
print(q)
print(p/q)
