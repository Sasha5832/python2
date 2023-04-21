import math
x = 5.6
y = 2
print("Zadanie 1 pk a)")
print(math.ceil(x))
print(math.floor(x))
print(round(x))
b = "Hello World"
print(b[2:5])

# if math.ceil(x) != x or math.ceil(y) != y:
#     print(math.fmod(x, y))
# else:
#     print(x % y)

if type(x) == "float" or type(y) == "float":
    print(math.fmod(x, y))
else:
    print(x % y)

a = 5
n = 5
for k in range(1, n):
    print(math.log(a, k+1), end="|")

print("\n")

print(math.exp(a))
print(math.e**a)
print(math.pow(math.e, a))


print("Zadanie 1 pk b)")

# math.pow(-5,5)
# -3125.0
# -5**5
# -3125

# math.remainder(8,5)
# -2.0
# 8%5
# 3


print("Zadanie 2 pk a)")
g = str("abcdefghigklmnopqrstuvwdxyz")
print(g[12])
# g = program21.g
# g[12]
# 'm'
n = g[3] + g[5]
print(n)

print(len(g))

print("Zadanie 2 pk b)")

