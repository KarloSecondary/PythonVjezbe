#vjezba6_zd5 Karlo Hasnek 29/11/2022

s = str(input("Unesi niz znakova: "))
l = [*s]
print(l)
l.pop()
l.append("+")
l.sort()
s = ''.join(l)
print(s)
