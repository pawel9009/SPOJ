"""
Sprawdź, czy podane 3 punkty są współliniowe, czy też nie.

Input
Najpierw zostaje podana liczba t (1 < t ≤ 100) wykonywanych testów. W każdej następnej linii podawane są współrzędne trzech punktów będącymi liczbami całkowitymi z przedziału [-1000, 1000]. Kolejne współrzędne oddzielone są znakiem tabulacji.

Output
Jako wydruk otrzymujemy słowo TAK, gdy podane trzy punkty są współliniowe albo słowo NIE, gdy nie są współliniowe. Każda odpowiedź zapisywana jest w osobnej linii.

Example
Input:
5
1	2	3	4	5	6
1	3	1	4	1	-3
1	2	-3	4	3	9
2	-1	3	-1	-4	-1
0	0	0	0	0 	0

Output:
TAK
TAK
NIE
TAK
TAK
"""

t = int(input())
for a in range(t):
    dane = input().split('	')
    A = (int(dane[0]), int(dane[1]))
    B = (int(dane[2]), int(dane[3]))
    C = (int(dane[4]), int(dane[5]))
    x, y = 0, 0
    rownanie = (B[0] - A[0]) * (C[1] - A[1])
    rownanie1 = (B[1] - A[1]) * (C[0] - A[0])
    if rownanie == rownanie1:
        print("TAK")
    else:
        print("NIE")
