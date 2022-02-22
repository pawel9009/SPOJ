"""
Pewnego pięknego, słonecznego dnia grupa przyjaciół z niecierpliwością oczekiwała na początek kolejnego wspaniałego meczu w wykonaniu naszej piłkarskiej reprezentacji. Popijali Coca-Colę, opowiadali dowcipy, postanowili również coś zjeść. Jak przystało na prawdziwych informatyków zamówili pizzę. Dostawca przyjechał na czas, mecz właśnie się zaczynał, wszystko przebiegało bez problemów - do czasu gdy otworzyli karton. Oczom naszych bohaterów ukazał się przerażający widok - pizza nie była pokrojona! Co tu teraz począć? Po długim namyśle ustalili niezwykle przebiegły plan działania. Na ulotce z pizzerii znaleźli wielkość boku kwadratowego kartonu, zauważyli również, że pizza styka się z każdym jego brzegiem. Mając te informacje nie pozostało nic innego jak tylko ją pokroić. Każde wykonane cięcie powinno stanowić średnicę pizzy.

Wejście
W pierwszej linii wejścia znajduje się jedna liczba naturalna Z (1 ≤ Z ≤ 105) określająca ilość zestawów danych. W kolejnych liniach znajdują się zestawy danych.

W pierwszej i jedynej linii każdego zestawu danych znajdują się dwie liczby całkowite d, n (10 ≤ d ≤ 108; 3 ≤ n ≤ 106) opisujące odpowiednio długość boku kartonu od pizzy w centymetrach oraz ilość osób chętnych do jedzenia.

Wyjście
Dla każdego zestawu danych należy w osobnej linii wypisać dwie liczby określające odpowiednio co ile centymetrów należy przeciąć pizzę i ile takich cięć należy wykonać aby każdy otrzymał tyle samo pizzy, a kawałki były możliwie jak największe. W związku z tym, że nasi bohaterowie nie lubią marnować pieniędzy cała pizza musi zostać zjedzona. Pierwsza z liczb powinna zostać wypisana z dokładnością do trzech cyfr po przecinku.

Przykład
Wejście:

1
10 4
Wyjście:

7.854 2
"""
from math import pi
t = int(input())
lista = []
for a in range(t):
    dane = input().split(' ')
    lista.append([int(dane[0]),int(dane[1])])

[print("%.3f %u" % ((pi * x[0]) / (x[1]<<1), x[1])) if x[1]%2==1 else print("%.3f %u" % ((pi * x[0]) / x[1], x[1]>>1))for x in lista]