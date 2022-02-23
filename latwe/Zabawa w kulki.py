"""
Z okazji Dnia Dziecka w szkole Jasia organizowany jest konkurs, o to kto więcej razy trafi do okrągłej miski. Jasio wraz z kolegami z chęcią zapisali się na udział w tym konkursie.

Z powodu dużego zainteresowania tym konkursem, szkoła utrudniła zadanie. Wszystkie osoby, które wzięły udział w konkursie, będą mogli w nim wziąć udział jedynie z zasłoniętymi oczami, przez co każda osoba może rzucić kulką przed siebie, w bok, a nawet za siebie.

Jako dobry programista i przyjaciel Jasia postanawiasz napisać program, który wyznacz osobę, która wygrała oraz ilość trafień jakie wykonała poprawnie.

Wejście
W pierwszym wierszu wpisujemy współrzędne miski (x, y), jej promień oraz liczbę rzutów.

W drugim wierszu wpisujemy ilość uczestników, nie większa niż 1000.

W każdym teście wypisujemy imię uczestnika oraz współrzędne każdego rzutu piłką.

Wyjście
Na wyjściu powinno znaleźć się imię wygranej osoby oraz liczba poprawnych trafień do miski. Trafienie zaliczamy, jeżeli odległość kulki od miski jest mniejsza lub równa.

Jeżeli osób wygranych jest więcej niż jeden, wypisz imię oraz liczbę poprawnych trafień pierwszej osoby.

Przykład
Wejście:
10 5 2 4

3

Adam

2 8

3 4

5 6

7 9

Oliwia

1 1

8 7

10 5

10 6

Bartosz

3 8

9 6

1 2

3 4

Wyjście:
Oliwia 2
"""
from math import sqrt

dane = input().split(' ')
dict = {}

x = int(dane[0])
y = int(dane[1])
r = int(dane[2])
n = int(dane[3])
ilosc_uczestnikow = int(input())
for q in range(ilosc_uczestnikow):
    imie = input()
    dict[imie] = 0
    for w in range(n):
        wejscie = input().split(' ')
        x1 = int(wejscie[0])
        y1 = int(wejscie[1])
        odleglosc = sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1))
        if odleglosc <= r:
            dict[imie] += 1

wygrany = ''
pkt = 0
for k, v in dict.items():
    if v > pkt:
        pkt = v
        wygrany = k

print(wygrany, dict[wygrany])
