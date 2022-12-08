#vjezba5_zd8 Karlo Hasnek 18/11/2022

print("Program za pretvorbu broja sa bazom 5 u broj sa bazom 10.")
print("NAPOMENA! Svi uneseni brojevi moraju biti izmedu 0-4.")
n = int(input("Unesi broj: "))
l1 = [int(n) for n in str(n)]
if (5 or 6 or 7 or 8 or 9) in l1:
    print("Unesen je broj veci od 4!")
else:
    l1.reverse()
    l2 = []
    for i in range(len(l1)):
        l2.append(l1[i]*(5**i))
    print("Broj %d po bazi 5 iznosi: %d po bazi 10." %(n, sum(l2)))

