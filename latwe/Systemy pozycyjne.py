def zamien(x):
    znak = ''
    if x>=0 and x<10:
        znak=f'{x}'
    elif x==10:
        znak='A'
    elif x==11:
        znak= 'B'
    elif x==12:
        znak= 'C'
    elif x==13:
        znak= 'D'
    elif x==14:
        znak= 'E'
    elif x==15:
        znak= 'F'
    return znak

def hex(n):
    wynik = ""
    while n>0:
        reszta = n%16
        wynik+=zamien(int(reszta))
        n//=16
    return wynik[::-1]

def to_11(n):
    wynik = ""
    while n>0:
        reszta = n%11
        wynik+=zamien(int(reszta))
        n//=11
    return wynik[::-1]

t = int(input())
for x in range(t):
    n = int(input())
    print(hex(n), to_11(n))
