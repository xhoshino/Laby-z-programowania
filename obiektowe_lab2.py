import matplotlib.pyplot as plt
import datetime

# zad 3.1

class Punkt:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def nalezy_do(self, prosta):
        return self.y == prosta.a * self.x + prosta.b
        
    def __str__(self):
        return f"Punkt({self.x}, {self.y})"

    def __repr__(self):
        return f"Punkt({self.x},{self.y})"
        
class Prosta:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def miejsce_zerowe(self):
        if self.a != 0:
            miejsce_x = -self.b / self.a
            return miejsce_x
        else:
            if self.b == 0:
                print(f"Prosta {self} pokrywa się z osią X, czyli ma nieskończenie wiele miejsc zerowych")
                return None
            else:
                print(f"Prosta {self} jest pozioma (y={self.b}) i nie przecina osi X")
                return None
                
    
    def __str__(self):
        return f"Prosta(a={self.a}, b={self.b})"
    
print("zadanko 3.1")
p_zad1 = Punkt(3, 6)
pr_zad1 = Prosta(2,0)

print(f"punkt: {p_zad1}")
print(f"prosta: {pr_zad1}")
print(f"Czy punkt należy do prostej: {p_zad1.nalezy_do(pr_zad1)}")
print(f"Miejsce zerowe prostej: {pr_zad1.miejsce_zerowe()}")
print("-" * 40)

# zad 3.2

    
class Prostokat:
    def __init__(self, p1: Punkt, p2: Punkt):
        if not isinstance(p1, Punkt) or not isinstance(p2, Punkt):
            raise TypeError("argumenty muszą być obiektami punkt")
        
        self.p1 = p1
        self.p2 = p2
        self.bok_a = abs(self.p1.x - self.p2.x)
        self.bok_b = abs(self.p1.y - self.p2.y)
        
    def pole(self):
        return self.bok_a * self.bok_b
    
    def obwod(self):
        return 2 * (self.bok_a + self.bok_b)
    
    
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
        return f"Prostokat(p1={self.p1}, p2={self.p2})"
        

print("zadanko 3.2")
p1_zad2 = Punkt(1, 1)
p2_zad2 = Punkt(2, 3)
prost_zad2 = Prostokat(p1_zad2, p2_zad2)

print(f"Prostokąt: {prost_zad2}")
print(f"Pole: {prost_zad2.pole()}")
print(f"Obwód: {prost_zad2.obwod()}")
prost_zad2.rysuj()
print("-" * 40)

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


print("zadanko 3.3")
nb = Notebook()
nb.wyswietl_wszystko()
print(f"Liczba notatek: {nb.ile_notatek()}")

nb.dodaj_nowa("Natalia", "pierwsza notatka")
n2 = Note("Feliks", "druga notatka")
nb.dodaj(n2)
nb.wyswietl_wszystko()
print(f"Liczba notatek: {nb.ile_notatek()}")
print("-" * 40)

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
    
    
print("zadanko 3.4")
pracownik1 = Pracownik("Feliks", "Kot", "Łapacz much")

pracownik1.przedstaw_sie()
print(f"ID pracownika: {pracownik1._id_pracownika}")

print(f"\nPensja Feliksa przed wpłatą: {pracownik1.get_pensja()}")
try:
    pracownik1.wplata(2500)
    print(f"Pensja Feliksa po wpłacie: {pracownik1.get_pensja()}")
    pracownik1.wplata(500.75)
    print(f"pensja Feliksa po drugiej wpłacie: {pracownik1.get_pensja()}")
    print("ujemna wpłata:")
    pracownik1.wplata(-100)
except ValueError as e:
    print(f"błąd: {e}")
    print(f"Pensja Feliksa bez zmian: {pracownik1.get_pensja()}")

print("-" * 40)

# zad 3.5


class Player:
    max_health = 100
    default_attack = 10
    default_heal = 5
    score_per_attack = 20
    score_per_heal = 3
    
    def __init__(self, nick):
        self.nick = nick
        self.__health = self.max_health
        self._score = 0
    
    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):
        old_health = self.__health
        if value < 0:
            self.__health = 0
        elif value > self.max_health:
            self.__health = self.max_health
        else:
            self.__health = value
            
        if self.__health != old_health:
            print(f"{self.nick} health value changed to {self.__health}")
            
    @property
    def level(self):
        return (self._score // 100) + 1
    
    def attack(self, enemy):
        if isinstance(enemy, Player):
            damage = self.default_attack
            print(f"{self.nick} attacked {enemy.nick}")
            enemy.health -= damage
            self._score += self.score_per_attack
            if enemy.health <= 0:
                print(f"{enemy.nick} has been defeated")
                self._score +=20
        else:
            print(f"{self.nick} cannot attack {type(enemy)}")
        
    
    def heal(self):
        heal_amount = self.default_heal
        if self.health < self.max_health:
            print(f"{self.nick} healed himself")
            self.health += heal_amount
            self._score += self.score_per_heal
        else:
            print(f"{self.nick} is already at full health")
            
    def __str__(self):
        return f"{self.nick}: health={self.health}, level={self.level}"
    
    def __repr__(self):
        return f"Player(nick='{self.nick}')"
    
    
    
print("zadanko 3.5")
player1 = Player("Natalia")
player2 = Player("Feliks")
print(player1)
print(player2)

player1.attack(player2)
print(player1)
print(player2)

player2.heal()

for _ in range(10):
    if player2.health > 0:
        player1.attack(player2)
    else:
        break
    
print(player1)
print(player2)