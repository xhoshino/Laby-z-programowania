from abc import ABC, abstractmethod
import random
import math

# zad 1

class Transport(ABC):
    def __init__(self, start, koniec, ladunek):
        self.start = start
        self.koniec = koniec
        self.ladunek = ladunek
    
    @abstractmethod
    def transportuj(self, nowy_koniec):
        pass
    
    def get_start(self):
        return self.start
    
    def get_ladunek(self):
        return self.ladunek
    
    def get_koniec(self):
        return self.koniec
    
    def __str__(self):
        return f"Transport z {self.start} do {self.koniec}, ładunek: {self.ładunek}"
    
    def __repr__(self):
        return self.__str__()
    
class Samolot(Transport):
    def __init__(self, start, koniec, ladunek, ilosc_pasazerow, ilosc_bagazy):
        super().__init__(start, koniec, ladunek)
        self.ilosc_pasazerow = ilosc_pasazerow
        self.ilosc_bagazy = ilosc_bagazy
        
    def transportuj(self, nowy_koniec):
        self.start = self.koniec
        self.koniec = nowy_koniec
        print(f"Samolot startuje z {self.get_start()} do {self.get_koniec()}.")
        print(f"Liczba pasażerów: {self.ilosc_pasazerow}, liczba bagaży: {self.ilosc_bagazy}")
        
    def __str__(self):
        return (f"Samolot: z {self.start} do {self.koniec}, ładunek: {self.ladunek}, "
                f"pasażerowie: {self.ilosc_pasazerow}, bagaże: {self.ilosc_bagazy}")
        
    def __repr__(self):
        return self.__str__()
    
    
class Statek(Transport):
    def __init__(self, start, koniec, ladunek, rodzaj_ladunku, ilosc_kontenerow):
        super().__init__(start, koniec, ladunek)
        self.rodzaj_ladunku = rodzaj_ladunku
        self.ilosc_kontenerow = ilosc_kontenerow

    def transportuj(self, nowy_koniec):
        print(f"Statek wypływa z portu {self.get_start()} do portu {self.get_koniec()}.")
        print(f"Rodzaj ładunku: {self.rodzaj_ladunku}, liczba kontenerów: {self.ilosc_kontenerow}")
        self.start = self.koniec
        self.koniec = nowy_koniec

    def __str__(self):
        return (f"Statek: z {self.start} do {self.koniec}, ładunek: {self.ladunek}, "
                f"rodzaj ładunku: {self.rodzaj_ladunku}, kontenery: {self.ilosc_kontenerow}")

    def __repr__(self):
        return self.__str__()
    
    
class Ciezarowka(Transport):
    def __init__(self, start, koniec, ladunek, ilosc_palet, typ_ladunku):
        self.ilosc_palet = ilosc_palet
        self.typ_ladunku= typ_ladunku
        super().__init__(start, koniec, ladunek)
        
    def transportuj(self, nowy_koniec):
        self.start = self.koniec
        self.koniec = nowy_koniec
        print(f"ciężarówka startuje z {self.get_start()} do {self.get_koniec()}.")
        print(f"Liczba palet: {self.ilosc_palet}, typ ladunku: {self.typ_ladunku}")
        
    def __str__(self):
        return (f"Ciężarówka: z {self.start} do {self.koniec}, ładunek: {self.ladunek}, "
                f"palety: {self.ilosc_palet}, ładunek: {self.typ_ladunku}")
        
    def __repr__(self):
        return self.__str__()
    
samolot = Samolot("Warszawa", "Paryż", "poczta lotnicza", 150, 300)
print(samolot)
samolot.transportuj("Londyn")
print(samolot)

statek = Statek("Gdańsk", "Sztokholm", "samochody", "auta osobowe", 50)
print(statek)
statek.transportuj("Helsinki")
print(statek)

ciezarowka = Ciezarowka("Kraków", "Berlin", "elektronika", 20, "sprzęt RTV")
print(ciezarowka)
ciezarowka.transportuj("Praga")
print(ciezarowka)
print("-" * 40)

# zad 2

class GameObject(ABC):
    def __init__(self, health):
        self.health = health

    def is_alive(self):
        return self.health > 0
    
    @abstractmethod
    def interact(self, player):
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__} (HP: {self.health})"
    
    def __repr__(self):
        return self.__str__()
    
class Player(GameObject):
    def interact(self, player):
        pass
    
class Monster(GameObject):
    def interact(self, player):
        player.health -= 10
        self.health = 0
        print("Gracz zabił potwora")

class Door(GameObject):
    def interact(self, player):
        print("Gracz przeszedł przez drzwi")


player = Player(50)
objects = []

for _ in range(10):
    if random.random() < 0.7:
        objects.append(Monster(health=10))
    else:
        objects.append(Door(health=0))
        
for i, obj in enumerate(objects, 1):
    print(f"{i}. ", end="")
    obj.interact(player)
    if not player.is_alive():
        print(f"{i + 1}. Gracz z dech")
        break

print("-" * 40)

# zad 3

class Equation(ABC):
    def __init__(self, coefficients):
        self.coefficients = coefficients
    
    @abstractmethod
    def solve(self):
        pass
    
class LinearEquation(Equation):
    def __init__(self, coefficients):
        if len(coefficients) != 2:
            raise ValueError("Równanie liniowe ma mieć 2 wwspółczynniki")
        super().__init__(coefficients)

    def solve(self):
        a, b = self.coefficients
        if a != 0:
            x = -b /a
            print(f"x = {x}")
        else:
            if b == 0:
                print("Nieskończeniewiele rozwiązań")
            else:
                print("brak rozwiązań")
                
class QuadraticEquation(Equation):
    def __init__(self, coefficients):
        if len(coefficients) != 3:
            raise ValueError("Równanie kwadrtowe ma mieć 3 wwspółczynniki")
        super().__init__(coefficients)
    
    def solve(self):
        a, b, c = self.coefficients
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            sqrt_delta = math.sqrt(delta)
            x1 = (-b - sqrt_delta) / (2 * a)
            x2 = (-b + sqrt_delta) / (2 * a)
            print(f"x1 = {x1}, x2 = {x2}")
        elif delta == 0:
            x = -b / (2*a)
            print(f"x = {x}")
        else:
            print("brak rozwiązań")
            
eq = LinearEquation([2, 0])
eq.solve()

eq1 = LinearEquation([0, 2])
eq1.solve()

eq2 = QuadraticEquation([1, -5, 6])
eq2.solve()