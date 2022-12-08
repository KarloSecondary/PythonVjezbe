#Vježba3_Zadatak6 Karlo Hasnek 31.10.

unos = int(input("Unesite neki cijeli broj: "))
baza = int(input("Unesite u kojoj bazi želite ispisati broj (2 = binarni, 8 = oktalni, 16 = heksadecimalni): "))

if baza == 2:
    print(bin(unos))
elif baza == 8:
    print(oct(unos))
elif baza == 16:
    print(hex(unos))
else:
    print("Baza nije pravilno zadana")
