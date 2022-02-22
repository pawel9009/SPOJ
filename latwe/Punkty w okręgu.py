"""
Dane są: okrąg o środku o=(xo, yo) i promieniu r oraz n punktów pi=(xi, yi). Dla każdego punktu pi sprawdź, jego położenie względem okręgu o.

Wejście
W pierwszej linii 3 liczby całkowite z przedziału [-10000, 10000] będące współrzędnymi środka okręgu i jego promieniem. Następnie n - liczba punktów i w kolejnych n liniach po dwie liczby całkowite będące współrzędnymi kolejnego punktu.

Wyjście
Dla każdego punktu w osobnej linii jedna litera:
I, jeśli punkt leży w obszarze wewnętrznym okręgu
O, jeśli punkt leży w obszarze zewnętrznym okręgu
E, jeśli punkt leży na okręgu

Przykład
Wejście:
5 5 2
4
0 0
6 5
5 7
5 5
Output:
O
I
E
I
"""
import math

okreg = input().split(' ')
x = int(okreg[0])
y = int(okreg[1])
r = int(okreg[2])
t = int(input())
for a in range(t):
    dane = input().split(' ')
    x1 = int(dane[0])
    y1 = int(dane[1])
    odleglosc = math.sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1))
    if odleglosc < r:
        print("I")
    elif odleglosc == r:
        print('E')
    else:
        print('O')
