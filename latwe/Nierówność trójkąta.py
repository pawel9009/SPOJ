"""
Napisz program, który sprawdza, czy istnieje trójkąt o bokach o podanej długości.

Wejście
Na wejście programu podana zostanie pewna nieokreślona liczba zestawów danych. Każdy z zestawów składa się z 3 liczb rozdzielonych spacjami. Poszczególne zestawy zostaną rozdzielone znakiem nowej linii.

Wyjście
Na wyjściu ma się pojawić ciąg binarny, którego i-ty wyraz jest równy 1, jeżeli istnieje trójkąt o długościach boków podanych w i-tym wczytanym z wejścia zestawie. Poszczególne elementy tego ciągu należy rozdzielić znakiem nowej linii.

Przykład
Wejście:
1.2 1.2 1.2
1.5 2.5 3.5
-1.5 6.0 4.5
2 4 8

Wyjście:
1
1
0
0


"""
while True:
    try:
        dane = input().split(' ')
        a = float(dane[0])
        b = float(dane[1])
        c = float(dane[2])
        tab = [a, b, c]
        if a > 0 and b > 0 and c > 0:
            maks = max(tab)
            tab.remove(maks)
            if maks < tab[0] + tab[1]:
                print("1")
            else:
                print("0")
        else:
            print("0")
    except:
        break
