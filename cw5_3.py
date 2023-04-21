class Romanian:
    def __init__(self, bilans):
        self.bilans = bilans
        self.slownik = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

    def minus(self, number):
        pass

    def plus(self, number):
        pass

    def mnozenie(self, number):
        pass

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
            self.liczba.append(self.slownik[1000])
            self.bilans -= 5
        while self.bilans-1 >= 0:
            self.liczba.append(self.slownik[1000])
            self.bilans -= 1
        return "Twoja liczba rzymska to " + str(self.liczba)


liczba1 = Romanian(100)
print(liczba1)
