"""
Napisz program, który wczyta n liczb całkowitych, a następnie wyświetli te, które spełniają podany warunek.

Do wczytywania liczb wykorzystaj fragment rozwiązania poprzedniego zadania. Następnie wczywaj znak określający warunek i przejrzyj tablicę od początku do końca wypisując te elementy, które go spełniają.

Wejście
W pierwszym wierszu n < 1000. W kolejnych n wierszach liczby całkowite z zakresu typu longint. Następnie jeden wiersz postaci:

< x, albo:
> x

Wyjście
Elementy z tablicy podanej na wejściu, które spełniają podany warunek.

Przykład 1
Wejście:
5
2
7
0
6
2
> 4

Wyjście:
7
6
Przykład 2
Wejście:
5
2
7
0
6
2
< 3

Wyjście:
2
0
2
"""
t = int(input())
tab = []
for x in range(t):
    tab.append(int(input()))
dane = input().split(' ')
znak = dane[0]
liczba = int(dane[1])
for a in tab:
    if znak == '>':
        if a > liczba:
            print(a)
    elif znak == '<':
        if a < liczba:
            print(a)
