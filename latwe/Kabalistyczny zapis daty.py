"""
Istnieje bardzo łatwy sposób zapisu daty. Ten typowo barokowy pomysł nawiązywał do kabały, w której literom hebrajskim przypisane były liczby. W tym wypadku litery alfabetu łacińskiego odpowiadały następującym liczbom:

A       B       C       D       E       F       G       H       I       K
1       2       3       4       5       6       7       8       9       10
L       M       N       O       P       Q       R       S       T       V
20      30      40      50      60      70      80      90      100     200
X       Y       Z
300     400     500
Datę oblicza się sumując wszystkie liczby odpowiadające kolejnym literom tekstu. Zapis stosowano w drukach i rękopisach. W przypadku druków najczęściej podawano pod poszczególnymi słowami sumę liczb ich liter. Autorzy trudzili się nad stworzeniem tekstu, z którego daje się odczytać datę.

Input
Na wejściu podany jest wyraz, pisany małymi literami (używając wyłącznie liter podanych powyżej). Wyraz nie większy niż 25 znaków.

Output
Na wyjściu podany jest rok w postaci liczby naturalnej, który zapisałeś za pomocą wyrazu (czyli sumy każdej z liczb).

Example 1
Input:
info

Output:
105
Example 2
Input:
miska

Output:
140
"""
slownik = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'K': 10,
    'L': 20,
    'M': 30,
    'N': 40,
    'O': 50,
    'P': 60,
    'Q': 70,
    'R': 80,
    'S': 90,
    'T': 100,
    'V': 200,
    'X': 300,
    'Y': 400,
    'Z': 500,
}
text = input()
text = text.upper()
suma = 0
for x in text:
    suma += slownik[x]
print(suma)
