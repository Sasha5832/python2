
a = input("Podaj liczbe 1: ")
b = input("Podaj liczbe 2: ")

if a > b:
    najw = a
else:
    najw = b
a = int(a)
b = int(b)
najw = int(najw)

for i in range(1, najw):
    if a % i == 0 & b % i == 0:
        n = i


print(n)
