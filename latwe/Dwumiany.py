"""
Dla liczb całkowitych n i k, 0 <= k <= n <= 1000, wyznacz liczbę różnych k-elementowych podzbiorów zbioru n-elementowego. Liczby n i k będą dobrane tak, aby wynik nie przekroczył 1 000 000 000.

Input
T [ liczba testów, T <= 10000 ]
n_1 k_1
n_2 k_2
...
n_T k_T

Output
wynik_1
wynik_2
...
wynik_T
"""


def silnia(n):
    if n == 0:
        return 1
    for x in range(n - 1, 1, -1):
        n *= x
    return n


t = int(input())
for x in range(t):
    dane = input().split(' ')
    n = int(dane[0])
    k = int(dane[1])
    print(int(silnia(n) / (silnia(k) * silnia(n - k))))
