"""
Przesuń elementy w tablicy w taki sposób, jak pokazano w przykładzie (obróć ramkę w lewo).

Wejście
Najpierw t - liczba testów. Następnie dla każdego testu dwie liczby l i k - odpowiednio liczba wierszy i kolumn w tablicy - następnie l wierszy po k liczb całkowitych, 3 <= l, k <= 100.

Wyjście
Dla każdego testu l wierszy po k liczb w zmienionym porządku.

Przykład 1
Wejście:
1
3 3
1 2 3
4 5 6
7 8 9

Wyjście:
2 3 6
1 5 9
4 7 8
Przykład 2
Wejście:
1
3 5
1 2 3 4 5
6 7 8 9 0
1 2 3 4 5

Wyjście:
2 3 4 5 0
1 7 8 9 5
6 1 2 3 4
"""


def ramka(mac):
    height = len(mac) - 1

    top = mac[0].copy()
    dl = len(top) - 1

    bot = mac[height].copy()

    pom_x = mac[height - 1][0]
    pom_y = mac[1][dl]

    for e in range(height):
        mac[height - e][0] = mac[height - (e + 1)][0]
        mac[e][dl] = mac[e + 1][dl]

    for q in range(len(top) - 1):
        top[q] = top[q + 1]
        bot[dl - q] = bot[dl - (q + 1)]

    mac[0] = top
    mac[height] = bot

    mac[height][0] = pom_x
    mac[0][dl] = pom_y

    for a in mac:
        for b in a:
            print(b)


t = int(input())
for w in range(t):
    dane = input().split(' ')
    l = int(dane[0])
    k = int(dane[1])
    matrix = [[0 for i in range(k)] for l in range(l)]
    for x in range(l):
        row = input().split(' ')
        for r in range(k):
            matrix[x][r] = int(row[r])

    ramka(matrix)
