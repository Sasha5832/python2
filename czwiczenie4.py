import math
names = ["michal", "nela", "ola", "przemek"]

names2 = [x.capitalize() for x in names]
print(names2)

names3 = [x for x in names if 'l' in x]
print(names3)
names4 = [x.capitalize() for x in names if 'a' in x[-1]]
print(names4)

odpowiedz = 0
for x in range(0, len(names)):
    odpowiedz += [len(x) for x in names][x]
print(odpowiedz)
odp = 0
for x in names:
    odp += len(x)
    print(odp)

# cwiczenie 2


def iloczyn(*num):
    odp = 1
    for n in num:
        odp = odp * n
    print(odp)


iloczyn(2, 4, 5)


def sum_potega(*num, x):
    odp = 0
    for n in num:
        odp += pow(n, x)
    print(odp)


sum_potega(4, 3, x=2)


def mean(*num):
    odp = 0
    for n in num:
        odp += n
    print(odp/len(num))


mean(3, 5)


def gmean(*num):
    odp = 1
    for n in num:
        odp = odp * n
    print(pow(odp, 1/len(num)))


gmean(2, 4, 8)


def suma_str(*str):
    odp = 0
    for n in str:
        odp += len(n)
    print(odp)


suma_str("Hello", "World")

# Czwiczenie3


def funkcja(**phonebook):
    for n, value in phonebook.items():
        print(n, "na numer", value)


phonebook = {'Anna': 1234, 'Bartosh': 4321}

funkcja(**phonebook)

miesiecy = {'styczeń': 2700, 'luty': 300}


def zarobek(**miesiecy):
    suma = 0
    for n, value in miesiecy.items():
        print(n, "na numer", value)
        suma += value

    print(mean(suma/len(miesiecy)))


zarobek(**miesiecy)
