"""
Zadanie polega na zamianie podanej liczby n, która jest w systemie dziesiątkowym, na liczbę w systemie szesnastkowym (cyfry:0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F) i jedenastkowym (cyfry:0,1,2,3,4,5,6,7,8,9,A).

Wejście
W pierwszym wierszu wejścia znajduje się dokładnie jedna t (1<=t<=10000) oznaczająca liczbę zestawów danych. W każdym wierszu od 2 do t+1 znajduje się dokładnie jedna liczba całkowita n (1<=n<=106).

Wyjście
W każdym wierszu wyjścia powinny znaleźć się dokładnie dwie liczby, pierwsza - oznaczająca podana liczbę w systemie szesnastkowym, druga - oznaczająca podana liczbę w systemie jedenastkowym.

Przykład
Wejście:
2
1263
10

Wyjście:
4EF A49
A A
"""

def zamien(x):
    znak = ''
    if x >= 0 and x < 10:
        znak = f'{x}'
    elif x == 10:
        znak = 'A'
    elif x == 11:
        znak = 'B'
    elif x == 12:
        znak = 'C'
    elif x == 13:
        znak = 'D'
    elif x == 14:
        znak = 'E'
    elif x == 15:
        znak = 'F'
    return znak


def hex(n):
    wynik = ""
    while n > 0:
        reszta = n % 16
        wynik += zamien(int(reszta))
        n //= 16
    return wynik[::-1]


def to_11(n):
    wynik = ""
    while n > 0:
        reszta = n % 11
        wynik += zamien(int(reszta))
        n //= 11
    return wynik[::-1]


t = int(input())
for x in range(t):
    n = int(input())
    print(hex(n), to_11(n))
