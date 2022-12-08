#vjezba5_zd6 Karlo Hasnek 18/11/2022

l = []
kol = int(input("Unesi broj ocjena: "))
br = 0
while br < kol:
    m = int(input("unesi ocjenu od 1 do 5: "))
    l.append(m)
    br += 1
if 1 in l:
    print("Nedovoljan.")
else:
    suma = sum(l)/kol
    print("Prosjek svih ocjena iznosi: ", round(suma, 2))
