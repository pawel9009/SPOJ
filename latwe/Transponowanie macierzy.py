"""
Transponuj podaną macierz.



Wejście
W pierwszym wierszu znajdują się dwie liczby m n (1<=m,n<=200) oznaczające odpowiednio liczbę wierszy oraz liczbę kolumn. Następnie następuje m wierszy, w każdym n liczb.

Wyjście
Na wyjściu powinna znaleźć się macierz transponowana do zadanej

Przykład
Wejście:
4 3
1 2 5
4 3 3
3 4 9
8 7 7

Wyjście:
1 4 3 8
2 3 4 7
5 3 9 7
"""
dane = input().split(' ')
m = int(dane[0])
n = int(dane[1])
matrix = [[0 for i in range(n)] for j in range(m)]
for x in range(m):
    row = input().split(' ')
    for r in range(n):
        matrix[x][r] = int(row[r])

for x in range(n):
    for y in range(m):
        print(matrix[y][x])
