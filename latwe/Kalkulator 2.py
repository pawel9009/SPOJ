"""
Napisz program, który działa jak prosty kalkulator z pamięcią obsługujący pięć operacji: dodawanie, odejmowanie, mnożenie, dzielenie i obliczanie reszty z dzielenia liczb całkowitych. Przyjmujemy, że nasz kalkulator ma w pamięci 10 rejestrów o numerach 0 - 9 oraz że wszystkie rejestry zawierają na początku zera.

Wejście
Na wejście programu podana zostanie pewna nieokreślona liczba zestawów danych. Zestawy składają się z jednoznakowego symbolu operacji do wykonania (+, -, *, /, % i z) oraz następujących po nim dwóch liczb całkowitych.

Wyjście
Na wyjściu programu ma się pojawić ciąg liczb będących rezultatem wykonania pojawiających się na wejściu poleceń. Poszczególne liczby należy rozdzielić znakami nowej linii. To, co należy wykonać, zależy od symbolu operacji. Symbole +, -, *, / i % nakazują wykonanie odpowiednio dodawania, odejmowania, mnożenia, dzielenia i obliczenia reszty z dzielenia liczb, które są przechowywane w rejestrach o podanych numerach. Symbol z nakazuje zapis wartości podanej jako drugi argument w rejestrze o numerze podanym jako pierwszy argument. (Po wykonaniu tej operacji nie trzeba nic wyświetlać). Uwaga! Można założyć, że dane wejściowe nie zawierają polecenia dzielenia przez 0.

Przykład
Wejście:
z 3 6
z 1 89
z 2 60
z 0 11
+ 0 1
- 1 2
* 2 3
/ 3 0
% 3 1

Wyjście:
100
29
360
0
6
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


rejestry = []
while True:
    try:
        dane = input().split(' ')
        znak = dane[0]
        a = int(dane[1])
        b = int(dane[2])
        if znak == 'z':
            rejestry.append([a, b])
            continue
        pom_a = 0
        pom_b = 0
        for row in rejestry:
            if row[0] == a:
                pom_a = row[1]
            elif row[0] == b:
                pom_b = row[1]

        print(kalkulator(znak, pom_a, pom_b))
    except:
        exit()
