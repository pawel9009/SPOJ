"""
Pan Stefan, powszechnie znany piosenkarz, planuje swoją największą trasę koncertową. Starannie wybrał miasta, w których chciałby zagrać oraz ustalił kolejnośc ich odwiedzania. Niestety badania rynku wykazały, że nie we wszystkich miastach zarobi (być może koszty organizacji koncertu będą większe niż zyski z biletów). Pan Stefan wydrukował już plakaty z listą planowanych koncertów, więc jedyne zmiany, na jakie mógłby sie zgodzić, to rozpoczęcie trasy być może później niż w pierwszym mieście na liście oraz zakończenie być może wcześniej niż w ostatnim mieście na liście.

Zadanie
Wyznacz, jaki jest największy możliwy zysk Pana Stefana na trasie otrzymanej w opisany powyżej sposób.

Wejście
Pierwsza linia wejścia zawiera jedną liczbę naturalną n (1≤n≤100 000) oznaczającą liczbę miast na trasie. W każdej z kolejnych n linii znajduje się jedna liczba całkowita z przedziału [-100 000,100 000] oznaczająca całkowity zysk lub stratę z organizacji koncertu w danym mieście.

Wyjście
Należy wypisać maksymalny możliwy zysk Pana Stefana.

Przykład
Wejście
5
1
-2
4
5
-2
Wyjście
9
Wejście
2
-1
-2
Wyjście
0
"""
t = int(input())
suma = 0
maximum = 0
for a in range(t):
    x = int(input())
    if suma > 0:
        suma += x
    else:
        suma = x
    if suma > maximum:
        maximum = suma
print(maximum)
