#vjezba2_zd10 Karlo Hasnek 25/10/2022

'''10. Napišite program vjezba2_zd10.py koji od korisnika traži unos peteroznamenkastog cijelog
broja i potom ispisuje zbroj znamenaka ovog broja. Npr. za 43210 ispisuje 10.'''

unos = int(input("unesite peteroznamenkasti broj: "))
a, ostatak1 = divmod(unos, 10000)
b, ostatak2 = divmod(ostatak1, 1000)
c, ostatak3 = divmod(ostatak2, 100)
d, e = divmod(ostatak3, 10)
print("zbroj brojeva unutar zadanog broja iznosi: ",a+b+c+d+e)
