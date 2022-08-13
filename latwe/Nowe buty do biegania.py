"""
Janek marzy o zakupie nowych butów do biegania. W obecnych przebiegł już k kilometrów. Eksperci uważają, że buty do biegania należy wymienić nie wcześniej niż po przebiegnięciu 300 mil i nie później niż po przebiegnięciu 500 mil. 1 mila jest równa 1.609344 kilometra.

Rodzice Janka znają opinie ekspertów i na prośbę syna o zakup nowych butów do biegania zawsze udzielają 1 z 3 odpowiedzi:

NIE - jeżeli wartość k podana w milach zawiera się w przedziale [0, 300).
SPRAWDZIMY TWOJE OBECNE BUTY - jeżeli wartość k podana w milach zawiera się w przedziale [300, 500).
TAK - jeżeli wartość k podana w milach zawiera się w przedziale [500, ∞].
Jaka będzie odpowiedź rodziców, jeżeli Janek poprosi ich teraz o zakup nowych butów?

Wejście
W pierwszej i jedynej linii wejścia znajdują się liczba całkowita k ∈ [0, 1000] określająca dystans w kilometrach jaki Janek przebiegł w obecnych butach.

Wyjście
Na wyjściu należy wypisać, jaka będzie odpowiedź rodziców, jeżeli Janek poprosi ich teraz o zakup nowych butów.

Przykład 1:
Wejście:

482
Wyjście:

NIE
Wyjaśnienie do przykładu:

482 kilometry to w przybliżeniu 299,501 mil.

Przykład 2:
Wejście:

483
Wyjście:

SPRAWDZIMY TWOJE OBECNE BUTY
Wyjaśnienie do przykładu:

483 kilometry to w przybliżeniu 300,122 mil.

Przykład 3:
Wejście:

1000
Wyjście:

TAK
"""
while True:
    try:
        n = int(input())
        mile = n / 1.609344
        if mile < 300.0:
            print("NIE")
        elif mile < 500:
            print('SPRAWDZIMY TWOJE OBECNE BUTY')
        else:
            print("TAK")
    except Exception:
        break

