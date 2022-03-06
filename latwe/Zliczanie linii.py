"""
Napisz program, który obliczy liczbę linii pojawiających się na wejściu.

Wejście
Plik tekstowy.

Wyjście
Liczba linii w pliku wejściowym.

Przykład
Wejście:
ala
ma

kota

Wyjście:
4
"""

liczba_lini = 0
while True:
    try:
        input()
        liczba_lini+=1

    except Exception:
        break
print(liczba_lini)