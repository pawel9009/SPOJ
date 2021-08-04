def silnia(n):
    if n == 0:
        return 1
    for x in range(n - 1, 1, -1):
        n *= x
    return n


t = int(input())
for x in range(t):
    dane = input().split(' ')
    n = int(dane[0])
    k = int(dane[1])
    print(int(silnia(n) / (silnia(k) * silnia(n - k))))
