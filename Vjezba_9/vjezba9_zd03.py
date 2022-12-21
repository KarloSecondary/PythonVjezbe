#vjezba9_zd3 Karlo Hasnek 20/12/2022

f = open('./ulaz3.txt', 'r', encoding="utf8")
f2 = open('./izlaz3.txt', 'w', encoding="utf8")

linije = f.readlines()
br = 1

for i in linije:
    f2.write(f'{str(br)}. {i}')
    br += 1

print(f2)

f.close()
f2.close()
