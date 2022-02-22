"""
Jasio i Stasio grają w karty. Po skończonej sekwencji pewnych dziwnych ruchów, czas na wyłonienie zwycięzcy. Każdemu graczowi pozostała pewna liczba kart, których wartości należy zsumować. Wygrywa ten, który ma większą sumę. Wartość karty nie zależy od koloru, a jedynie od figury: 23456789TJQKA. Karta 2 ma wartość 2, a każda następna w ciągu ma wartość o 1 większą od poprzedniej. Widząc sekwencję kart Jasia i Stasia sprawdź, kto z nich wygrał.

Wejście
W pierwszym wierszu wejścia znajduje się sekwencja kart Jasia, w wierszu drugim - sekwencja kart Stasia. Sekwencje to ciągi znaków [23456789TJQKA] o długości nie większej niż 52.

Wyjście
Pierwszy i jedyny wiersz wyjścia powinien zawierać napis JASIO lub STASIO w zależności kto wygrał rozdanie. W przypadku remisu, należy wypisać na standardowe wyjście napis REMIS.

Przykład 1
Dla danych wejściowych:

T2T
A6
poprawną odpowiedzią jest:

JASIO
Przykład 2
Dla danych wejściowych:

Q72
AA
poprawną odpowiedzią jest:

STASIO
Przykład 3
Dla danych wejściowych:

77
A
poprawną odpowiedzią jest:

REMIS
"""
dict = {'2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
        }

jas = input()
stas = input()

pkt_jas, pkt_stas = 0, 0

for card in jas:
        pkt_jas+=dict[card]

for card in stas:
        pkt_stas+=dict[card]

if pkt_jas>pkt_stas:
        print('JASIO')
elif pkt_jas<pkt_stas:
        print('STASIO')
else:
        print('REMIS')