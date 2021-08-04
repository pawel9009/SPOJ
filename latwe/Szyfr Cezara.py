"""
Szyfr Cezara jest to szyfr za pomocą, którego Juliusz Cezar szyfrował swoje listy do Cycerona. Jako ciekawostkę można podać, że szyfr ten był podobno używany jeszcze w 1915 roku w armii rosyjskiej, gdyż tylko tak prosty szyfr wydawał się zrozumiały dla sztabowców.

Każdą literę tekstu jawnego zamieniamy na literę przesuniętą o 3 miejsca w prawo. I tak literę A szyfrujemy jako literę D, literę B jako E itd. W przypadku litery Z wybieramy literę C. W celu odszyfrowania tekstu powtarzamy operację tym razem przesuwając litery o 3 pozycje w lewo.

Input
Na wejściu pojawi się tekst zawierający jedynie wielkie litery alfabetu łacińskiego, spacje oraz znaki nowej linii, a jego długość nie przekracza 200 znaków.

Output
Na wyjściu otrzymujemy zaszyfrowany tekst używając Szyfru Cezara.

Example
Input:
ABC DEF
TERA EST ROTUNDA

Output:
DEF GHI
WHUD HVW URWXQGD
"""
while True:
    try:
        wynik = ""
        text = input()
        for x in text:
            if x == ' ':
                wynik += ' '
            elif x == 'X':
                wynik += 'A'
            elif x == 'Y':
                wynik += 'B'
            elif x == 'Z':
                wynik += 'C'
            else:
                znak = ord(x) + 3
                wynik += chr(znak)
        print(wynik)
    except:
        break
