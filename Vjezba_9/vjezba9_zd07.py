#vjezba9_zd7 Karlo Hasnek 22/12/2022

f = open('./ulaz7.txt', 'r')
f2 = open('./izlaz7.txt', 'w')
cont_l = []
cont_s = ''

content = f.read()

for i in range(len(content)):
    if content[i] == '0':
        continue
    elif content[i] == '.':
        cont_s += content[i]
    elif content[i].isnumeric():
        cont_s += content[i]
    elif cont_s != '':
        cont_l.append(float(cont_s))
        cont_s = ''

cont_l.append(float(cont_s))
cont_l.sort()
for i in cont_l:
    f2.write(f'{int(i)} ')

print(cont_l)

f.close()
f2.close()
