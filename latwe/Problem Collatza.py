"""
Dany jest ciąg xn określony rekurencyjnie:
x0=s,
xn+1=3*xn+1, jeśli xn jest nieparzyste i
xn+1=xn/2, jeśli xn jest parzyste

Napisz program, który oblicza pierwsze takie n, dla którego xn=1.

Wejście


W pierwszej linii liczba testów t. W każdym z t kolejnych wierszy jedna liczba całkowita s, 1 <= s <= 10000.

Wyjście
W każdej linii jedna liczba - obliczona wartość n.

Przykład
Wejście:
5
1
2
8
3
567
Wyjście:
0
1
3
7
61
"""


def rek(s):
    iter = 0
    while s > 1:
        if s % 2 == 1:
            s = 3 * s + 1
            iter += 1
        elif s % 2 == 0:
            s = s / 2
            iter += 1
    return iter


t = int(input())
for x in range(t):
    s = int(input())
    print(rek(s))
