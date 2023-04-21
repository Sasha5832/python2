import math

n = input("Podaj liczbe: ")
n = int(n)


if n<100 and n>0:
    for x in range(1, n):
        for b in range(1, n):
            print(x * b)
else:
    print("n is too large")
