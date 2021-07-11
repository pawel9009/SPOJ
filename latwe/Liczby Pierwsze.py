"""PRIME_T - Liczby Pierwsze
Sprawdź, które spośród danych liczb są liczbami pierwszymi

Input
n - liczba testów n<100000, w kolejnych liniach n liczb z przedziału [1..10000]

Output
Dla każdej liczby słowo TAK, jeśli liczba ta jest pierwsza, słowo: NIE, w przeciwnym wypadku.

Example
Input:
3
11
1
4

Output:
TAK
NIE
NIE"""

kandydat = [1 for x in range(10000)]
pierwsze = []
for i in range(2, 10000):
    if kandydat[i] != 0:
        pierwsze.append(i)
        for j in range(i + i, 10000, i):
            kandydat[j] = 0

t = int(input())
for x in range(t):
    n = int(input())
    if n in pierwsze:
        print("TAK")
    else:
        print("NIE")
