#vjezba12_zd3 Karlo Hasnek 24/01/2023

f = open('./kalorije.txt', 'r')
f2 = open('./sortirana_lista.txt', 'w')
l = []
for i in f:
    l.append(i.split())

l2 = sorted(l, key=lambda x: int(x[1]))
l2.reverse()

for i in l2:
    f2.write(f'{i[0]} {i[1]}\n')

f.close()
f2.close()
