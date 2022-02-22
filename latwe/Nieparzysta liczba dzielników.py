"""
Napisz program, który sprawdzi, czy liczba ma nieparzystą liczbę dzielników.

Wejście
Pierwszy i jedyny wiersz wejścia zawiera jedną liczbę całkowitą n (1 ≤ n ≤ 109).

Wyjście
W pierwszym i jedynym wierszu wyjścia należy wypisać słowo TAK, gdy liczba z wejścia ma nieparzystą liczbę dzielników, w przeciwnym przypadku należy wypisać słowo NIE.

Przykład 1
Dla danych wejściowych:

4
poprawną odpowiedzią jest:

TAK
Przykład 2
Dla danych wejściowych:

6
poprawną odpowiedzią jest:

NIE
"""
import math

while True:
    try:
        liczba = int(input())
        lista = []
        [lista.append(x) for x in range(1, int(math.sqrt(liczba)) + 1) if liczba % x == 0]
        [lista.append(liczba // lista[i]) for i in range(len(lista) - 1, -1, -1) if (liczba / lista[i] != lista[i])]
        if len(lista) % 2 == 1:
            print("TAK")
        else:
            print("NIE")
    except Exception:
        break
