"""
Niedługo święta i najwyższy czas aby przystroić choinkę. Mały Mikołaj właśnie zabiera się za sprawdzenie lampek choinkowych. Posiada on n żarówek koloru zielonego oraz m żarówek koloru czerwonego. Dodatkowo okazało się, że k spośród jego żarówek (niewiadomego koloru) jest przepalonych. Całe szczęście Mikołaj może wykręcić dowolną żarówkę i nie wieszać jej na choince.

Naszemu bohaterowi zależy, aby liczba żarówek jednego i drugiego koloru świecących się na jego choince była identyczna.

Mikołaj zastanawia się, ile maksymalnie żarówek będzie świeciło się na jego choince w najbardziej optymistycznym wariancie?

Wejście
Wejście składa się z trzech liczb naturalnych n, m oraz k (0 ≤ n, m < 1000; 0 ≤ k ≤ n + m) opisanych powyżej.

Wyjście
Na wyjściu należy wypisać maksymalną liczbę żarówek, które będą świeciły się na choince Mikołaja w najbardziej optymistycznym wariancie.

Przykład
Wejście:

5 8 3
Wyjście:

10
Wyjaśnienie do przykładu:

W najbardziej optymistycznym wariancie 3 przepalone żarówki są koloru czerwonego. Mikołaj wykręca je i wiesza na choince 5 żarówek koloru zielonego oraz 5 żarówek koloru czerwonego.
"""
dane = input().split(' ')
n = int(dane[0])
m = int(dane[1])
k = int(dane[2])
while k > 0:
    if n >= m:
        n -= 1
        k -= 1
    elif m >= n:
        m -= 1
        k -= 1

while n != m:
    if n >= m:
        n -= 1
    elif m >= n:
        m -= 1

if n > m:
    n -= 1
elif m > n:
    m -= 1
print(n + m)
