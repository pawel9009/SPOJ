"""

PTROL - ROL
Przesuń elementy tablicy cyklicznie w lewo.

Wejście
Najpierw liczba testów t (t ≤ 100). Następnie dla każdego testu liczba n (1 < n ≤ 100) i n liczb.

Wyjście
Dla każdego testu n liczb w zmienionym porządku.

Przykład
Wejście:
2
7 1 2 3 4 5 6 7
3 2 1 10

Wyjście:
2 3 4 5 6 7 1
1 10 2
"""
t = int(input())
for x in range(t):
    text = input().split(' ')
    n = int(text[0])
    tab=text[1:]
    wynik = ""
    pierwszy = tab[0]
    for a in range(1,len(tab)):
        wynik+=f'{tab[a]} '
    wynik+=pierwszy
    print(wynik)


