#Vježba3_Zadatak4 Karlo Hasnek 31.10.

bodovi = int(input("Unesite broj bodova (od 0 do 100): "))

if bodovi<60 and bodovi>=0:
    print("Nedovoljan!")
elif bodovi>60 and bodovi<70:
    print("Dovoljan!")
elif bodovi>70 and bodovi<80:
    print("Dobar!")
elif bodovi>80 and bodovi<90:
    print("Vrlo dobar!")
elif bodovi>90 and bodovi<=100:
    print("Odličan!")
else:
    print("Broj bodova je krivo unesen")
