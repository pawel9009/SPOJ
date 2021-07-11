"""
Dana jest lista punktów na płaszczyżnie. Posortuj je względem odległości od środka układu współrzędnych w metryce euklidesowej.

Wejście
W pierwszej linii liczba testów t (t < 100). Dla każdego testu najpierw n (1 ≤ n ≤ 1000) - liczba punktów i w kolejnych n liniach opis każdego punktu w formacie:
nazwa x y
gdzie nazwa jest unikalnym dla każdego testu ciągiem co najwyżej 10 liter alfabetu łacińskiego, a x i y są współrzędnymi punktu. Obie współrzędne są całkowite oraz -1000 ≤ x, y ≤ 1000. Kolejne testy oddzielone są jednym pustym wierszem. Żadne 2 punkty nie leżą w tej samej odległości od środka układu współrzędnych.

Wyjście
Dla każdego przypadku testowego w kolejnych n liniach posortowane punkty. Po każdym przypadku testowym jedna linia odstępu.

Przykład
Wejście:
2
3
A 0 0
C 5 5
B 1 -1

1
X 1 1

Wyjście:
A 0 0
B 1 -1
C 5 5

X 1 1
"""

import  math
from operator import attrgetter
class Lista(object):
    def __init__(self):
        self.lista =[]

    def add(self, pkt):
        self.lista.append(pkt)

    def show(self):
        for q in self.lista:
            print(q.nazwa, q.x, q.y)

    def sortuj(self):
        self.lista.sort(key=attrgetter('odleglosc'))


class Punkt(object):
    def __init__(self, nazwa, x ,y):
        self.nazwa = nazwa
        self.x = x
        self.y = y
        self.odleglosc = math.sqrt(self.x*self.x+self.y*self.y)

wynik = []
t = int(input())
for num in range(t):
    ile_pkt = int(input())
    tab = []
    lista = Lista()
    for pkt in range(ile_pkt):
        dane = input().split(' ')
        punkt = Punkt(dane[0], int(dane[1]), int(dane[2]))
        lista.add(punkt)
    lista.sortuj()
    lista.show()
    input()