"""
Napisz program, który działa jak prosty kalkulator obsługujący pięć operacji: dodawanie, odejmowanie, mnożenie, dzielenie i obliczanie reszty z dzielenia liczb całkowitych.

Wejście
Na wejście programu podana zostanie pewna nieokreślona liczba zestawów danych. Zestawy składają się z jednoznakowego symbolu operacji do wykonania (+ dodawanie, - odejmowanie, * mnożenie, / dzielenie całkowitoliczbowe, % reszta z dzielenia) oraz następujących po nim dwóch liczb całkowitych. Poszczególne składowe zestawu zostaną rozdzielone spacjami, a same zestawy znakiem nowej linii. Liczba testów nie przekracza 100, wynik zawiera się w typie int32.

Wyjście
Na wyjściu programu ma się pojawić ciąg liczb będących rezultatem wykonania pojawiających się na wejściu poleceń. Poszczególne liczby należy rozdzielić znakami nowej linii. Uwaga! Można założyć, że dane wejściowe nie zawierają polecenia dzielenia przez 0.

Przykład
Wejście:
+ 7 9
- 0 4
* 5 6
/ 8 3
% 5 2

Wyjście:
16
-4
30
2
1
"""


def kalkulator(znak, a, b):
    if znak == '+':
        return a + b
    elif znak == '-':
        return a - b
    elif znak == '*':
        return a * b
    elif znak == '/':
        return a // b
    elif znak == '%':
        return a % b


while True:
    try:
        dane = input().split(' ')
        znak = dane[0]
        a = int(dane[1])
        b = int(dane[2])
        print(kalkulator(znak, a, b))
    except:
        exit()
