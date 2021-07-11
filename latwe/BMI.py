"""

FR_02_06 - BMI


Wskaźnik masy ciałaNa lekcji biologii klasa Bajtka uczyła się o wskaźniku masy ciała, tzw. BMI, który klasyfikuje daną osobę w jednym z zakresów wartości: niedowadze, wartości prawidłowej oraz nadwadze. Pani od biologii podała klasie wzór:BMI=masa[kg]/(wzrost)^2[m^2]
Wskaźnik masy ciała

Na lekcji biologii klasa Bajtka uczyła się o wskaźniku masy ciała, tzw. BMI, który klasyfikuje daną osobę w jednym z zakresów wartości: niedowadze, wartości prawidłowej oraz nadwadze. Pani od biologii podała klasie wzór:

BMI=masa[kg]/(wzrost)^2[m^2]

Natomiast zakres wygląda następująco:

< 18,5 – niedowaga

[18,5; 25) – wartość prawidłowa

≥ 25,0 – nadwaga

Klasyfikacja ta nie może być stosowana u dzieci, więc Bajtek nie może wyliczyć wartości dla siebie. Postanowił więc, że napisze program, który określi w jakim zakresie znajduje się badana osoba, a Ty jako dobry kolega Bajkta, mu w tym pomożesz. Bajtek zebrał chętnych, którzy podali mu swoje dane.



Wejście
W pierwszym wierszu jedna liczba t (1 ≤ t ≤ 100) określająca ilość badanych osób. W kolejnych t wierszach - imię, masa i wzrost osoby podane odpowiednio w kilogramach i centymetrach (imię - maksymalnie 20 znaków, masa i wzrost to wartości naturalne dodatnie nie przekraczające 200).

Wyjście
Napis: "niedowaga", następnie w osobnych liniach wypisane imiona osób z tej grupy, podobnie z grupami: "wartosc prawidlowa" oraz "nadwaga". Dane osób wypisujemy w kolejności wczytania. Wstawienie znaku końca linii po każdej grupie jest opcjonalny.

Przykład
Wejście:
5
Ala 50 173
Beata 70 190
Boleslaw 100 180
Wincent 85 186
Hiacynta 62 164

Wyjście:
niedowaga
Ala

wartosc prawidlowa
Beata
Wincent
Hiacynta

nadwaga
Boleslaw
"""
def BMI(waga, wzrost):
    wz = wzrost / 100
    bmi = waga / (wz * wz)
    return bmi


niedowaga = []
prawidlowa = []
nadwaga = []
t = int(input())
for x in range(t):
    imie, waga, wzrost = input().split(' ')
    waga = float(waga)
    wzrost = float(wzrost)
    b = BMI(waga, wzrost)
    if b < 18.5:
        niedowaga.append(imie)
    elif b < 25:
        prawidlowa.append(imie)
    else:
        nadwaga.append(imie)
print("niedowaga")
for x in niedowaga:
    print(x)
print("wartosc prawidlowa")
for x in prawidlowa:
    print(x)
print("nadwaga")
for x in nadwaga:
    print(x)
