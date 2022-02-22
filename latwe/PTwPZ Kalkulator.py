"""
Kalkulator
Treść
Mała Ola jest uśmiechniętą i radosną uczennicą pierwszej klasy szkoły podstawowej. Dziewczynce wszystko się w szkole podoba. Jest tam bardzo miła pani wychowawczyni, trochę rozbrykanych koleżanek i kolegów w klasie oraz mnóstwo ciekawych rzeczy, o których można się dowiedzieć na lekcjach. Ulubionym przedmiotem Oli jest matematyka. Mała uczennica zna już wszystkie cyfry i potrafi dodawać i odejmować w pamięci. Po opanowaniu podstaw chce teraz nauczyć się obliczać dłuższe wyrażenia. Oczywiście sama nie poradzi sobie ze sprawdzaniem poprawności wyników. Ale od czego ma swój nowy błyszczący laptop i Ciebie, starszego kuzyna, prawdziwego komputerowego hakera. Pomóż Oli i napisz program, który obliczy wartość wprowadzonego wyrażenia arytmetycznego.

Wejście
Dane podawane są na standardowe wejście. W pierwszym wierszu podana jest liczba N (1<=N<=20) zestawów danych. Dalej podawane są zestawy danych zgodnie z poniższym opisem:

Jeden zestaw danych
W pierwszym i jedynym wierszu zestawu danych podane jest wyrażenie arytmetyczne. Wyrażenie to składa się na przemian z pojedynczych cyfr i znaków + bądź - . Długość wyrażenia jest nie mniejsza niż 3 znaki i nie większa niż 99 znaków.

Wyjście
Wyniki programu powinny być wypisywane na standardowe wyjście. W kolejnych wierszach należy podać odpowiedzi obliczone dla kolejnych zestawów danych. Wynikiem dla jednego zestawu jest wartość wyrażenia podanego na wejściu.

Przykład
dane wejściowe:
2
1+2+3-4
0-5+3

wynik:
2
-2
"""
def liczba_wytnij(dane):
    liczba = ''
    for char in dane:
        if char != '+' and char != '-':
            liczba += char
        else:
            break

    dane = dane[len(liczba)::]
    return dane, liczba

t = int(input())
for e in range(t):
    dane = input()

    dane,liczba = liczba_wytnij(dane)
    wynik = int(liczba)

    while len(dane)>0:
        liczba = ''
        dodawanie = True
        if dane[0] =='-':
            dodawanie=False
        dane=dane[1::]

        dane,liczba = liczba_wytnij(dane)

        if dodawanie:
            wynik+=int(liczba)
        else:
            wynik-=int(liczba)

    print(wynik)