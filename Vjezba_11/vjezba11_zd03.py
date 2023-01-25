#vjezba11_zd3 Karlo Hasnek 16/01/2023
f = open('./ulaz.txt', 'r', encoding="utf8")
f2 = open('./izlaz.txt', 'w', encoding="utf8")

l = []
for i in f:
    l.append(i)

l.sort(key=lambda x: x.split()[-1])

br = 1
for i in l:
    f2.writelines(f'{br}. {i}')
    br += 1

f.close()
f2.close()
