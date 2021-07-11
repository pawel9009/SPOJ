"""

PP0502B - Tablice
Odwróć kolejność elementów w tablicy.

Wejście
Najpierw liczba testów t (t ≤ 100). Następnie dla każdego testu liczba n (n ≤ 100) i n liczb oddzielonych spacjami.

Wyjście
Dla każdego testu n liczb w porządku odwrotnym niż na wejściu.

Przykład
Wejście:
2
7 1 2 3 4 5 6 7
3 3 2 11

Wyjście:
7 6 5 4 3 2 1
11 2 3
"""
t = int(input())
for x in range(t):
    text = input().split(' ')
    n = int(text[0])
    tab=text[1:]
    wynik = ""
    for a in range(n,0,-1):
        wynik+=f'{text[a]} '
    print(wynik)


