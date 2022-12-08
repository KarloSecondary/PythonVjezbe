#vjezba2_zd5 Karlo Hasnek 25/10/2022

'''Napišite program vjezba2_zd05.py koji od korisnika traži unos vremena u sekundama (unos
treba biti cijeli broj), a ispisuje odgovarajuće vrijeme u danima, satima, minutama i
sekundama (npr. 184713 sekunda = 2 dana, 3 sata, 18 minuta i 33 sekunde). Za izračun
koristite funkciju divmod(var_1, var_2) koja vraća dvije vrijednosti: rezultat cjelobrojnog
dijeljenja ulaznih varijabli var_1 i var_2 i ostatak pri dijeljenju ulaznih varijabli. Opiši funkciju
divmod pomoću operatora // i %.'''


unos = int(input("Vrijeme iskazano u sekundama: "))
dani, ostatak1 = divmod(unos, 86400)
sati, ostatak2 = divmod(ostatak1, 3600)
minute, sekunde = divmod(ostatak2, 60)
print("%d sekunda = %d dana, %d sata, %d minuta i %d sekunde" %(unos,dani,sati,minute,sekunde))
