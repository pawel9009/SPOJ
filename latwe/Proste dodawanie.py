"""
Twoim zadaniem jest dodać wszystkie liczby całkowite podane na wejściu.

Wejście
W pierwszym wierszu znajduje się liczba t testów (0 < t < 100) Każdy test opisany jest w następujący sposób. W pierwszym wierszu dana jest liczba n - liczba liczb do zsumowania. Następnie podanych jest n liczb pooddzielanych spacją.

Przykład
Input:
2
5
1 2 3 4 5
2
-100 100

Output:
15
0
"""
t = int(input())

for x in range(t):
    n = int(input())
    tab = input().split(' ')
    suma = 0
    for a in tab:
        suma += int(a)
    print(suma)
