#vjezba9_zd1 Karlo Hasnek 20/12/2022

f = open('./ulaz1.txt', 'r')

content = f.read()
cont = ''

for i in range(len(content)):
    if content[i].isalpha():
        cont += content[i]

print(cont)
f.close()
