def f(num):
    if num == 1: return 1
    return num * f(num - 1)


t = int(input())
if t < 1 and t > 100:
    exit()

tab = []
for x in range(t):
    tab.append(int(input()))

for a in tab:
    print(f(a))
