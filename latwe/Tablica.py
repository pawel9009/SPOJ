"""
Napisz program, który wczytuje z wejścia ciąg liczb i wypisuje go w odwróconej kolejności.

Wejście
Na wejście programu podana zostanie pewna nieokreślona, ale niewielka ilość liczb całkowitych rozdzielonych spacjami.

Wyjście
Na wyjściu ma się pojawić ciąg liczbowy, którego i-ta pozycja jest równa (n+1-i)-tej liczbie wczytanej z wejścia, gdzie n to ilość wczytanych liczb. Poszczególne liczby należy rozdzielić spacjami.

Przykład
Wejście:
1 2 3

Wyjście:
3 2 1
"""
tab = input().split(' ')
wynik = ""
for x in reversed(tab):
    wynik+=f'{x} '
print(wynik)