import math

# zad 3.1


class Samochod:
    
    def __init__(self, marka, model, rok, maxPredkosc):
        self.marka = marka
        self.model = model
        self.rok = rok
        self.maxPredkosc = maxPredkosc
        
    def __del__(self):
        print("zniszczon")
        
    def jedz(self, predkosc, droga):
        przekroczon = predkosc - droga.maxPredkosc
        print(f"Samochód marki {self.marka}, model {self.model} z {self.rok} roku jedzie z predkoscia {predkosc}. Przekraczasz maksymalna predkosc o {przekroczon} na drodze rodzaju {droga.rodzaj}.")
        
    
class Droga:
    
    def __init__(self, rodzaj, maxPredkosc):
        self.rodzaj = rodzaj
        self.maxPredkosc = maxPredkosc
        

mojeAuto = Samochod("Ferrari", "250 GTO", 2019, 200)
mojaDroga = Droga("Autostrada", 140)
mojeAuto.jedz(200, mojaDroga)


# zad 3.2


class kontoBankowe:
    
    def __init__(self, numerKonta, imie, nazwisko, saldo):
        self.numerKonta = numerKonta
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = saldo
    
    def __del__(self):
        print("zniszczon")
        
    def wplata(self, kwota):
        self.saldo += kwota
        print(f"Wpłata na konto o numerze {self.numerKonta} została wykonana. Aktualne saldo: {self.saldo}.")
    
    def wyplata(self, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
            print(f"Wyplata z konta o numerze {self.numerKonta} została wykonana. Aktualne saldo: {self.saldo}.")
        else:
            print("Nie masz tyle kasy")
            
mojeKonto = kontoBankowe("2121", "Natalia", "Gołębiowska", 10)
mojeKonto.wplata(200)
mojeKonto.wyplata(200)


# zad 3.3


class energiaOdnawialna:
    
    def __init__(self, nazwa, moc, lokacja):
        self.nazwa = nazwa
        self.moc = moc
        self.lokacja = lokacja
    
    def get_info(self):
        print(f"Nazwa: {self.nazwa}, Moc: {self.moc} MW, Lokalizacja: {self.lokacja}.")
        
    def __eq__(self, elektrownia):
        return self.nazwa == elektrownia.nazwa and self.moc == elektrownia.moc and self.lokacja == elektrownia.lokacja
        
        
elektrowniaWiatrowa = energiaOdnawialna("wiatr", 50, "Szczecin")
elektrowniaSloneczna = energiaOdnawialna("Slonce", 50, "Szczecin")
elektrowniaWiatrowaa = energiaOdnawialna("wiatr", 50, "Szczecin")

elektrowniaSloneczna.get_info()
print(elektrowniaWiatrowa == elektrowniaWiatrowaa)
print(elektrowniaWiatrowa == elektrowniaSloneczna)


# zad 3.4


class Ulamek:
    
    def __init__(self, licznik, mianownik):
        if mianownik == 0:
            raise ZeroDivisionError("mianownik nie moze byc zerem")
        self.licznik = licznik
        self.mianownik = mianownik
        
    def __str__(self):
        nwd = math.gcd(self.licznik, self.mianownik)
        uproszczonyLicznik = self.licznik // nwd
        uproszczonyMianownik = self.mianownik // nwd
        czescCalkowita = uproszczonyLicznik // uproszczonyMianownik
        pozostalyLicznik = uproszczonyLicznik % uproszczonyMianownik
        
        if pozostalyLicznik == 0:
            return str(czescCalkowita)
        else:
            if czescCalkowita == 0:
                return f"{pozostalyLicznik}/{uproszczonyMianownik}"
        return f"{czescCalkowita} {pozostalyLicznik}/{uproszczonyMianownik}"
    
    def __repr__(self):
        return f"ulamek({self.licznik}, {self.mianownik})"
        
    def __add__(self, ulamek):
        nowyLicznik = self.licznik * ulamek.mianownik + ulamek.licznik * self.mianownik
        nowyMianownik = self.mianownik * ulamek.mianownik
        return Ulamek(nowyLicznik, nowyMianownik)
    
    def __sub__(self, ulamek):
        nowyLicznik = self.licznik * ulamek.mianownik - ulamek.licznik * self.mianownik
        nowyMianownik = self.mianownik * ulamek.mianownik
        return Ulamek(nowyLicznik, nowyMianownik)
        
    def __mul__(self, ulamek):
        nowyLicznik = self.licznik * ulamek.licznik
        nowyMianownik = self.mianownik * ulamek.mianownik
        return Ulamek(nowyLicznik, nowyMianownik)
    
    def __truediv__(self, ulamek):
        nowyLicznik = self.licznik * ulamek.mianownik
        nowyMianownik = self.mianownik * ulamek.licznik
        return Ulamek(nowyLicznik, nowyMianownik)
    
    def __abs__(self):
        return Ulamek(abs(self.licznik), abs(self.mianownik))
        
    def __lt__(self, ulamek):
        return (self.licznik * ulamek.mianownik) < (ulamek.licznik * self.mianownik)

    def __gt__(self, ulamek):
        return (self.licznik * ulamek.mianownik) > (ulamek.licznik * self.mianownik)

    def __le__(self, ulamek):
        return (self.licznik * ulamek.mianownik) <= (ulamek.licznik * self.mianownik)

    def __ge__(self, ulamek):
        return (self.licznik * ulamek.mianownik) >= (ulamek.licznik * self.mianownik)

    def __eq__(self, ulamek):
        return (self.licznik * ulamek.mianownik) == (ulamek.licznik * self.mianownik)

    def __ne__(self, ulamek):
        return (self.licznik * ulamek.mianownik) != (ulamek.licznik * self.mianownik)
    
    def __float__(self):
        return self.licznik / self.mianownik

    def __int__(self):
        return int(float(self))

    def __bool__(self):
        return bool(float(self))

    def __round__(self, n=None):
        if n is None:
            return Ulamek(round(float(self)), 1)
        else:
            zaokraglona = round(float(self), n)
            mianownik = 10 ** n
            licznik = round(zaokraglona * mianownik)
            return Ulamek(licznik, mianownik)
        

print("\ntworzenie ulamkow:")
u1 = Ulamek(3, 4)
u2 = Ulamek(7, 2)
u3 = Ulamek(-3, 4)
print(f"ulamek wlasciwy: {u1}")
print(f"ulamek niewlasciwy: {u2}")
print(f"ulamek ujemny: {u3}")

print("\ndzialania arytmetyczne:")
print(f"dodawanie: {u1} + {u2} = {u1 + u2}")
print(f"odejmowanie: {u2} - {u1} = {u2 - u1}")
print(f"mnozenie: {u1} * {u2} = {u1 * u2}")
print(f"dzielenie: {u2} / {u1} = {u2 / u1}")

print("\nporownania:")
print(f"{u1} < {u2}: {u1 < u2}")
print(f"{u1} > {u2}: {u1 > u2}")
print(f"{u1} <= {u2}: {u1 <= u2}")
print(f"{u1} >= {u2}: {u1 >= u2}")
print(f"{u1} == {u2}: {u1 == u2}")
print(f"{u1} != {u2}: {u1 != u2}")

print("\nwartosc bezwzgledna:")
print(f"|{u3}| = {abs(u3)}")

print("\nkonwersja typow:")
print(f"{u2} jako float: {float(u2)}")
print(f"{u2} jako int: {int(u2)}")
print(f"{u2} jako bool: {bool(u2)}")
print(f"Ulamek(0,1) jako bool: {bool(Ulamek(0,1))}")

print("\nzaokraglanie:")
u4 = Ulamek(22, 7)
print(f"ulamek {u4} zaokraglony do 2 miejsc po przecinku: {u4.__round__(2)}") # to dziala, tylko przeladowanie printa skraca ten ulamek 👎
print(f"ulamek {u4} zaokraglony do liczby calkowitej: {u4.__round__()}")

print("\ndzielenie przez zero:")
try:
    error = Ulamek(1, 0)
except ZeroDivisionError as e:
    print(f"blad: {e}")