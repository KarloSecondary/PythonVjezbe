#vjezba5_zd4 Karlo Hasnek 16/11/2022

niz = str(input("Unesi niz znakova: "))
niz = [*niz]
for i in range(len(niz)):
    if ord(niz[i]) in range(64, 91) or ord(niz[i]) in range(96, 123):
        print(niz[i])