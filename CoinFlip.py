#RZUT MONETA
class Coin:
    def __init__(self,orzel,reszka,strona,suma,licznik,licznik_p):
        self.orzel = orzel #1
        self.reszka = reszka #2
        self.strona = strona
        self.suma = suma
        self.licznik = licznik
        self.licznik_p = licznik_p

    def Throw(self):
        import random
        strona = random.randrange(self.orzel, self.reszka + 1)
        if strona == 1:

            print("orzel")
        else:
            print("reszka")
        return self.strona

    def Jedna(self):
        while self.suma < 20:
            import random
            jedna = random.randrange(self.orzel, self.reszka + 1)
            if jedna == 1:
                self.suma += 1
                print("Złotówka")
                print(self.suma)
                if self.suma == 20:
                    ""
            else:
                ""

            dwie = random.randrange(self.orzel, self.reszka + 1)
            if dwie == 1:
                self.suma += 2
                print("DwuZłotówka")
                print(self.suma)
                if self.suma == 20:
                    ""
            else:
                ""

            piec = random.randrange(self.orzel, self.reszka + 1)
            if piec == 1:
                self.suma += 5
                print("PiecioZłotwóka")
                print(self.suma)
                if self.suma == 20:
                    ""
            else:
                ""
        print(f"Cała Suma " + str(self.suma))
        print("-"*58)
        if self.suma == 20:
            print("Wygrales")
            print("-"*58)
            self.licznik +=1
        if self.suma !=20:
            self.licznik_p +=1

        self.suma = 0

    def Koniec(self):
        return print("Wygrales w sumie " + str(self.licznik)+ " razy"), print("Przegrales w sumie " + str(self.licznik_p) + " razy")


if __name__ == "__main__":
    obiekt = Coin(1, 2, 0, 0, 0,0)
    i = 0
    while i <100:
        obiekt.Jedna()
        i +=1
    obiekt.Koniec()



