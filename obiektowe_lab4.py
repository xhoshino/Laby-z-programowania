# zad 1

class Ssak:
    rodzaj = "Ssak"
    
    def __init__(self, info="Brak ciekawostki"):
        self.info = info
        print(f"Stworzyłaś: {self.rodzaj}")
        
    def ciekawostka(self):
        print(self.info)
    
class Kot(Ssak):
    rodzaj = "Kot"
    
    def __init__(self, info="Lubi wcinać paprotki"):
        super().__init__(info)
    
class Pies(Ssak):
    rodzaj = "Pies"
    
    def __init__(self, info="Szczeka jak ma się kaptur na głowie (dziwne cziłały)"):
        super().__init__(info)
        
s = Ssak()
s.ciekawostka()
k = Kot()
k.ciekawostka()
p = Pies()
p.ciekawostka()
print("-" * 40)

# zad 2

class Zegar:
    def __init__(self):
        self.godzina = 0
        self.minuta = 0
        self.sekunda = 0
    
    def ustaw_czas(self, godzina, minuta, sekunda):
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda
    
    def __str__(self):
        return f"{self.godzina:02}:{self.minuta:02}:{self.sekunda:02}"
    
class ZegarElektroniczny(Zegar):
    def __init__(self):
        super().__init__()
        self.dni_tygodnia = 0
        self.dzien_miesiaca = 0
        self.miesiac = 0
        self.rok = 0
    
    def ustaw_czas(self, godzina, minuta, sekunda, dni_tygodnia, dzien_miesiaca, miesiac, rok):
        super().ustaw_czas(godzina, minuta, sekunda)
        self.dni_tygodnia = dni_tygodnia
        self.dzien_miesiaca = dzien_miesiaca
        self.miesiac = miesiac
        self.rok = rok
    
    def __str__(self):
        return f"{super().__str__()}, {self.dzien_miesiaca:02}-{self.miesiac:02}-{self.rok}"
    
class ZegarCzwartyWymiar(ZegarElektroniczny):
    def __init__(self):
        super().__init__()
        self.czas_kwantowy = 0.0
        
    def ustaw_czas(self, godzina, minuta, sekunda, dni_tygodnia, dzien_miesiaca, miesiac, rok, czas_kwantowy):
        self.czas_kwantowy = czas_kwantowy
        super().ustaw_czas(godzina, minuta, sekunda, dni_tygodnia, dzien_miesiaca, miesiac, rok)
        
    def __str__(self):
        return f"{super().__str__()}, {self.czas_kwantowy}"
    
zegar = Zegar()
zegar.ustaw_czas(12, 30, 0)
print("Zegar:", zegar)

zegar_elektroniczny = ZegarElektroniczny()
zegar_elektroniczny.ustaw_czas(12, 30, 0, 2, 22, 3, 2023)
print("ZegarElektroniczny:", zegar_elektroniczny)

zegar_czwarty_wymiar = ZegarCzwartyWymiar()
zegar_czwarty_wymiar.ustaw_czas(12, 30, 0, 2, 22, 3, 2023, 0.5)
print("ZegarCzwartyWymiar:", zegar_czwarty_wymiar)
print("-" * 40)

# zad 3

class Ksiazka:
    def __init__(self, tytul, autor, cena):
        self.tytul = tytul
        self.autor = autor
        self.cena = cena

    def __str__(self):
        return f"{self.tytul}, autor: {self.autor}, cena: {self.cena}"

    def __repr__(self):
        return f"Ksiazka({self.tytul}, {self.autor}, {self.cena})"


class KsiazkaFantasy(Ksiazka):
    def __init__(self, tytul, autor, cena, podgatunek_fantasy):
        super().__init__(tytul, autor, cena)
        self.podgatunek_fantasy = podgatunek_fantasy

    def __str__(self):
        return f"{super().__str__()}, podgatunek fantasy: {self.podgatunek_fantasy}"

    def __repr__(self):
        return f"KsiazkaFantasy({self.tytul}, {self.autor}, {self.cena}, {self.podgatunek_fantasy})"


class KsiazkaKryminalna(Ksiazka):
    def __init__(self, tytul, autor, cena, liczba_zabojstw):
        super().__init__(tytul, autor, cena)
        self.liczba_zabojstw = liczba_zabojstw

    def __str__(self):
        return f"{super().__str__()}, liczba zabójstw: {self.liczba_zabojstw}"

    def __repr__(self):
        return f"KsiazkaKryminalna({self.tytul}, {self.autor}, {self.cena}, {self.liczba_zabojstw})"


