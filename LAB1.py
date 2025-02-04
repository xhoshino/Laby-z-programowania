import math as m
import random



# zadanie 1
listunia = [10, 40.5, "meow"]
print(listunia)



# zadanie 2 
a = int(input("pierwsza liczba: "))
b = int(input("druga liczba: "))
iloczyn = a * b

if a == 0 or b == 0:
    print("iloczyn: ", iloczyn)
    print("Nie dziel przez zero")
else:
    iloraz = a / b
    print("iloczyn: ", iloczyn)
    print("iloraz: ", iloraz)



# zadanie 3
a = int(input("liczbe: "))

if a % 2 == 0:
    print(a / 2)
else:
    print(a ** 3)

# zadanie 4
imie = input("imie: ")
print(f"Hello, ", imie)



# zadanie 5
promien = float(input("promien podstawy walca: "))
wysokosc = float(input("wysokosc walca: "))

objetosc = wysokosc * m.pi * promien ** 2
print(objetosc)

# zadanie 6
for i in range(0, 5):
    print(i)

for i in range(5,11):
    print(i)

for i in range(0,10,3):
    print(i)

for i in range(0,-10,-2):
    print(i)



# zadanie 7
slowa = []
while True:
    word = input("slowa/powiedz koniec: ")
    if word == "koniec":
        break
    else:
        slowa.append(word)

print("lista slow:", " ".join(slowa))

 
 
# zadanie 8 
lista = [2, 4, 10, 1, 23, 53, 3, 7]

# Zalozenie, ze m i ind przechowuja najwyzsza wartosc
m = lista[0]
ind = 0

for i in range(1, len(lista)):
    # sprawdzanie, czy aktualny element z listy jest wiekszy od obecnej najwiekszej wartosci
    if lista[i] > m:
        m = lista[i]
        ind = i

print("Najwieksza wartosc: ", m)
print("Indeks: ", ind)



# zadanie 9 
a = float(input("pierwszy bok: "))
b = float(input("drugi bok: "))
c = float(input("trzeci bok: "))

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("mozna zrobic trojkat")
else:
    print("nie mozna zrobic trojkata")



# zadanie 10
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
x3 = float(input("x3: "))
y3 = float(input("y3: "))

# Granice prostokata

x_min = min(x1, x2)
x_max = max(x1, x2)
y_min = min(y1, y2)
y_max = max(y1, y2)

# Czy punkt znajduje sie w srodku prostokata
if x_min <= x3 <= x_max and y_min <= y3 <= y_max:
    print("punkt znajduje sie w srodku prostokata")
else:
    print("punkt nie znajduje sie w srodku prostokata")



# zadanie 11
liczba = int(input("liczbe: "))
suma = 0

while liczba > 0:
    suma += liczba % 10
    liczba //= 10

print("Suma wynosi", suma)



# zadanie 12
napis = input("Napisz cos: ")
# dlugosc napisu
print(len(napis))

# czwarty znak
print(napis[3])

# przedostatni znak
przedostatniZnak = slice(len(napis) - 2, len(napis) - 1)
print(napis[przedostatniZnak])

# pierwsze 10 znakow
pierwszaDziesiatka = slice(10)
print(napis[pierwszaDziesiatka])

# wszystkie znaki napisu oprocz ostatnich 5
wszystkieOprocz = slice(0, len(napis) - 5)
print(napis[wszystkieOprocz])

# wszystkie znaki od 5 do 5 od konca znaku (wlacznie)
wszystkieOd5do5 = slice(5, len(napis) - 5)
print(napis[wszystkieOd5do5])

# znaki o indeksach parzystych w odwrotnej kolejnosci
print(napis[-1:0:-2])



# zadanie 13
napis = input("Napisz cos: ")
napisBezSpacji = "".join(napis.split()).lower()
palindrom = True
dlugoscNapisu = len(napisBezSpacji)

for i in range(dlugoscNapisu // 2):
    if napisBezSpacji[i] != napisBezSpacji[dlugoscNapisu - i - 1]:
        palindrom = False
        break

if palindrom:
    print("Jest palindromem")
else:
    print("Nie jest palindromem")



# zadanie 14
napis = input("napisz cos: ")
slowa = napis.split()
zmienioneSlowa = []

for i in range(0, len(slowa)):
    if i % 2 == 1:
        zmienioneSlowo = slowa[i].replace("a", "A")
    else:
        zmienioneSlowo = slowa[i].capitalize()
    zmienioneSlowa.append(zmienioneSlowo)

nowyTekst = " ".join(zmienioneSlowa)

print("zmieniony tekst:", nowyTekst)



# zadanie 15
wyrazy = int(input("Wpisz liczbe: "))
fibon = [0,1]

for i in range(2, wyrazy):
    kolejnyWyraz = fibon[-1] + fibon[-2]
    fibon.append(kolejnyWyraz)

print("ciag: ", fibon)



# zadanie 16
listaJeden = [1, 4, 3, 5, 2]
listaDwa = [4, 2, 1, 5, 3]

listaZip = zip(listaDwa, listaJeden)

for para in listaZip:
    if para[0] == para[1]:
        print(para[0], "*", para[1], "=", para[0] * para[1])
    else:
        print(para[0], "+", para[1], "=", para[0] + para[1])



# zadanie 17
wyrazy = ["orange", "apple", "cherry", "banana"]

for indeks, wyraz in enumerate(wyrazy):
    if wyraz.count('a') == indeks:
        print(f"{indeks} {wyraz} <--")
    else:
        print(f"{indeks} {wyraz}")
        


# zadanie 18
losowa = random.randrange(1000)

while True:
    try:
        odp = int(input("odpowiedz: "))
        
        if odp > losowa:
            print("za duza liczba")
        elif odp < losowa:
            print("za mala liczba")
        else:
            print("Udalo sie")
            break
    except ValueError:
        print("podaj liczbe calkowita")



# zadanie 19
lista = [random.randint(0, 9) for _ in range(10)]
print("lista: ", lista)
wystapienia = {}

for liczba in lista:
    if liczba in wystapienia:
        wystapienia[liczba] +=1
    else:
        wystapienia[liczba] = 1
        
print("wynik: ", wystapienia)



# zadanie 20
while True:
    napis = input("> ").strip()
    
    if not napis:
        print("koniec")
        break

    czastki = napis.split(maxsplit=1)

    if len(czastki) < 2:
        print("napisz polecenie (lower, upper, title lub reverse) i jakies slowa")
        continue
    
    polecenie, slowa = czastki[0], czastki[1]
    
    if polecenie == "lower":
        print(slowa.lower())
    elif polecenie == "upper":
        print(slowa.upper())
    elif polecenie == "title":
        print(slowa.title())
    elif polecenie == "reverse":
        print(slowa[::1])
    else:
        print(f"nieznane polecenie {polecenie}, wybierz inne")