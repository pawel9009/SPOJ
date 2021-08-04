"""
Dla podanego ciągu długości 2*k, wypisz na standardowe wyjście dokładnie pierwszą połowę ciągu.

Wejście
W pierwszej linijce wejścia znajduje się jedna liczba całkowita t (1<=t<=100). Każdy wiersz o numerze od 2 do t+1, zawiera ciąg długości 2*k (1<=k<=1000).

Wyjście
Dla każdego przypadku testowego na wyjściu powinien pojawić się ciąg będący pierwszą połową wczytanego ciągu.

Example
Wejście:
3
pierwszy
lubiec
ktotozrobi

Output:
pier
lub
ktoto
"""

t = int(input())
for x in range(t):
    text = input()
    l = len(text) // 2
    print(text[0:l])
