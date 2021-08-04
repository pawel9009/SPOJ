"""
Wczytaj ciąg liczb. Następnie wypisz wczytane liczby w taki sposób, aby najpierw pojawiły się te, które wystąpiły na pozycjach parzystych, a następnie te, które wystąpiły na pozycjach nieparzystych; z zachowaniem pierwotnej kolejności w obrębie obu grup. Numerujemy od 1.

Wejście
Najpierw t - liczba testów. Następnie dla każdego testu liczba n i n liczb, n <= 100.

Wyjście
Dla każdego testu n liczb w opisanym porządku.

Przykład
Wejście:
2
4 1 2 3 5
3 9 8 7

Wyjście:
2 5 1 3
8 9 7
"""
t = int(input())
for x in range(t):
    dane = input().split(' ')
    n = int(dane[0])
    liczby = dane[1:]
    wynik = ""
    for znak in range(1, len(liczby), 2):
        wynik += f'{liczby[znak]} '
    for znak in range(0, len(liczby), 2):
        wynik += f'{liczby[znak]} '
    wynik = wynik[:-1]
    print(wynik)
