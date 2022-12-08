#vjezba4_zd6 Karlo Hasnek 08/11/2022

niz_1 = str(input("Unesite 1. niz znakova: "))
niz_2 = str(input("Unesite 2. niz znakova: "))
location = niz_2.find(niz_1)
duljina_1 = len(niz_1)
visak = location+duljina_1
if niz_1 in niz_2:
    niz_2 = niz_2[visak:]
    print(niz_2)
else:
    print("Prvi niz nije dio drugog niza znakova.")