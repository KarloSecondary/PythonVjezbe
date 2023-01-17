#vjezba11_zd3 Karlo Hasnek 16/01/2023

f = open('./ulaz.txt', 'r', encoding="utf8")
f2 = open('./izlaz.txt', 'w', encoding="utf8")

l1 = []
l2 = []
l3 = []

class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime


for i in f:
    i = i.replace(' ', '\n').splitlines()
    i = Osoba(i[0], i[1])
    l1.append(i)

for i in range(len(l1)):
    l2.append(l1[i].prezime)
    l3.append(l1[i].ime)

l2.sort()
for i in l2:



f.close()
f2.close()
