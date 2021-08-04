"""
Często się zdarza, że pisząc stronę internetową piszemy tagi HTMLowe w postaci dużych, a czasami małych liter. Powoduje, że kod strony wygląda nieestetycznie. Twoim zadanie jest napisanie programu, który przerobi wszystkie tagi HTMLowe na duże litery, tzn, wszystkie litery pomiędzy znakami "<" a ">" zamieni na duże litery.

Input
Na wejściu znajduje się fragment kodu HTMLowego.

Output
Na wyjściu znajduje się kod HTML z wejścia, tyle tylko, że wszystkie tagi HTMLowe składają się z dużych liter.

Example
Input:
<html>
<head>
<TITLE>To jest tytul</Title>
</head>
<body>
<b>Cos tam</b>
</body>
</html>


Output:

<HTML>
<HEAD>
<TITLE>To jest tytul</TITLE>
</HEAD>
<BODY>
<B>Cos tam</B>
</BODY>
</HTML>
"""


def tagi(text):
    for a in range(len(text)):
        poczatek = None
        koniec = None
        if text[a] == '<':
            poczatek = a + 1
            for znak in range(a, len(text)):
                if text[znak] == '>':
                    koniec = znak
                    break

            fraza = text[poczatek:koniec].upper()
            text = text[0:poczatek] + fraza + text[koniec:]
        else:
            continue
    return text


while True:
    try:
        wynik = ""
        wejscie = input()

        print(tagi(wejscie))


    except:
        break
