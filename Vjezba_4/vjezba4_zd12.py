#vjezba4_zd12 Karlo Hasnek 08/11/2022

print("Program za racunanje aritmeticke sredine svih unesenih znamenaka")
niz = input("unesite niz brojeva: ")
niz_length = len(niz)
suma = 0
for i in range(niz_length):
    suma = suma + int(niz[i])
print("Aritmetička sredina zadanog niza je: ", suma/niz_length)