import math as m


def p(x):
    print(x)


x = 2.562
print(round(x, 1))
print(type(round(m.pow(2, 5))))
p(pow(2, 10))

lista = []

for x in range(0, 14):
    lista.append(m.pow(x, 5))

lista2 = []
for x in range(0, 19):
    lista2.append(m.factorial(x))

lista3 = []
for x in range(0, 19):
    lista3.append(pow(m.e, x))

lista4 = ["Oleksandr", "Hrypas"]
lista5 = [len(x) for x in lista4]

p("Zadanie 1 b)")
p("Pk. 1")
p(lista)
p("Pk. 2")
p(lista2)
p("Pk. 3")
p(lista3)
p("Pk. 4")
p(lista5)



