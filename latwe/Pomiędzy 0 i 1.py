text = input()
if len(text) == 0:
    print("PUSTY")
    exit()
if len(text) < 3:
    exit()
if len(text) > 1000000:
    exit()
ind_0 = None
ind_1 = None
if text.__contains__('0'):
    ind_0 = text.find('0')
    zmiana = text[ind_0 + 1:]
    if zmiana.__contains__('1'):
        reversed = text[:]
        reversed = reversed[::-1]
        ind_1 = reversed.find('1')
        ind_1 = len(text) - ind_1
        print(ind_1)
        print(text[ind_0 + 1:ind_1 - 1])
# for a in range(ind_0+1,ind_1-1):
#     print(text[a])
