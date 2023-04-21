import math

"""
def wypisz(lista):
    for x in range(0, len(lista)):
        print(lista[x] + "\n")


lista = {2, 4, 6, 7, 4}
wypisz(lista)




def display_unique_values(my_list):
    unique_values = set(my_list)
    for value in unique_values:
        print(value)

"""


def display_unique_values(my_list):
    unique_values = []
    for value in my_list:
        if value not in unique_values:
            unique_values.append(value)
            print(value)


my_list = [3, 2, 2, 2, 1, 4, 5, 4]
display_unique_values(my_list)
