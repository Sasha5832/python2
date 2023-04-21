import math


class Fruit:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def isfresh(self):
        if self.color == "brown":
            return False
        else:
            return True

    def __str__(self):
        return("color: "+str(self.color)
               + "\nweight:" + str(self.weight))

    def __add__(self, other):
        return Fruit(self.color+'-'+other.clor,
                     self.weight+other.werigt)


class Apple(Fruit):
    pass


class Banana(Fruit):
    pass


class Orange(Fruit):
    pass


fruit1 = Apple("red", 0.3)
fruit2 = Banana("yellow", 0.5)
fruit3 = Orange("Orange", 0.7)
"""
print(fruit1.color)
print(fruit2.weight)
print(fruit3.color)
print(fruit1.isfresh())
"""


class Account:
    def __init__(self, saldo):
        self.saldo = saldo

    def przelew_miedzy_kontami(self, otheracc, ilosc, operacja):
        if operacja == 'wlpata':
            otheracc.saldo -= ilosc
            self.saldo += ilosc
            return "Operacja zostala wykonana"
        elif operacja == 'wyplata':
            otheracc.saldo += ilosc
            self.saldo -= ilosc
            return "Operacja zostala wykonana"
        else:
            return 'nieprawidlowa operacja'

    def wplata(self, moneyadd):
        self.saldo += moneyadd
        return "Operacja zostala wykonana"

    def wyplata(self, moneyremove):
        self.saldo -= moneyremove
        return "Operacja zostala wykonana"

    def __str__(self):
        return "Saldo: " + str(self.saldo)

    def przelew_wynagrodzenia(self, firma, ilosc):
        firma.saldo -= ilosc
        self.saldo += ilosc/100*95
        return "Operacja zostala wykonana"


class PrivateAccount (Account):
    def __init__(self, saldo, wynagrodzenia):
        self.saldo = saldo
        self.wynagrodzenia = wynagrodzenia

    def __str__(self):
        return "wynagrodzenia to: " + str(self.wynagrodzenia)


class FirmAccount(Account):
    def __init__(self, saldo, przelew_do_zus):
        self.saldo = saldo
        self.przelew_do_zus = przelew_do_zus

    def __str__(self):
        return "przelew_do_zus to: " + str(self.przelew_do_zus)


konto1 = Account(1000)
konto2 = Account(500)
konto3 = Account(250)
kontoPriv = PrivateAccount(100, {"mike pence": 1000, "micheel zpalka": 2000})
FirmaAccount = Account(250000)

print(konto1)
print(konto2)
print(konto1.przelew_miedzy_kontami(konto2, 200, 'wlpata'))
print(konto1)
print(konto2)
print(konto2.wplata(2000))
print(konto2)
print(konto3.wyplata(999999999))
print(konto3)
print(konto1.przelew_wynagrodzenia(FirmaAccount, 3000))
print(konto1)
print(kontoPriv)


class Romanian:
    def __init__(self, bilans):
        self.bilans = bilans
        self.slownik = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

    def minus(self, number):
        self.bilans -= number

    def plus(self, number):
        self.bilans += number

    def mnozenie(self, number):
        self.bilans *= number

    def __str__(self):
        self.liczba = []
        if self.bilans == 0:
            return"liczba 0 nie istnieje"
        while self.bilans-1000 >= 0:
            self.liczba.append(self.slownik[1000])
            self.bilans -= 1000
        while self.bilans - 500 >= 0:
            self.liczba.append(self.slownik[500])
            self.bilans -= 500
        while self.bilans-100 >= 0:
            self.liczba.append(self.slownik[100])
            self.bilans -= 100
        while self.bilans-50 >= 0:
            self.liczba.append(self.slownik[50])
            self.bilans -= 50
        while self.bilans-10 >= 0:
            self.liczba.append(self.slownik[10])
            self.bilans -= 20
        while self.bilans-5 >= 0:
            self.liczba.append(self.slownik[5])
            self.bilans -= 5
        while self.bilans-1 >= 0:
            self.liczba.append(self.slownik[1])
            self.bilans -= 1
        return "Twoja liczba rzymska to " + str(self.liczba)


number = 10

liczba = Romanian(100)
print(liczba)
liczba.mnozenie(number)
print(liczba)
liczba.plus(number)
print(liczba)
