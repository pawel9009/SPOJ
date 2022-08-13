"""
Rywal Wolfganga Pucka - Emeril Lagasse ("BAM!") ustanowił ostatnio rekord w upieczeniu najmniejszego soufflé na świecie mierzącego dokładnie 2 cm. Wolfgang doszedł do wniosku, że nie może być gorszy od niego i postanowił upiec najbardziej symetryczne ciasto na świecie. Z pewnością zadanie nie należy do najłatwiejszych ;)

Wszyscy dobrze wiemy (z ostatniej bestsellerowej książki Wolfganga), że jest on przesądny. Aby ciasto mu się udało, od chwili włożenia do piekarnika, musi wyciągnąć je o najbliższej godzinie, która jest palindromem (ale nie o tej, o której włożył on ciasto do piekarnika). Kiedy Wolfgang będzie miał okazję do wyciągnięcia ciasta ??

Wejście
W pierwszej linijce standardowego wejścia znajduje się dokładnie jedna liczba całkowita n - liczba prób Wolfganga do upieczenia jego ciasta. W kolejnych n liniach otrzymasz godzinę w formacie "GG:MM", wskazującą obecną godzinę w formacie 24-godzinnym (Więc 0 <= GG <= 23 oraz 0 <= MM <=59 i godzina "00:00" następuje po godzinie "23:59").

Wyjście
Dla każdego przypadku na wyjściu powinna pojawić się godzina w formacie "GG:MM". UWAGA: Sprawdzając czy godzina jest palindromem nie bierzemy pod uwag wiodących zer liczby GG, a w przpadku gdy GG = 0, wtedy nie bierzemy również pod uwagę zer wiodących liczby MM.

Przykład
Wejście:
4
00:00
23:30
14:59
23:58

Wyjście:
00:01
23:32
15:51
00:00
"""

t = int(input())
for x in range(t):
    czas = input().split(':')
    if czas[0] == czas[1][::-1]:
        pom = int(czas[1])
        pom += 1
        if pom < 10:
            minuta = f'0{pom}'
        else:
            minuta = str(pom)
        print(f'{czas[0]}:{minuta}')
        continue

    godzina = int(czas[0])
    minuta = int(czas[1])

    while True:
        h = str(godzina)
        m = str(minuta)
        if godzina < 10:
            h = '0' + str(godzina)
        if minuta < 10:
            m = '0' + str(minuta)

        minuta += 1
        if minuta == 60:
            minuta = 0
            godzina += 1
        if godzina > 23:
            godzina = 0

        if str(h) == str(m)[::-1]:
            print(f'{h}:{m}')
            break
