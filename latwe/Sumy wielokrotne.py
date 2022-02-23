"""
Napisz program, który sumuje pojawiające się na wejściu liczby całkowite.

Wejście
Na wejście programu podana zostanie pewna nieokreślona ilość zestawów danych. Pojedynczy zestaw składa się z ciągu liczb całkowitych, rozdzielonych spacjami i kończących się zerem. Poszczególne zestawy zostaną rozdzielone znakiem nowej linii.

Wyjście
Na wyjściu mają się pojawić sumy liczb z poszczególnych zestawów danych. Ich wartości należy rozdzielić znakami nowej linii. Na samym końcu należy dodatkowo podać sumę wszystkich wczytanych z wejścia liczb (jest ona mniejsza niż 1015).

Przykład
Wejście:
11 8 2 -1 0
6 33 -9 10 0
0

Wyjście:
20
40
0
60
"""

suma = 0
while True:
    try:
        suma_l = 0
        dane = input().split(' ')
        for x in dane:
            suma_l+=int(x)
        suma+=suma_l
        print(suma_l)
    except Exception:
        break
print(suma)