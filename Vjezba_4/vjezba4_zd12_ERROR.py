#vjezba4_zd12 Karlo Hasnek 08/11/2022

print("Program za racunanje aritmeticke sredine svih unesenih znamenaka")
niz = int(input("unesite niz brojeva: "))
niz_length = len(str(niz))
suma = 0
for i in range(niz_length):
    suma = suma + int(niz[i])
print("Aritmetička sredina zadanog niza iznosi: ", suma/niz_length)