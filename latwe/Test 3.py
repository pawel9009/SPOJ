"""
Przepisz dane z wejścia na wyjście. Dane wejściowe są dwucyfrowymi liczbami naturalnymi. Zakończ działanie programu, gdy na wejściu pojawi się, trzecia liczba 42 poprzedzona jakąkolwiek inną liczbą, różną od 42.

Wejście
W każdej linii jedna liczba dwucyfrowa.

Wyjście
W każdej linii jedna liczba dwucyfrowa. Odczytane wartości 42 również powinny się pojawić.

Przykład
Wejście:
42
42
12
13
42
11
42
43
42
42
99
01
Wyjście:
42
42
12
13
42
11
42
43
42
"""
pom = 42
i = 0
tab = []
while True:
    n = int(input())
    if n != pom and n == 42:
        i += 1
    pom = n
    tab.append(n)
    if i == 3:
        break

for x in tab:
    print(x)
