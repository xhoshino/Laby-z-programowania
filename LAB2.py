import copy
import random 

# zadanie 1

def licz(x):
    return x**3 - 3 * x**2 + 8 * x - 2

print(licz(int(input("Wpisz liczbe: "))))

# zadanie 2

def funkcja(a, b=0):
    if a==0:
        if b == 0:
            print("nieskonczenie wiele rozwiazan")
        else:
            print("brak rozwiazan")
    else:
        return -b/a
    
print(funkcja(1,2))
print(funkcja(a = 1, b = 2))
print(funkcja(b = 2, a = 1))
print(funkcja(1, b = 2))
a = 1
b = 2
print(funkcja(a,b))

# zadanie 3

def modify(lst):
    lstKopia = copy.copy(lst)
    i=0
    while i < len(lstKopia):
        if lstKopia[i] % 2 == 1:
            lstKopia.insert(i, -1)
            i += 1
        if lstKopia[i] % 4 == 0:
            del lstKopia[i]
            continue
        i += 1
    return lstKopia[::1]

lst = [2, 3, 1, 5, 8, 3, 2, 4, 10, 5]
print(lst, modify(lst))

# zadanie 4

def losowe(n = 10, a = 0, b = 10):
    return [random.randrange(a, b) for _ in range(n)]

# zadanie 5

def wypisz(n):
    lst = losowe(n)
    print(lst)
    print(min(lst))
    print(lst.index(max(lst)))
    print(sum(lst))
    print(sorted(lst))
    print(lst.count(3))
    print(set(lst))
    
wypisz(10)

# zadanie 6

def kombinacje(napis):
     pary = []
     for i, pierwszaLitera in enumerate(napis): 
         for j in range(i + 1, len(napis)):
             drugaLitera = napis[j]
             pary.append(pierwszaLitera + drugaLitera)

     return pary

napis = 'ABCD'
print(kombinacje(napis))

# zadanie 7

l1 = [x**2 for x in range(11)]
l2 = [x**2 for x in range(20) if x**2 % 2 == 1]
l3 = [x**2 if x % 2 == 0 else x**3 for x in range(11)]
        
print(l1, l2, l3)

# zadanie 8

lista = [random.randrange(-10,11) for i in range(20)]
print(lista)
suma = sum([i**2 for i in lista if i < 0])
print(suma)

# zadanie 9

def kwadrat(wartosc):
    if isinstance(wartosc, (int, float)):
        return wartosc **2
    elif isinstance(wartosc, list):
        return [x**2 for x in wartosc]
    else:
        return "moze byc lista lub liczba"
    
liczba = random.randrange(-10,10)
print(f"liczba: {liczba}")
print(kwadrat(liczba))

lista = [random.randrange(-10,10) for _ in range(5)]
print(f"lista: {lista}")
print(kwadrat(lista))

# zadanie 10

def zamiana(asciiLista):
    return ''.join([chr(znak) for znak in asciiLista])

lista = [random.randrange(97,123) for i in range(10)]
print(lista)
print(zamiana(lista))

# zadanie 11

lista1 = [random.randrange(0,10) for _ in range(10)]
lista2 = [random.randrange(0,10) for _ in range(10)]

def listy(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    unikalneLiczby = set1.union(set2)
    wspolneLiczby = set1.intersection(set2)
    tylkow1 = set1.difference(set2)
    
    print(unikalneLiczby)
    print(wspolneLiczby)
    print(tylkow1)

print(f"Lista1: {lista1}, Lista2: {lista2}")
listy(lista1, lista2)

# zadanie 12

slownik = {
    'warrior': 'wojownik',
    'ranger': 'straznik',
    'sorcerer': 'wiedzma',
    'wizard': 'czarodziej'
}

while True:
    slowo = input("Wpisz slowo: ")
    
    if slowo == "stop":
        print("koniec programu")
        break
        
    if slowo in slownik:
        print(slownik[slowo])
    else:
        dodajSlowo = input("Nie ma tego slowa. Dodac je do slownika? [tak/nie]: ")
        
        if dodajSlowo.lower() == "tak":
            tlumaczenie = input("wpisz tlumaczenie tego slowa: ")
            slownik[slowo] = tlumaczenie