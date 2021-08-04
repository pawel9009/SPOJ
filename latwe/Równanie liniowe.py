"""
Równanie liniowe jest postaci ax+b=c, gdzie a, b, c są liczbami rzeczywistymi. Niewiadomą jest x, która również jest liczbą rzeczywistą. Równanie to może mieć jedno rozwiązanie, brak rozwiązań lub nieskończenie wiele rozwiązań.

Input
W pojedyńczej linii podane są trzy liczby rzeczywiste zaokrąglone do drugiego miejsca po przecinku.

Output
Rozwiązaniem problemu jest liczba rzeczywista zaokrąglona do drugiego miejsca po przecinku w przypadku, gdy równanie liniowe ax+b=c posiada rozwiązanie. W przypadku braku rozwiązania powinien zostać wydrukowany napis BR, a w przypadku nieskończenie wielu rozwiązań napis NWR

Example 1
Input:
0.52 1.60 -5.44

Output:
-13.54


Example 2
Input:
0.00 2.00 3.00

Output:
BR


Example 3
Input:
0.00 2.00 2.00

Output:
NWR
"""
dane = input().split(' ')
a = float(dane[0])
b = float(dane[1])
c = float(dane[2])

b -= c

if a == 0 and b != 0:
    print("BR")
elif a == 0 and b == 0:
    print("NWR")
elif a != 0:
    x = -b / a
    print("%.2f" % x)
elif a == 0:
    x = b
    print(x.__round__(2))
