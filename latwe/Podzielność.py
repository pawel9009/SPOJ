"""
Wypisz wszystkie liczby ai podzielne przez x i niepodzielne przez y, gdzie 1 < ai < n < 100000.

Wejście
Najpierw w oddzielnej linii t liczba przypadków testowych następnie w kolejnych t liniach liczby n x y.

Wyjście
W kolejnych t liniach oddzielone pojedynczym odstępem liczby spełniające warunki zadania wypisane od najmniejszej do największej.

Przykład
Wejście:
2
7 2 4
35 5 12
Wyjście:
2 6
5 10 15 20 25 30
"""
t = int(input())
for a in range(t):
    dane = input().split(' ')
    n = int(dane[0])
    x = int(dane[1])
    y = int(dane[2])
    for num in range(x,n,x):
        if num%y==0:
            continue
        else:
            print(num)