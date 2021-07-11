"""
Napisz program, który wyznacza liczbę pierwiastków rzeczywistych równania kwadratowego.

Wejście
Na wejście programu podana zostanie pewna nieokreślona, ale niewielka ilość zestawów danych. Każdy zestaw składać się będzie z 3 liczb rzeczywistych (współczynników A, B i C równania Ax^2 + Bx + C = 0) rozdzielonych spacjami. Poszczególne zestawy zostaną rozdzielone znakiem nowej linii. Można przyjąć, że A jest różne od zera.

Wyjście
Na wyjściu ma się pojawić ciąg liczbowy, którego i-ta pozycja jest równa liczbie pierwiastków rzeczywistych i-tego wczytanego z wejścia równania. Poszczególne liczby należy rozdzielić znakami nowej linii.

Przykład
Wejście:
0.3 0.3 0.4
0.5 1 0.5
-0.5 -0.5 0

Wyjście:
0
1
2
"""
def licz(a,b,c):
    delta =b*b - 4*a*c
    if delta>0:
        return 2
    elif delta==0:
        return 1
    else:
        return 0



while True:
    try:
        we = input().split(' ')
        a=float(we[0])
        b=float(we[1])
        c=float(we[2])
        print(licz(a,b,c))
        print()
    except:
        exit()


