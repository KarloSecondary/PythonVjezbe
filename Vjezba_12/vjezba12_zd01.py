#vjezba12_zd1 Karlo Hasnek 24/01/2023
from random import randint

l = []
maks = 0
n = int(input("Veci od 0: "))
if n > 0:
    for i in range(n):
        suma = 0
        lista = []
        for j in range(5):
            lista.append(randint(0, 10))
        l.append(lista)
        suma = sum(lista)

najveca = []
for j in range(len(l)):
    suma = sum(l[j])
    l2 = l[j]

    if suma > maks:
        maks = suma
        najveca = l[j]

print(maks)
print(najveca)