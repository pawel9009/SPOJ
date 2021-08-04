"""
W celu zaoszczędzenia ilości znaków w krótkich wiadomościach tekstowych (SMS) nie pisze się spacji, a każdy wyraz rozpoczyna się wielką literą. Twoim zadaniem jest otrzymany tekst przerobić zgodnie z powyższym trendem.

Input
Na wejściu znajduje się dowolny tekst bez polskich znaków.

Output
Tekst wprowadzony z wejścia, ale bez spacji. Ponadto każdy wyraz poprzedzony na wejściu spacją zaczyna się wielką literą.

Example
Input:
Dzisiaj jest czwartek,
A jutro bedzie piatek.

Output:
DzisiajJestCzwartek,
AJutroBedziePiatek.
"""

flaga = True
while flaga:
    try:
        text = input()
        a = 0
        while True:
            try:
                licznik = 0
                if text[a] == ' ':
                    for z in range(a, len(text)):
                        if text[z] == ' ':
                            licznik += 1
                        else:
                            break
                    text = text[0:a] + ' ' + text[a + licznik:]
            except:
                break
            a += 1

        spacje = text.count(' ')
        for x in range(len(text) - spacje):
            if text[x] == ' ':
                text = text[0:x] + f'{text[x + 1].upper()}' + text[x + 2:]

        if text[-1] == ' ':
            print(text[:-1])
        else:
            print(text)
    except:
        flaga = False