class KsiazkaFantastycznoKryminalna(KsiazkaFantasy, KsiazkaKryminalna):
    def __init__(self, tytul, autor, cena, podgatunek_fantasy, liczba_zabojstw):
        Ksiazka.__init__(self, tytul, autor, cena)
        self.podgatunek_fantasy = podgatunek_fantasy
        self.liczba_zabojstw = liczba_zabojstw

    def __str__(self):
        return (f"{super(KsiazkaFantasy, self).__str__()}, podgatunek fantasy: {self.podgatunek_fantasy}, "
                f"liczba zabójstw: {self.liczba_zabojstw}")

    def __repr__(self):
        return (f"KsiazkaFantastycznoKryminalna({self.tytul}, {self.autor}, {self.cena}, "
                f"{self.podgatunek_fantasy}, {self.liczba_zabojstw})")

class Biblioteka:
    def __init__(self):
        self.ksiazki = []
        self.wypozyczone = {}

    def dodaj_ksiazke(self, ksiazka):
        self.ksiazki.append(ksiazka)

    def wyswietl_ksiazki(self):
        dostepne = [k for k in self.ksiazki if k not in self.wypozyczone]
        if not dostepne:
            print("brakuje książek w bibliotece")
        else:
            for k in dostepne:
                print(k)

    def wypozycz_ksiazke(self, ksiazka, osoba):
        if ksiazka in self.wypozyczone:
            print(f"Książka {ksiazka.tytul} jest już wypożyczona przez {self.wypozyczone[ksiazka]}.")
        elif ksiazka not in self.ksiazki:
            print(f"Książka {ksiazka.tytul} nie jest dostępna w bibliotece")
        else:
            self.wypozyczone[ksiazka] = osoba
            print(f"Wypożyczono książkę {ksiazka.tytul} osobie {osoba}")

    def zwroc_ksiazke(self, ksiazka):
        if ksiazka in self.wypozyczone:
            del self.wypozyczone[ksiazka]
            print(f"książka {ksiazka.tytul} została zwrócona")
        else:
            print(f"Książka {ksiazka.tytul} nie była wypożyczona")

    def wyswietl_wypozyczone(self):
        if not self.wypozyczone:
            print("Brak wypożyczonych książek.")
        else:
            print("Wypożyczone książki:")
            for ksiazka, osoba in self.wypozyczone.items():
                print(f"{ksiazka.tytul}, wypożyczona przez: {osoba}")
                

ksiazka1 = Ksiazka("Dune", "Frank Herbert", 39.99)
ksiazka2 = KsiazkaFantasy("Władca Pierścieni", "J.R.R. Tolkien", 49.99, "high fantasy")
ksiazka3 = KsiazkaKryminalna("Zbrodnia i kara", "Fiodor Dostojewski", 29.99, 10)
ksiazka4 = KsiazkaFantastycznoKryminalna("Miasto Cienia", "Cassandra Clare", 59.99, "urban fantasy", 5)

biblioteka = Biblioteka()
biblioteka.dodaj_ksiazke(ksiazka1)
biblioteka.dodaj_ksiazke(ksiazka2)
biblioteka.dodaj_ksiazke(ksiazka3)
biblioteka.dodaj_ksiazke(ksiazka4)
biblioteka.wyswietl_ksiazki()

biblioteka.wypozycz_ksiazke(ksiazka2, "Jan Kowalski")
biblioteka.wypozycz_ksiazke(ksiazka4, "Adam Nowak")
biblioteka.wyswietl_wypozyczone()

biblioteka.zwroc_ksiazke(ksiazka2)
biblioteka.zwroc_ksiazke(ksiazka4)
biblioteka.wyswietl_ksiazki()
print("-" * 40)

# zad 4

class Furniture:
    def __init__(self, material, size):
        self.__material = material
        self.size = size

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, value):
        self.__material = value

class Table(Furniture):
    def __init__(self, material, size, legs):
        super().__init__(material, size)
        self.__legs = legs

    @property
    def legs(self):
        return self.__legs

    @legs.setter
    def legs(self, value):
        self.__legs = value

class Chair(Furniture):
    def __init__(self, material, size, has_armrests):
        super().__init__(material, size)
        self.__has_armrests = has_armrests

    @property
    def has_armrests(self):
        return self.__has_armrests

    @has_armrests.setter
    def has_armrests(self, value):
        self.__has_armrests = value

table = Table('wood', 'large', 4)
chair = Chair('metal', 'medium', True)

print('Table material:', table.material)
table.material = 'plastic'
print('Table material after modification:', table.material)
print('Table size:', table.size)
print('Table legs:', table.legs)
table.legs = 6
print('Table legs after modification:', table.legs)
print('Chair material:', chair.material)
print('Chair size:', chair.size)
print('Chair has armrests:', chair.has_armrests)
chair.has_armrests = False
print('Chair has armrests after modification:', chair.has_armrests)