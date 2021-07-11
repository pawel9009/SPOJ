t = int(input())
for x in range(t):
    dane = input().split(' ')
    a = int(dane[0])
    b = int(dane[1])
    wynik = None
    flaga = True
    while flaga:
        if a-b>0 or b-a>0:
            if a>b:
                a=a-b
            else:
                b=b-a
        else:
            flaga = False
            wynik=a+b

    print(wynik)