"""
SUMA - Suma
Napisz program, który oblicza sumę pojawiających się na wejściu liczb.

Wejście
Na wejście programu podana zostanie pewna nieokreślona, ale niewielka ilość małych liczb całkowitych (z zakresu -100..100). Poszczególne liczby zostaną rozdzielone znakiem nowej linii.

Wyjście
Na wyjściu ma się pojawić ciąg liczbowy, którego i-ta pozycja jest równa sumie i pierwszych wczytanych z wejścia liczb. Poszczególne liczby należy rozdzielić znakami nowej linii.

Przykład
Wejście:
6
8
-3

Wyjście:
6
14
11
"""
suma = 0
for x in range(10):
    a = int(input())
    suma += a
    print(suma)
