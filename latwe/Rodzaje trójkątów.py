"""
Dla długości boków a, b i c wypisz rodzaj trójkąta.

Wejście
Nieznana liczba testów.

Każdy z nich składa się z trzech liczb: a, b i c (wszystkie < 10000).

Wyjście
Jedno słowo określające rodzaj trójkąta ("prostokatny", "rozwartokatny", "ostrokatny") lub "brak", jeśli taki trójkąt nie istnieje.

Przykład
Wejście:
1 1 10
3 4 5
2 3 4
7 7 7
Wyjście:
brak
prostokatny
rozwartokatny
ostrokatny
"""

def sprawdz_boki(args):
    if sum(args) > 2 * max(args):
        return True
    return False


while True:
    try:
        dane = input().split(' ')
        a, b, c = dane
        a = int(a)
        b = int(b)
        c = int(c)
        if sprawdz_boki([a, b, c]):
            if a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
                print("prostokatny")
            else:
                if a*a+b*b<c*c or b*b+c*c<a*a or a*a+c*c<b*b:
                    print("rozwartokatny")
                else:
                    print("ostrokatny")
        else:
            print('brak')
    except Exception:
        break
