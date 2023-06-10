import random
import math

class Vector():
    """Przechowuje kolekcję liczb."""

    def __init__(self, *args):
        if len(args) == 0:
            self.values = [0, 0, 0]
        else:
            self.wektor = list(args)

    def generate(self, argumenty):
        """Generuje wektor o losowych wspórzędnych"""
        
        self.wektor = []
        for i in range(argumenty):
            i = random.randint(-100, 100)
            self.wektor.append(i)
        print(self.wektor)

    def load(self, lista):
        """Przekształca argument zdefiniowany jako lista w wektor"""
        for i in range(len(lista)):
            self.wektor[i] = lista[i]
        return self.wektor

    def add(self, other):
        """Dodaje do siebie poszczególne współrzędne wektorów o tych samych wymiarach"""
        vectors_sum = []
        if len(self.wektor) == len(other.wektor):
            for i in range(len(self.wektor)):
                sum = self.wektor[i] + other.wektor[i]
                vectors_sum.append(sum)
            print(vectors_sum)
        else:
            print("Wektory mają inną liczbę argumentów")

    def subtract(self, other):
        """Odejmuje od siebie poszczególne współrzędne wektorów o tych samych wymiarach"""
        vectors_difference = []
        if len(self.wektor) == len(other.wektor):
            for i in range(len(self.wektor)):
                difference = self.wektor[i] - other.wektor[i]
                vectors_difference.append(difference)
                print(vectors_difference)
        else:
            print("Liczba wymiarów podanych wektorów jest różna od siebie")

    def scalar_multiplication(self, skalar):
        """Wylicza iloczyn skalarny"""
        for i in range(len(self.wektor)):
            self.wektor[i] = self.wektor[i]*skalar
        print(self.wektor)

    def lenght(self):
        """ Oblicza długość wektora"""
        l = math.sqrt(sum(x**2 for x in self.wektor))
        print("Długość wektora:", l)

    def arguments_sum(self):
        """Podaje sumę wszystkich argumentów wektora"""
        s = sum(x for x in self.wektor)
        print("Suma elementów wektora:", s)

    def scalar_product(self, other):
        """Wylicza iloczyn skalarny wektorów o tej samej ilości wymiarów"""
        m = 0
        if len(self.wektor) == len(other.wektor):
            for i in range(len(self.wektor)):
                a = self.wektor[i]*other.wektor[i]
                m += a
            print("Iloczyn skalarny wektorów wynosi:", m)

    def __str__(self):
        """Podaje nam współrzędne wektora"""
        print("Współrzędne wektora:")
        for i in range(len(self.wektor)):
            print("Współrzędna nr", i+1, "=", self.wektor[i])

    def argument(self, x):
        """Podaje współrzędną stojącą w danym wymiarze wektora"""
        print(self.wektor[x-1])

    def check(self, x):
        """ Sprawdza, czy dana współrzędna zawiera się w którymś wymiarze wektora"""
        if x in self.wektor:
            print("Współrzędna zawiera się w danym wektorze")
        else:
            print("Współrzędna nie zawiera się w danym wektorze")

Wektor_losowy_1 = Vector()
Wektor_losowy_1.generate(3)
Wektor_losowy_1.__str__()
Wektor_1 = Vector(1, 2, 3)

Wektor_1.scalar_product(Wektor_losowy_1)

Wektor_1.__str__()

lista=[1, 2, 3]

x = Vector(0, 0, 0)

x.load(lista)

x.lenght()

x.check(2)

x.argument(3)

a = Vector()
a.generate(30)
Wektor_1.add(Wektor_losowy_1) 
Wektor_1.arguments_sum()


