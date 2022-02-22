"""
Napisz program, który sprawdzi, czy dane słowo zawiera słowo 'sto'.

Wejście
Pierwszy i jedyny wiersz wejścia zawiera jedno słowo, ciąg małych liter alfabetu łacińskiego, którego długość nie przekracza 100 znaków.

Wyjście
W pierwszym i jedynym wierszu wyjścia należy wypisać słowo TAK, gdy odpowiedź na pytanie postawione w treści zadania jest twierdząca, w przeciwnym razie należy wypisać NIE.

Przykład 1
Dla danych wejściowych:

istota
poprawną odpowiedzią jest:

TAK
Przykład 2
Dla danych wejściowych:

strop
poprawną odpowiedzią jest:

NIE
"""
while True:
    try:
        wejscie = input()
        flaga = False
        if wejscie.find('sto',0) >=0:
            print('TAK')
        else:
            print('NIE')
    except Exception:
        break

