#vjezba7_zd5 Karlo Hasnek 29/11/2022

s = str(input("Unesi niz znakova: "))
l = [*s]
l.sort()
l2 = []
print(l)
for i in l:
    if ord(i) in range(65, 91) or ord(i) in range(97, 123):
        l2.append(i)
    else:
        continue

print(l2)
