#vjezba8_zd1 Karlo Hasnek 30/11/2022
from math import sqrt

#a)
print("Funkcija za zbrajanje dva broja.")
a = int(input("unesi prvi broj: "))
b = int(input("unesi drugi broj: "))


def zbroj(a, b):
    c = a + b
    return c


print(f'Zbroj brojeva {a} i {b} iznosi: {zbroj(a, b)}')


#b)
print("\nFunkcija za zbroj znamenaka unutar jednog broja")
n = int(input("Unesi cijeli broj: "))


def zbroj_znamenaka(n):
    n = [int(n) for n in str(n)]
    s = sum(n)
    return s


print(f'Zbroj znamenaka unutar broja {n} iznosi: {zbroj_znamenaka(n)}')

#c)
print("\nFunkcija za racunanje udaljenosti koordinate od ishodista koordinatnog sustava.")
x = int(input("unesi x koordinatu: "))
y = int(input("unesi y koordinatu: "))


def udaljenost_od_0(x, y):
    d = sqrt(x**2+y**2)
    return d


print(f'udaljenosti koordinata {x, y} od ishodista koordinatnog sustava iznosi: {round(udaljenost_od_0(x, y), 2)}')

#d)
print("\nFunkcija za racunanje udaljenosti izmedu dvije tocke unutar koordinatnog sustava.")
x1 = int(input("unesi x1 koordinatu: "))
y1 = int(input("unesi y1 koordinatu: "))
x2 = int(input("unesi x2 koordinatu: "))
y2 = int(input("unesi y2 koordinatu: "))


def udaljenost_tocaka(x1, y1, x2, y2):
    dT = sqrt((x1-x2)**2+(y1-y2)**2)
    return dT


print(f'udaljenosti tocaka {x1, y1} i {x2, y2} iznosi: {round(udaljenost_tocaka(x1, y1, x2, y2), 2)}')
