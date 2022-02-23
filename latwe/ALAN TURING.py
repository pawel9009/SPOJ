"""
Alan Turing — brytyjski matematyk, kryptolog, twórca koncepcji maszyny Turinga i jeden z twórców informatyki. Uważany za ojca sztucznej inteligencji.

Napisz program, który będzie imitował uproszczoną maszynę Turinga. W zasadzie do wykonania będzie miał tylko trzy instrukcje:

DODAJ [litera] — dodaje literę na koniec napisu,
USUN [liczba znaków] — usuwa z końca napisu podaną liczbę liter (lub mniej jeśli tyle w napisie nie istnieje),
ZAMIEN [litera] — zamienia ostatnią literę na podaną (lub nie robi nic, jeśli w napisie nie ma znaków).
Twój program powinien wypisać napis, który znajduje się w napisie po wykonaniu podanych instrukcji.

Wejście
W piewszym wierszu jedna liczba n określająca liczbę instrukcjii (nie więcej niż 1000).

W kolejnych n wierszach instrukcje zdefiniowane w treści zadania. Podane litery są dużymi znakami natomiast liczba liter do usunięcia jest nie większa niż miliard.

Wyjście
Napis, który zostanie otrzymany po wykonaniu instrukcji. Początkowo napis jest pusty.

Przykład
Wejście:
8
DODAJ T
DODAJ U
DODAJ R
DODAJ I
DODAJ T
USUN 1
DODAJ N
DODAJ G

Wyjście:
TURING
"""

t = int(input())
napis = ''
for q in range(t):
    dane = input().split(' ')
    polecenie = dane[0]
    argument = dane[1]
    if polecenie == 'DODAJ':
        napis += argument
    if polecenie == 'USUN':
        if len(napis) <= int(argument):
            napis = ''
        else:
            napis = napis[0:-int(argument)]
    if polecenie == 'ZAMIEN':
        if len(napis) > 0:
            napis = napis[:-1] + argument
print(napis)
