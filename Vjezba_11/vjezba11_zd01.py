#vjezba11_zd1 Karlo Hasnek 16/01/2023
from random import randint

l = []
n = int(input('Unesite broj veci od 0: '))
if n > 0:
    for i in range(n):
        l.append(randint(1, 100))

p = 0
nep = 0
for i in l:
    if i%2 == 0:
        p += 1
    else:
        nep += 1

print(l)
print(f'broj parnih: {p}, broj neparnih: {nep}')
