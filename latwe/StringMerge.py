"""
Napisz funkcję:

char* string_merge(char *, char *);
która sklei ze sobą dwa łańcuchy biorąc na przemian po jednym znaku z każdego łańcucha i umieści w nowej dynamicznie alokowanej tablicy znaków, do której zwróci wskaźnik. Należy wziąć po tyle znaków ile jest w krótszym łańcuchu.

Input


W pierwszej linii liczba testów t, w kolejnych liniach po dwa łańcuchy znaków odzielone spacją.

Output
W każdej linii jeden łańcuch, wynik działania funkcji string_merge.

Example
Input:
4
a bb
abs sfd
ewr w
wqeqweqweq eqweqwe
Output:
ab
asbfsd
ew
weqqewqewqewqe

"""

def string_merge(a,b):
    dl_a = len(a)
    dl_b = len(b)
    dlugosc = 0
    if dl_a>dl_b:
        dlugosc=dl_b
    else:
        dlugosc=dl_a
    wynik = ""
    for q in range(dlugosc):
        wynik+=a[q]
        wynik+=b[q]
    return wynik

t = int(input())
for x in range(t):
    zmienne = input().split()
    a =zmienne[0]
    b = zmienne[1]
    print(string_merge(a,b))
