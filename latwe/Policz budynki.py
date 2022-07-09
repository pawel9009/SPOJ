"""
Od jakiegoś czasu we Fraktalocji prowadzony jest spis powszechny. Fraktalocja to niewielki kraj, w którym ponumerowane zostały wszystkie budynki. Każdy mieszkaniec określając swoje miejsce zamieszkania, podaje tylko dwie informacje: numer budynku i nazwisko.

Od początku spisu rachmistrzowie dzwonili do poszczególnych osób, wypytując je o niezbędne dane i zapisywali je w swoich notatkach. Po zakończonej pracy rachmistrzowie przekazali Ci swoje notatki.

Odpowiedz na pytanie, ile budynków we Fraktalocji jest zamieszkałych?

Wejście
W pierwszym wierszu jedna liczba n (1 ≤ n ≤ 1000) określająca liczbę osób.

W każdym z kolejnych n wierszy znajdują się informacje dotyczące spisanej osoby w postaci:
numer_budynku nazwisko
Numer budynku zawiera się w przedziale [1, 1000]. Nazwisko składa się z liter alfabetu angielskiego, pierwsza litera jest wielka, a pozostałe małe. Jego długość zawiera się w przedziale [3, 20]. Nazwiska są unikatowe.

Wyjście
Na wyjściu wypisz liczbę zamieszkałych budynków we Fraktalocji.

Przykład
Wejście:

5
1 Kowalski
7 Nowicki
1 Nowak
2 Pawlak
2 Amowicz
Wyjście:

3
"""

t = int(input())
budynki = []
for x in range(t):
    dane = input().split(' ')
    if dane[0] not in budynki:
        budynki.append(dane[0])

print(len(budynki))
