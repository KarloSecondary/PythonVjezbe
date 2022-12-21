#vjezba9_zd4 Karlo Hasnek 20/12/2022

f = open('./ulaz4.txt', 'r')
f2 = open('./izlaz4.txt', 'w')

for i in f:
    izraz = i.split(' ')
    if izraz[1] == '+':
        vrijednost = float(izraz[0]) + float(izraz[2])
        f2.write(f'{str(vrijednost)}\n')
    elif izraz[1] == '-':
        vrijednost = float(izraz[0]) - float(izraz[2])
        f2.write(f'{str(vrijednost)}\n')
    elif izraz[1] == '*':
        vrijednost = float(izraz[0]) * float(izraz[2])
        f2.write(f'{str(vrijednost)}\n')
    elif izraz[1] == '/':
        vrijednost = float(izraz[0]) / float(izraz[2])
        f2.write(f'{str(vrijednost)}\n')
    else:
        print("Greška prilikom unosa. Pokušajte ponovno.")

f.close()
f2.close()
