"""
Telefony
Treść
Jeszcze kilkanaście lat temu wykręcanie numeru telefonicznego było czynnością, która niejedną sekretarkę mogła przyprawić o ból palców. Niewygodne tarcze na aparatach i impulsowy wybór numerów powodowały, że nawiązanie połączenia trwało przesadnie długo, zwłaszcza gdy linia była zajęta i przy każdej próbie trzeba było wykręcać ten sam numer.

Dziś sytuacja jest o niebo lepsza. Wybór numeru odbywa się tonowo, a do dyspozycji mamy wygodne klawiatury. Jedną z ich charakterystycznych cech jest przyporządkowanie każdej cyfrze trzech lub czterech liter, tak jak w tabeli poniżej.

 Cyfra 	 Litery
2	ABC
3	DEF
4	GHI
5	JKL
6	MNO
7	PQRS
8	TUV
9	WXYZ
Dzięki takiemu przyporządkowaniu pewne numery łatwiej jest zapamiętać jako tekst. Dla przykładu numer 252625682 może być reprezentowany przez tekst ALAMAKOTA. Takie udogodnienie ma jednak pewną wadę. Wszelkiego rodzaju formularze i inne dokumenty wymagają podania numeru w postaci cyfrowej, a to wymagałoby doskonałej pamięci lub użycia klawiatury telefonu. Napisz program, który będzie pomocny w takich sytuacjach, tzn. zamieni numer telefoniczny z postaci tekstowej na postać numeryczną.

Wejście
Dane podawane są na standardowe wejście. W pierwszym wierszu podana jest liczba N (1<=N<=20) zestawów danych. Dalej podawane są zestawy danych zgodnie z poniższym opisem:

Jeden zestaw danych
W pierwszym i jedynym wierszu zestawu danych podany jest ciąg wielkich liter alfabetu łacińskiego – tekstowa postać numeru telefonicznego. Długość ciągu jest nie mniejsza niż 4 i nie przekracza 20 znaków.

Wyjście
Wyniki programu powinny być wypisywane na standardowe wyjście. W kolejnych wierszach należy podać odpowiedzi obliczone dla kolejnych zestawów danych. Wynikiem dla jednego zestawu jest cyfrowa postać numeru telefonicznego podanego na wejściu.

Przykład
dane wejściowe:
2
ALAMAKOTA
BRZECZYSZCZYKIEWICZ

wynik:
252625682
2793299792995439429
"""

slownik = {'A':2,'B':2,'C':2,
           'D':3,'E':3,'F':3,
           'G':4,'H':4,'I':4,
           'J':5,'K':5,'L':5,
           'M':6,'N':6,'O':6,
           'P':7,'Q':7,'R':7, 'S':7,
           'T':8,'U':8,'V':8,
           'W':9,'X':9,'Y':9, 'Z':9}

t = int(input())
for a in range(t):
    dane = input()
    dane.upper()
    wynik = ''
    for znak in dane:
        wynik+=str(slownik[znak])
    print(wynik)
