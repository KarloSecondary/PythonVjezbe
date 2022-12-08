#vjezba4_zd7 Karlo Hasnek 08/11/2022

n = int(input("Unesite broj veci od 1: "))
if n > 1:
    a = []
    for i in range(n):
        a.append(i+1)
    print(a)
    b = []
    for i in range(n):
        b.append(2*(i+1))
    b.reverse()
    print(b)
else:
    print("Uneseni broj je manji od 1.")
