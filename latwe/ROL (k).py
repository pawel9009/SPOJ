"""
Przesuń elementy tablicy cyklicznie w lewo o zadaną liczbę miejsc.

Input
Najpierw dwie liczby n i k takie, że 1 < k < n < 10000, a następnie w kolejnym wierszu n liczb.

Output
W jednym wierszu n liczb w zmienionym porządku (przesuniętych cyklicznie o k miejsc).

Example
Input:
5 3
1 2 3 4 5

Output:
4 5 1 2 3
"""
dane = input().split(' ')
n = int(dane[0])
k = int(dane[1])
liczby = input().split(' ')

tab = []
for x in range(n):
    tab.append(int(liczby[x]))

pom = [0 for q in range(n)]

for a in range(len(tab)):
    pom[a] = tab[(a + k) % n]

for q in pom:
    print(q, end=" ")
