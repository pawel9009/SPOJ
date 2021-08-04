"""
Napisz funkcję:

 int nwd(int a, int b);
która oblicza największy wspólny dzielnik liczb a i b,

 0 <= a,b <= 1000000
Input


W pierwszej linii liczba testów t, w kolejnych liniach po dwie liczby w każdym wierszu.

Output
W każdej linii jedna liczba - wynik działania funkcji nwd

Example
Input:
5
1 4
4 1
12 48
48 100
123456 653421

Output:
1
1
12
4
3
"""


def NWD(a, b):
    if b > 0:
        return NWD(b, a % b)
    return a


t = int(input())
for x in range(t):
    zmienne = input().split(' ')
    a = int(zmienne[0])
    b = int(zmienne[1])
    print(NWD(a, b))
