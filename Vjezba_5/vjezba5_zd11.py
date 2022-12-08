#vjezba5_zd11 Karlo Hasnek 18/11/2022

niz = str(input("Unesite proizvoljan niz znakova: "))
niz = [*niz]
ascii_niz = [(ord(niz[i]))+1 for i in range(len(niz))]
ascii_niz = ''.join([chr(ascii_niz[i]) for i in range(len(ascii_niz))])
print(" šifrirana zadani niz znakova:", ascii_niz)
