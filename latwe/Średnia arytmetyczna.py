"""
W tablicy n liczb całkowitych dodatnich znajdź tę, której wartość jest najbliższa warości średniej z wszystkich liczb.

Input
Najpierw t < 101 - liczba testów. W kolejnych liniach, dla każdego testu, liczba 0 < n < 100 i n liczb całkowitych dodatnich nie większych niż 100.

Output
Dla każdego testu, w kolejnych liniach, jedna liczba - pierwszy element tablicy, którego wartość jest najbliższa wartości średniej.

Example
Input:
3
4 1 2 3 4
4 4 3 2 1
4 0 3 2 4

Output:
2
3
2
"""


def wartosc_bezwzgledna(a, wynik):
    wart = wynik - a
    if wart < 0:
        wart *= -1
    return wart


t = int(input())
for x in range(t):
    dane = input().split(' ')
    n = int(dane[0])
    liczby = dane[1:]

    suma = 0
    for a in liczby:
        suma += int(a)
    srednia = suma / n
    index = None
    result = 999999
    for iterator in range(len(liczby)):
        wartosc_b = wartosc_bezwzgledna(int(liczby[iterator]), srednia)
        if wartosc_b < result:
            result = wartosc_b
            index = iterator

    print(int(liczby[index]))
