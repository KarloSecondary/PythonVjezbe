#vjezba5_zd12 Karlo Hasnek 18/11/2022

print("Kalkulator aritmeticke sredine. Radi sve do unosa negativnog broja!")
n = 1
br = 0
suma = 0
while n > 0:
    n = int(input("unesite broj: "))
    if n > 0:
        br += 1
        suma = suma+n
ar = round(suma/br, 2)
print("Aritmeticka sredina unesenih brojeva iznosi:", ar)
