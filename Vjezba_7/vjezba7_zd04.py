#vjezba7_zd4 Karlo Hasnek 29/11/2022

s = str(input("Unesi niz znakova: "))
s = s.lower()
print(s)
l1 = [*s]
l2 = []
for i in l1:
    if i == 'š':
        i = 's'
        l2.append(i)
    elif i == 'đ':
        i = 'd'
        l2.append(i)
    elif i == 'č' or i == 'ć':
        i = 'c'
        l2.append(i)
    elif i == 'ž':
        i = 'z'
        l2.append(i)
    else:
        l2.append(i)

s2 = ''.join(l2)
print(s2)
