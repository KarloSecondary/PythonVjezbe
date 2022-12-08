#vjezba2_zd6 Karlo Hasnek 25/10/2022

'''6. Napišite program vjezba2_zd06.py koji od korisnika traži unos dvaju decimalnih brojeva a i b,
te ispisuje vrijednost količnika brojeva a i b zaokruženu na:
a) 5 decimala
b) 2 decimale
c) cijeli broj'''

a = float(input("Unesite 1. decimalni broj: "))
b = float(input("Unesite 2. decimalni broj: "))

# a)
kolicnik1 = round(a * b, 5)
# b)
kolicnik2 = round(a * b, 2)
# c)
kolicnik3 = int(a * b)

print("a)",kolicnik1,"\nb)",kolicnik2,"\nc)",kolicnik3)
