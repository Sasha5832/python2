import math


def przepisz(my_list):
    unique_value = []
    for value in my_list:
        if value not in unique_value:
            unique_value.append(value)
    return unique_value


my_list = [1, 2, 2, 3, 4, 2, 6, 5]
print(przepisz(my_list))
string = "abcdifghijklmnopqrstuwdxyz"
clean_string = "".join(x for x in string if x.isalnum())
revers = clean_string[::-4]
print(revers)


def iloczyn(*num, n=2):
    odp = 1
    for x in num:
        odp *= x**n
    return odp


print(iloczyn(1, 2, 3, 4, 5))

list5 = ['apple', 'banana', 'pomergranate', 'plum', 'orange', 'melon', 'cherry', 'watermelon']

listodp = [x for x in list5 if 'u' in x or 'o' in x]
print(listodp)
lenz = [len(i) for i in listodp]

print(lenz)


def newton(n, k):
    gora = 1
    dol = 1
    for i in range(k):
        gora *= n - i
        dol *= i + 1
    return gora // dol


print(newton(7, 2))

