"""Flamaster
Kasia niedawno poznała wszystkie literki w szkole. Z wielką pasją potrafiła całe dnie spędzać na pisaniu długich słów swoim ulubionym flamastrem. Pisała i pisała "tasiemce" tak długo, aż flamaster wypisał się. Kasia posmutniała. Z trudem, ale udało jej się uprosić swoją mamę, aby kupiła jej nowy pisak. Musiała jednak obiecać, że tym razem będzie bardziej oszczędna przy jego używaniu żeby wystarczył na dłużej. Kasia zaczęła zastanawiać się w jaki sposób będzie mogła zrealizować obietnicę daną mamie.

Postanowiła, że aby zaoszczędzić wkład flamastra będzie wypisywała skróconą wersję wymyślanych wyrazów. Jeśli miała zamiar napisać więcej niż dwie takie same literki obok siebie w wyrazie, to teraz napisze literkę a następnie liczbę, określającą ilość wystąpień tej literki.
Zadanie
Twoim zadaniem jest dla zadanego wyrazu, który wymyśliła Kasia, podanie skróconej wersji tego wyrazu.
Wejście
W pierwszej linijce wejścia znajduje się liczba naturalna C, 1 ≤ C ≤ 50, oznaczająca ilość zestawów danych. W kolejnych C wierszach wejścia znajdują się zestawy danych. Każdy zestaw składa się z niepustego wyrazu złożonego z samych dużych liter alfabetu amerykańskiego. Długość wyrazu nie przekracza 200 znaków.
Wyjście
Dla każdego zestawu danych, dla zadanego wyrazu, na wyjściu powinna znaleźć się jego skrócona wersja.
Przykład
Dla danych wejściowych:
4
OPSS
ABCDEF
ABBCCCDDDDEEEEEFGGHIIJKKKL
AAAAAAAAAABBBBBBBBBBBBBBBB
prawidłowym rozwiązaniem jest:
OPSS
ABCDEF
ABBC3D4E5FGGHIIJK3L
A10B16"""

t = int(input())
for x in range(t):
    text = input()
    wynik = ""
    znak=0
    while znak < len(text):
        licznik = 0
        if znak != len(text)-1:
            if text[znak]!=text[znak+1]:
                wynik+=text[znak]
                znak += 1
                continue
            elif znak != len(text)-2 and text[znak] == text[znak + 1] and text[znak] == text[znak + 2]:

                char = text[znak]
                for a in range(znak,len(text)):
                    if char==text[a]:
                        licznik+=1
                    else:
                        break
                wynik+=char
                wynik+=str(licznik)
                if licznik>0:
                    znak+=licznik
                else:
                    znak += 1
                continue
            elif text[znak]== text[znak+1]:
                wynik += text[znak]
                znak += 1
                continue

        else:
            wynik+=text[znak]
            znak += 1

    print(wynik)
