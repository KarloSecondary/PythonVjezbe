#vjezba9_zd2 Karlo Hasnek 20/12/2022

f = open('./ulaz2.txt', 'r')

lista = []
dupli = []

for i in f:
    for j in i:
        if j not in lista:
            lista.append(j)
        elif j not in dupli:
            dupli.append(j)

print(''.join(dupli))

f.close()
