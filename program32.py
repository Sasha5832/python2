import math
# punkt 1
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(list1+list2)

list3 = []

for x in range(0, len(list2)):
    list3.append(list1[x]+list2[x])

print(list3)

# punkt 2


def nrmies(x):
    if x == "styczeń":
        return 0
    elif x == "luty":
        return 1
    elif x == "marzec":
        return 2
    elif x == "kwiecień":
        return 3
    elif x == "maj":
        return 4
    elif x == "czerwiec":
        return 5
    elif x == "lipiec":
        return 6
    elif x == "sierpień":
        return 7
    elif x == "wrzesień":
        return 8
    elif x == "październik":
        return 9
    elif x == "listopad":
        return 10
    elif x == "grudzień":
        return 11


list4 = ["marzec", "czerwiec", "wrzesień", "październik", "listopad", "styczeń",]
list4.sort(key=nrmies)
print(list4)


# punkt 3
def wynik(a, b):
    odp = []
    for k in a:
        if k[0] > b:
            odp.append(k)
    return odp


nazwiska = ["Hrypas", "Kwitnicki", "Tunik", "Zaharow"]

print(wynik(nazwiska, "H"))

# punkt 4

newlist = [x for x in nazwiska if len(x) > 6]

print(newlist)

# punkt 5

a ="solgos"
b ="QWERTREWQ"


def czypalindrom(a):
    temp1 = []
    temp2 = []
    for x in range(0, len(a)):
        temp1.append(a[x])
        temp2.append(a[x])
    temp2.reverse()
    if temp1 == temp2:
        return "true"
    else:
        return "false"


print(czypalindrom(a))
print(czypalindrom(b))

# punkt 6

list5 = [1, 2, 3, 4, 5]
list6 = [5, 4, 3, 2, 1]


def czysort(a):
    temp = [x for x in a]
    temp.sort(reverse=True)
    if a == temp:
        return True
    else:
        return False


print(czysort(list5))
print(czysort(list6))

# punkt 7
list7 = [1, 2, 3, 4]
# def potega(a):

    
newlist = [x for x in nazwiska if len(x) > 6]

print(newlist)
