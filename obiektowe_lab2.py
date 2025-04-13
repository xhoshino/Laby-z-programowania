import matplotlib.pyplot as plt
import datetime

# zad 3.1

'''class punkt:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def nalezyDo(self, prosta):
        return self.y == prosta.a * self.x + prosta.b
        
    
    def __str__(self):
        return f"Punkt({self.x}, {self.y})"
        
class prosta:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def miejsceZerowe(self):
        if self.a != 0:
            miejsceX = -self.b / self.a
            return miejsceX
        else:
            if self.b == 0:
                print(f"Prosta {self} pokrywa się z osią X, czyli ma nieskończenie wiele miejsc zerowych")
                return None
            else:
                print(f"Prosta {self} jest pozioma (y={self.b}) i nie przecina osi X")
                
    
    def __str__(self):
        return f"Prosta(a={self.a}, b={self.b})"
    

p = punkt(3, 6)
pr = prosta(2,0)

print(f"Punkt {p}")
print(f"Prosta {pr}")
print(f"Czy nalezy do prostej: {p.nalezyDo(pr)}")
print(f"Miejsce zerowe proste {pr}: {pr.miejsceZerowe()}")

# zad 3.2

class punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Punkt ({self.x},{self.y})"
    
class prostokat:
    def __init__(self, p1: punkt, p2: punkt):
        if not isinstance(p1, punkt) or not isinstance(p2, punkt):
            raise TypeError("argumenty muszą być obiektami punkt")
        
        self.p1 = p1
        self.p2 = p2
        self.bokA = abs(self.p1.x - self.p2.x)
        self.bokB = abs(self.p1.y - self.p2.y)
        
    def pole(self):
        return self.bokA * self.bokB
    
    def obwod(self):
        return 2 * (self.bokA + self.bokB)
    
    
    def rysuj(self):
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        wierzcholkiX = [x1, x1, x2, x2, x1]
        wierzcholkiY = [y1, y2, y2, y1, y1]
        
        fig, ax = plt.subplots()
        ax.plot(wierzcholkiX, wierzcholkiY, 'b-')
        ax.plot([self.p1.x, self.p2.x], [self.p1.y, self.p2.y], 'ro')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(True)
        plt.show()
        
    def __repr__(self):
        return f"Prostokat({self.p1},{self.p2})"
        
        
p1 = punkt(1,1)
p2 = punkt(2,3)
prost = prostokat(p1, p2)

print(f"prostokat: {prost}")
print(f"pole: {prost.pole()}")
print(f"obwod: {prost.obwod()}")
prost.rysuj()

# zad 3.3

class Note:
    def __init__(self, author: str, content: str):
        self.author = author
        self.content = content
        self.creation_time = datetime.datetime.now()

    def __str__(self) -> str:
        hour = self.creation_time.hour
        minute = self.creation_time.minute
        formattedTime = f"{hour:02d}:{minute:02d}"

        return f'{self.author}: "{self.content}" o godzinie {formattedTime}'

    def __repr__(self):
        return f'Note(author="{self.author}", content="{self.content}")'

class Notebook:
    def __init__(self):
        self.notes = []

    def dodaj_nowa(self, author: str, content: str):
        nowa = Note(author, content)
        self.notes.append(nowa)

    def dodaj(self, note: Note):
        if isinstance(note, Note):
            self.notes.append(note)
            print(f"Dodano istniejaca notatke od {note.author}")
        else:
            raise TypeError("Mozna dodawac tylko obiekty klasy Note")

    def ile_notatek(self) -> int:
        return len(self.notes)

    def wyswietl_wszystko(self):
        if not self.notes:
            print("Nie ma notek")
            return
        print("Masz takie notatki: ")
        for i, note in enumerate(self.notes, start=1):
            print(f"{i}. {note}")


print("Tworzenie nowego notatnika...")
nb = Notebook()

print("\nSprawdzenie, czy notatnik jest pusty:")
nb.wyswietl_wszystko()
print(f"Liczba notatek: {nb.ile_notatek()}")


print("\nDodawanie notatek:")
nb.dodaj_nowa("notka", "pierwsza notatka")
n2 = Note("notka 2", "druga notatka")
nb.dodaj(n2)
nb.wyswietl_wszystko()
print(f"Liczba notatek: {nb.ile_notatek()}")
'''
# zad 3.4

class Pracownik:
    def __init__(self, imie, nazwisko, stanowisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self._id_pracownika = id(self)
        self.__pensja = 0.0

    def przedstaw_sie(self):
        print(f"Cześć, nazywam się {self.imie} {self.nazwisko} i pracuję na stanowisku {self.stanowisko}")

    def __zmien_pensje(self, nowa_pensja):
        if nowa_pensja < 0:
            raise ValueError("Pensja nie może być ujemna")
        self.__pensja = nowa_pensja
        
    def wplata(self, wartosc):
        if wartosc < 0:
            raise ValueError("Wartość wpłaty nie może być ujemna")
        nowa_calkowita_pensja = self.__pensja + wartosc
        
        try:
            self.__zmien_pensje(nowa_calkowita_pensja)
            print(f"Dokonano wpłaty {wartosc}. Pensja: {self.__pensja}")
        except ValueError as e:
            print(f"błąd: {e}")
            
    def get_pensja(self):
        return self.__pensja
    
pracownik1 = Pracownik("Feliks", "Kot", "Łapacz much")

pracownik1.przedstaw_sie()
print(f"ID pracownika: {pracownik1._id_pracownika}")

print(f"\nPensja Feliksa przed wpłatą: {pracownik1.get_pensja()}")
try:
    pracownik1.wplata(2500)
    print(f"Pensja Feliksa po wpłacie: {pracownik1.get_pensja()}")
    pracownik1.wplata(500.75)
    print(f"Pensja Feliksa po drugiej wpłacie: {pracownik1.get_pensja()}")
    print("ujemna wpłata:")
    pracownik1.wplata(-100)
except ValueError as e:
    print(f"błąd: {e}")
    print(f"Pensja Feliksa bez zmian: {pracownik1.get_pensja()}")