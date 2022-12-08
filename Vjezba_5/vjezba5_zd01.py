#vjezba5_zd1 Karlo Hasnek 15/11/2022


n = int(input('Unesite prirodni broj: '))

#a)
niz1 = []
if n > 0 :
    for i in range(n):
        niz1.append(i+1)
print('prvih %d prirodnih brojeva' %(n), *niz1, sep=' ')

#b)
niz2 = []
if n > 0 :
    for i in range(n):
        niz2.append((2*(i+1))-1)
print('prvih %d neparnih prirodnih brojeva' %(n), *niz2, sep=' ')

#c)
fakt = 1
if n > 0 :
    for i in range(n):
        fakt = fakt*(i+1)
print('Faktorijela od broja %d iznosi: ' %(n), fakt)

#d)
niz3 = []
if n % 2 == 1:
    for i in range(n // 2):
        niz3.append(2 * i + 1)
    niz3.append(n)
    print("Svi neparni brojevi do %d: " %(n), niz3)
else:
    for i in range(n // 2):
        niz3.append(2 * (i + 1))
    print("Svi parni brojevi do %d: " % (n), niz3)