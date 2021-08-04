"""
Napisz program, który sprawdza, czy dany formularz osobowy został prawidłowo wypełniony. Formularze, których poprawność należy sprawdzić, mają postać:

Imie: II; Nazwisko: NN; Data ur.: RRRR-MM-DD

gdzie II jest napisem złożonym z co najwyżej 10 znaków, NN jest napisem złożonym z co najwyżej 20 znaków, RRRR jest 4-znakowym napisem, a MM i DD są 2-znakowymi napisami.

Wejście
Na wejście programu podana zostanie pewna nieokreślona liczba zestawów danych. Każdy z zestawów składa się z 3 rozdzielonych średnikiem napisów, o postaci opisanej powyżej (można przyjąć, że pola II, NN, RRRR, MM i DD składają się wyłącznie z czarnych znaków różnych od średnika). Poszczególne zestawy zostaną rozdzielone znakiem nowej linii.

Wyjście
Na wyjściu ma się pojawić ciąg liczbowy, którego i-ty wyraz jest równy:

0, jeżeli i-ty wczytany z wejścia formularz nie zawiera poprawnego imienia; poprawne imiona zaczynają się od wielkiej litery, po której mogą nastąpić małe litery;
1, jeżeli i-ty wczytany z wejścia formularz zawiera poprawne imię, a nie zawiera poprawnego nazwiska; poprawne nazwiska zaczynają się od wielkiej litery, po której następują małe litery;
2, jeżeli i-ty wczytany z wejścia formularz zawiera poprawne imię i nazwisko, a nie zawiera poprawnej daty; w poprawnej dacie pole RRRR jest liczbą całkowitą z zakresu 1900-2000, pole MM jest liczbą całkowitą z zakresu 1-12, a pole DD liczbą całkowitą z zakresu 1-31;
3, w pozostałych przypadkach.
Poszczególne elementy tego ciągu należy rozdzielić znakiem nowej linii.

Przykład
Wejście:
Imie: Roman; Nazwisko: Kowalski6; Data ur.: 1900-01-30
Imie: Andrzej; Nazwisko: Kowal; Data ur.: 1899-10-10
Imie: roman; Nazwisko: No-wak; Data ur.: 1099-11-12
Imie: Alicja; Nazwisko: Nowak; Data ur.: 1990-01-01

Wyjście:
1
2
0
3
"""


def walidacja_imie(imie):
    flaga = True

    if imie[0] == ' ':
        imie = imie[1:]

    if ord(imie[0]) > 64 and ord(imie[0]) < 91:
        imie = imie[1:]
    else:
        return False

    for litera in imie:
        if ord(litera) > 96 and ord(litera) < 123:
            continue
        else:
            flaga = False

    return flaga


def walidacja_data(data):
    if len(data) == 11:
        pass
    else:
        return False
    if data[0] == ' ':
        data = data[1:]

    dane = data.split('-')

    try:
        rok = int(dane[0])
    except:
        return False
    try:
        miesiac = int(dane[1])
    except:
        return False
    try:
        dzien = int(dane[2])
    except:
        return False

    if rok < 1900 or rok > 2000:
        return False
    if miesiac < 1 or miesiac > 12:
        return False
    if dzien < 1 or dzien > 31:
        return False

    return True


while True:
    try:
        dane = input().split(';')
        imie_ = dane[0]
        nazwisko_ = dane[1]
        data_ = dane[2]

        imie = imie_.split(':')
        imie = imie[1]

        nazwisko = nazwisko_.split(':')
        nazwisko = nazwisko[1]

        data = data_.split(':')
        data = data[1]

        val_imie = walidacja_imie(imie)
        val_nazwisko = walidacja_imie(nazwisko)
        val_data = walidacja_data(data)

        if not val_imie:
            print("0")
        elif val_imie and not val_nazwisko:
            print("1")
        elif val_imie and val_nazwisko and not val_data:
            print("2")
        else:
            print("3")



    except:
        break

# Imie: Roman; Nazwisko: Kowalski6; Data ur.: 1900-01-30
# Imie: Andrzej; Nazwisko: Kowal; Data ur.: 1899-10-10
# Imie: roman; Nazwisko: No-wak; Data ur.: 1099-11-12
# Imie: Alicja; Nazwisko: Nowak; Data ur.: 1990-01-01
