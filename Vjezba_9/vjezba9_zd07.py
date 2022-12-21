#vjezba9_zd7 Karlo Hasnek 20/12/2022
from re import sub

f = open('./ulaz7.txt', 'r')
f2 = open('./izlaz7.txt', 'w')

content = f.read()
cont = ''

result = sub(r'[^0-9]', '', content)

print(result)
for i in range(len(content)):
    for j in range(len(content)):
        if content[i].isnumeric():
            continue

print(cont)

f.close()
f2.close()
