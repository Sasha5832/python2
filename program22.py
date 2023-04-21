import math
g = str("abcdefghigklmnopqrstuvwdxyz")
h = str()


def parzyste(g):
    print(g[::2])


def ostatnie(g, n=1):
    print(g[len(g)-n::])


def odwrotni(g):
    x = len(g)-1
    odp = g[::-1]

    return odp


def ktorydluzszy(g, h):
    if len(g) > len(h):
        return g
    else:
        return h


def wstawianie(c, d):
    odp = "My name is {imie}. My date of birth is {dataUr}."
    odp = odp.format(imie=c, dataUr=d)
    return odp


c = "Oleksandr"
d = "02-11-2004"
parzyste(g)
print(ostatnie(g, 5))
print(odwrotni(g))
print(ktorydluzszy(g, h))
print(wstawianie(c, d))
