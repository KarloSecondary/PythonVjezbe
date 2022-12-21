#vjezba9_zd6 Karlo Hasnek 20/12/2022

f = open('./ulaz6.txt', 'r')
f2 = open('./izlaz6.txt', 'w')
l1 = []
l2 = []


class Osoba:
    def __init__(self, ime, tezina, visina):
        self.ime = ime
        self.tezina = float(tezina)
        self.visina = float(visina)
        self.itm = round(self.tezina/(self.visina**2), 2)


for i in f:
    i = i.replace(' ', '\n').splitlines()
    i = Osoba(i[0], i[1], i[2])
    l1.append(i)

for i in range(len(l1)):
    l2.append(l1[i].itm)
    l2.sort()

for i in range(len(l2)):
    for j in l1:
        if l2[i] == j.itm:
            f2.write(f'{j.ime} {l2[i]}\n')

f.close()
f2.close()
