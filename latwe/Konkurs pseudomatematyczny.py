"""
Pewna stacja telewizyjna ogłosiła konkurs. Aby przyciągnąć widza, konkurs musiał mieć w sobie coś wyjątkowego. Szefowie stacji długo zastanawiali się nad tym, co to może być, ale im dłużej myśleli, tym bardziej stwierdzali, że wszystko już było. Wreszcie pewien pracownik wymyślił coś, czego jeszcze z pewnością nie było, a co było (przynajmniej według szefów stacji) genialne!

Pomysł polegał na tym, że w ciągu całego dnia na antenie, co jakiś czas, będą pokazywały się skomplikowane zadania matematyczne. Będą wśród nich do obliczania rozmaite całki, granice, szeregi itp. Widzowie będą musieli równania te rozwiązywać, a wyniki przesyłać smsami do siedziby stacji. Wygrywa oczywiście ten, kto rozwiąże poprawnie najwięcej zadań.

Konkurs miał już startować, kiedy prezes, po zapoznaniu się z zadaniami, stwierdził, że tak być nie może. Okazało się, że nie umiał on samodzielnie rozwiązać zadań, musiał prosić o pomoc swoich informatyków, którzy też męczyli się z nimi niemiłosiernie. Stwierdził, że zbyt wiele już zmienić nie można, bo za daleko posunęły się przygotowania, ale chociaż nagradzać można nie tylko według kryterium liczby rozwiązanych zadań. Żeby zasady były jak najprostsze, jak najbardziej zrozumiałe dla ludzi, a zarazem promujące humanistów, prezes zadecydował arbitralnie, że wygra, owszem, osoba, która rozwiąże najwięcej zadań, ale kolejne miejsca będą zajmowały te osoby, które rozwiążą zadań jak najmniej.

Nie trzeba chyba mówić, co o ignoranckiej decyzji prezesa myśli pomysłodawca konkursu...

Niemniej, co szef, to szef, i będzie właśnie tak, jak on chce. Jedyne, co udało się jeszcze wyprosić to to, że jeśli więcej niż jedna osoba rozwiąże najwięcej zadań prawidłowo, to zajmą one ex equo pierwsze miejsce.

Znając wyniki po zakończeniu konkursu, przygotuj dla prezesa ranking zawodów, aby mógł się on w nim umiejscowić (czyli interesuje go tylko liczba punktów poszczególnych miejsc).

Wejście
Pierwsza linia wejścia zawiera liczbę całkowitą D (1 ≤ D ≤ 500) oznaczającą liczbę zestawów danych. W pierwszej linii zestawu znajduje się jedna liczba całkowita N (1 ≤ N ≤ 200) oznaczająca liczbę uczestników konkursu. W drugiej linii znajduje się N nieujemnych liczb całkowitych pooddzielanych spacjami, oznaczających liczby punktów zdobywanych przez kolejnych uczestników konkursu. Maksymalną liczbą punktów do zdobycia był 1000.

Wyjście
Dla każdego zestawu danych należy wypisać w osobnej linii, uszeregowane w kolejności zgodnej z rankingiem, liczby punktów zdobyte przez zawodników.

Przykład
Wejście:

3
5
1 2 3 4 5
5
4 5 2 3 5
2
1 1

Wyjście:

5 1 2 3 4
5 5 2 3 4
1 1
"""
t = int(input())
for a in range(t):
    uczestnicy = int(input())
    dane = input().split(' ')
    tab = []
    for x in range(uczestnicy):
        tab.append(int(dane[x]))
    winner = max(tab)
    liczba_win = 0
    for z in tab:
        if z == winner:
            liczba_win += 1

    wynik = []
    for win in range(liczba_win):
        wynik.append(winner)
    tab.sort()
    for w in range(len(tab) - liczba_win):
        wynik.append(tab[w])

    for wy in wynik:
        print(wy)
