"""
W pewnym małym miasteczku rozchorowała się nauczycielka biologii. Dla tak małego miasteczka okazało się to ogromnie wielkim problemem. W okolicy nie było nikogo kto mógłby i chciałby zastąpić nauczycielkę ucząc dzieci w podstawówce biologii. Zwłaszcza, że akurat zgodnie z programem trzeba by zacząć przerabiać bardzo trudne tematy dotyczące rozmnażania zwierząt. Ponieważ nie było chętnych, dyrektor zadecydował, że dopóki nauczycielka nie wróci do szkoły, lekcje biologii będzie przeprowadzał nauczyciel matematyki. Mimo iż był on temu bardzo niechętny, nie mógł odmówić swojemu dyrektorowi.

Na pierwszej lekcji, którą miał przeprowadzić zgodnie z programem nauczania, powinien powiedzieć o tym, jak różnorodne mogą być długości ciąży u ssaków. Tak się akurat składało, że dzień wcześniej jego kolega, matematyk z dużego miasta, przesłał mu mejlem taką zagadkę:

Matka jest o 21 lat starsza od swojego dziecka. Za 6 lat dziecko będzie 5 razy młodsze od matki. Pytanie: Gdzie jest ojciec?

Rozwiązując tę zagadkę matematyk spostrzegł, że obliczył bez problemu moment poczęcia (chwila obecna) i urodzenia dziecka, czyli poznał długość trwania ciąży człowieka. Wpadł więc na doskonały pomysł, aby tylko modyﬁkować dane tego zadania, podstawiając odpowiednie gatunki zwierząt, i w ten sposób, uczyć bawiąc, pozwolić uczniom na poznanie długości trwania ciąży różnych zwierząt.

Niestety uczniowie okazali się mniej entuzjastycznie nastawieni do zagadki, a pomysł rozwiązywania łamigłówek matematycznych nie tylko na matematyce, ale także na lekcjach biologii, wydał im się mało traﬁony. Dlatego zamiast obliczać długości ciąży różnych gatunków zwierząt poprosili Cię o napisanie programu, który zrobi to za nich.

Dla danego gatunku zwierząt znając różnicę wieku między matką a dzieckiem, oraz wiedząc, kiedy dziecko będzie ile razy młodsze od matki, ustal długość trwania ciąży.

Wejście
Pierwsza linia wejścia zawiera liczbę całkowitą D (1 ≤ D ≤ 500) oznaczającą liczbę zestawów danych. Każdy zestaw znajduje się w osobnej linii i składa się z 3 liczb całkowitych X, Y, Z (1 ≤ X, Y, Z ≤ 1000, Z > 1). Po ich podstawieniu do zagadki brzmi ona następująco: "Matka jest o X lat starsza od swojego dziecka. Za Y lat dziecko będzie Z razy młodsze od matki."

Wyjście
Dla każdego zestawu danych należy wypisać w osobnej linii jedną liczbę – długość trwania ciąży badanego gatunku zwierząt. Aby trzymać się standardów biologicznych, długość ta powinna być wyrażona w liczbie miesięcy, które trwa ciąża. Ponieważ biologów nie interesują dokładne wartości ułamkowe, a wszystko jest zaokrąglane, ty także musisz zaokrąglić swój wynik do najbliższej liczby całkowitej i wypisać go na wyjście.

Uwaga: Zakładamy, że nauczyciel obliczył wcześniej sam wszystkie zadania i każde dane dają prawidłowy wynik, tzn. można na ich podstawie wyliczyć długość ciąży, która jest zawsze pewną dodatnią wartością (co oczywiście nie musi oznaczać, że wyjście musi być zawsze dodatnie).

Przykład
Wejście:

3
21 6 5
11 1 13
223 2 113

Wyjście:

9
1
0
"""

t = int(input())
for a in range(t):
    dane = input().split(' ')
    x = int(dane[0])
    y = int(dane[1])
    z = int(dane[2])

    matka = x
    dziecko = 0
    dziecko += y
    matka += y
    dziecko *= z
    wynik = (matka - dziecko) / (z - 1)
    if wynik < 0:
        print(round(wynik * -12))
    else:
        print(round(wynik * 12))
