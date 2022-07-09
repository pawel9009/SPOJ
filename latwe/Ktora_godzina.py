"""
Odczytaj godzinę z pewnego specyficznego zegara.

Wejście
Cztery niewielkie liczby całkowite, złożone wyłącznie z 0 i 1.

Wyjście
Wypisz godzinę w formacie GG:MM.

Przykład
Wejście:

0 1 11 110
Wyjście:

01:36
"""


def zamien(str):
    cyfra = 0
    i = len(str) - 1
    for char in str:
        if char == '1':
            cyfra += 2 ** i
            i -= 1
        else:
            i -= 1
    return cyfra


dane = input().split(' ')

print(f'{zamien(dane[0])}{zamien(dane[1])}:{zamien(dane[2])}{zamien(dane[3])}')
