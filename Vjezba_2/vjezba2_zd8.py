#vjezba2_zd8 Karlo Hasnek 25/10/2022

'''8. Napišite program vjezba2_zd08.py koji od korisnika traži unos troznamenkastog cijelog broja
i potom u tri odvojena retka ispisuje pojedinačne znamenke ovog broja. Npr. za unos broja
426 ispisuje:
4
2
6'''

unos = int(input("Unesite troznamenkasti broj: "))
a, o = divmod(unos, 100)
b, c = divmod(o, 10)
print("%d\n%d\n%d" %(a,b,c))
