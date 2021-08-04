t = int(input())
for x in range(t):
    czas = input().split(':')
    if czas[0] == czas[1][::-1]:
        pom = int(czas[1])
        pom += 1
        if pom < 10:
            minuta = f'0{pom}'
        else:
            minuta = str(pom)
        print(f'{czas[0]}:{minuta}')
        continue

    godzina = int(czas[0])
    minuta = int(czas[1])

    while True:
        h = str(godzina)
        m = str(minuta)
        if godzina < 10:
            h = '0' + str(godzina)
        if minuta < 10:
            m = '0' + str(minuta)

        minuta += 1
        if minuta == 60:
            minuta = 0
            godzina += 1
        if godzina > 23:
            godzina = 0

        if str(h) == str(m)[::-1]:
            print(f'{h}:{m}')
            break
