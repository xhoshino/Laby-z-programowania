import random
from collections import Counter
import itertools
import math

# zadanie 1


losoweLiczby = [random.randint(0, 10) for _ in range(50)]
najczestsze = Counter(losoweLiczby).most_common(5)

print("Lista losowych liczb:", losoweLiczby, "\n5 najczęstszych liczb i ile razy wystąpiły:", najczestsze)


# zadanie 2


napis = input("napisz coś: ")

permutacje = []
for p in itertools.permutations(napis, 2):
    permutacje.append(''.join(p))
    
print("permutacje dwusymbolowe: ", ' '.join(permutacje))

kombinacje = []
for k in itertools.combinations(napis, 2):
    kombinacje.append(''.join(k))
    
print("kombinacje dwusymbolowe: ", ' '.join(kombinacje))


# zadanie 3


def wyznacznik(macierz):
    if len(macierz) != 2:
        raise ValueError("Macierz musi mieć dokładnie dwa wiersze")

    for wiersz in macierz:
        if len(wiersz) != 2:
            raise ValueError("Macierz musi miec dokładnie dwie kolumny")
    
    a, b = macierz[0]
    c, d = macierz[1]
    wyznacznik = a*d - b*c
    
    return wyznacznik

macierz = [
    [1, 2],
    [3, 4],
]

macierz2 = [
    [1, 2, 3],
    [0, 4, 5],
]

try:
    print("Wyznacznik 1 macierzy: ", wyznacznik(macierz))
    print("Wyznacznik 2 macierzy: ", wyznacznik(macierz2))
except ValueError as error:
    print("Błąd: ", error)
    
    
# zadanie 4


with open('points.txt', 'r') as plik: # otwarcie pliku w trybie odczytu
    linie = plik.readlines() 
    
punkty = []
for linia in linie:
    xstr, ystr = linia.strip().split()      # usuwanie bialych znakow i dzielenie linii na dwie czesci
    x = float(xstr)
    y = float(ystr)
    punkty.append((x, y))       # dodawanie punktow jako krotka do listy
    
iks = float(input("Podaj współrzędną x: "))
igrek = float(input("Podaj współrzędną y: "))
wspolrzednePodane = (iks, igrek)       # podane przez użytkownika

odleglosci = []
for punkt in punkty:
    odleglosc = math.dist(wspolrzednePodane, punkt)     # dlugosc punkty z listy do punktu uzytkownika
    odleglosci.append((odleglosc, punkt))    # dlugosc punkty z listy do punktu uzytkownika
    
odleglosci.sort()   # sortowanie po odleglosci

najblizszePunkty = odleglosci[:10]

print('\n10 najblizszych punktow:')
for odleglosc, punkt in najblizszePunkty:
    print(f"Punkt: ({punkt[0], punkt[1]}) z odległością {odleglosc}")
    
    
# zadanie 5


def rownaniaKwadratowe(a, b, c):
    delta = b**2 - 4 * a * c
    pierwiastekDelty = math.sqrt(delta)
    x1 = (-b + pierwiastekDelty) / (2*a)    # pierwszy pierwiastek
    x2 = (-b - pierwiastekDelty) / (2*a)    # a tu drugi pierwiastek
    return x1, x2

with open("equations.txt", "r") as plik:    # otwarcie pliku
    rownania = plik.read().splitlines()
    
wyniki = []

for wiersz in rownania[:50]:
    wspolczynniki = wiersz.strip().split()
    if len(wspolczynniki) != 3:     # sprawdzonko czy na pewno sa 3 wspolczynniki
        wyniki.append('')           # jak nie ma, to dodajemy pusty wiersz
        continue
    try:
        a, b, c = map(float, wspolczynniki)
        x1, x2 = rownaniaKwadratowe(a, b, c)
        wyniki.append(f"{x1} {x2}")
    except ValueError as error:
        wyniki.append('')
    except Exception as error:
        wyniki.append('')

    
with open("equations_results.txt", "w") as wynikowy:    # otwarcie pliku z zapisanymi wynikami tak, by mozna bylo w nim pisac
    for wiersz in wyniki:
        wynikowy.write(wiersz + '\n')


# zadanie 6


def czyPierwsza(n):
    if n <= 1:
        return False # liczba 1 i wszystkie liczby ujemne nie są pierwsze
    if n == 2:
        return True # 2 jest liczbą pierwszą
    if n % 2 == 0:
        return False # eliminowanie parzystych większych od 2
    najwiekszyDzielnik = int(math.sqrt(n))
    for i in range(3, najwiekszyDzielnik + 1, 2):   # zaczyna od 3 i iteruje co 2, by sprawdzala same nieparzyste
        if n % i == 0:
            return False
    return True
    
    
fibon = []
a, b = 0, 1
while len(fibon) < 30:
    fibon.append(b)
    a, b = b, a+b
    
pierwsze = []
for i in fibon:
    if czyPierwsza(i):
        pierwsze.append(i)
        
print("Liczby pierwsze, ktore sa w ciagu Fibona: ", pierwsze)


# zadanie 7

def kolac(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Musi to być całkowita albo większa lub równa 1")
    
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield 1
        
n = 5
print(f"Ciąg Collatza dla n = {n}:")
for liczba in kolac(n):
    print(liczba)


# zadanie  8


with open("cars.csv", "r", encoding="utf-8") as plik:
    autka = [tuple(wiersz.strip().split(",")) for wiersz in plik]

odNajdrozszego = sorted(autka, key=lambda x: float(x[3]), reverse=True)
odNajstarszego = sorted(autka, key=lambda x: float(x[2]))
najtanszaFura = min(autka, key=lambda x: float(x[3]))

print("Posortowane od najdrozszego:", odNajdrozszego, '\n')
print("Posortowane od najstarszego:", odNajstarszego, '\n')
print("Najtansza fura:", najtanszaFura)