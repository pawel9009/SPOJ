"""
Janek jest posiadaczem stacji meteorologicznej. Od początku jej użytkowania nasz bohater zapisał n pomiarów temperatury. Janek zastanawia się teraz, ile różnych pomiarów temperatury zapisał?

Wejście
W pierwszej linii wejścia znajduje się liczba pomiarów temperatury n (1 ≤ n ≤ 1000000).

W drugiej linii znajduje się n pomiarów temperatury zapisanych przez Janka. Każdy pomiar temperatury to liczba całkowita z przedziału [-50, 50].

Wyjście
Na wyjściu należy wypisać odpowiedź na pytanie, ile różnych pomiarów temperatury zapisał Janek?

Przykład
Wejście:

7
-5 -5 -1 1 0 1 2
Wyjście:

5
Wyjaśnienie do przykładu:

Nasz bohater zapisał 5 różnych pomiarów temperatury:

2 °C
1 °C
0 °C
-1 °C
-5 °C
"""
while True:
    try:
        t = int(input())
        lista = set()
        dane = input().split(' ')
        [lista.add(x) for x in dane if len(lista)<=101]

        print(len(lista))
    except Exception:
        break