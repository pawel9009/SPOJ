"""
Tym razem napisz program, który dla danej liczby n. Wypisze wszystkie liczby 0,1,2,...,n przy czym obok siebie nie mogą znaleźć się kolejne dwie liczby.

Wejście
W pierwszym i jedynym wierszu dana jest liczba n (0 <= n <= 10^6).

Wyjście
n+1 kolejnych liczb 0,1,2,...,n oddzielanych spacjami wypisanych w dowolnej kolejności, przy czym żadne dwie sąsiednie liczby nie mogą różnić się o 1.

Jeśli niemożliwe jest wypisanie liczb w żądany sposób, Twój program powinien wypisać NIE.

Przykładowe wejście:
2
Przykładowe wyjście
NIE
Przykładowe wejście
4
Przykładowe wyjście
1 4 2 0 3
"""

liczba = int(input())
wynik = ""

if liczba == 0:
    wynik = "0"
elif liczba in (1, 2):
    wynik = "NIE"
elif liczba == 3:
    wynik = "2 0 3 1"
elif liczba == 4:
    wynik = "2 0 3 1 4"
elif liczba > 4:
    polowa = liczba // 2

    if liczba % 2:
        for x in range(polowa + 1):
            wynik += f'{x} '
            wynik += f'{polowa + 1 + x} '
    else:
        for x in range(polowa):
            wynik += f'{x} '
            wynik += f'{polowa + 1 + x} '
        wynik += f'{polowa} '

print(wynik)
