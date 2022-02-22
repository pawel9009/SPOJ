"""
Mały Jasio znalazł pudełko z patyczkami. Postanowił z nich budować trójkąty równoboczne. Na każdy taki trójkąt zużywał trzy patyczki o jednakowej długości, nie łamiąc ich, ani nie łącząc. Napisz program, który wczyta długości patyczków i wyznaczy największą liczbę trójkątów jakie można zbudować, przy założeniu, że każdy patyczek można wykorzystać tylko raz.

Wejście
W pierwszym i jedynym wierszu wejścia znajduje się jedna liczba całkowita n nie większa od 1024 oznaczająca liczbę patyczków. W wierszu drugim znajduje się n liczb całkowitych dodatnich nie większych od 256, oznaczających długości patyczków.

Wyjście
Pierwszy i jedyny wiersz wyjścia powinien zawierać jedną wartość - liczbę trójkątów jakie można zbudować z patyczków o długościach podanych na wejściu.

Przykład
Dla danych wejściowych:

12
3 5 3 4 3 3 4 3 3 4 3 3
poprawną odpowiedzią jest:

3
"""
t = int(input())
lista = input().split(' ')
for i,x in enumerate(lista):
    lista[i] = int(x)

i = 0
while len(lista)>2:
    x= lista[0]
    if lista.count(x) >2:
        i+=1
        lista.remove(x)
        lista.remove(x)
        lista.remove(x)
    else:
        lista.pop(0)
print(i)


