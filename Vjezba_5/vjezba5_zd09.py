#vjezba5_zd9 Karlo Hasnek 18/11/2022

m = int(input("unesi prvi broj (manji): "))
n = int(input("unesi drugi broj (veci): "))
l = []
for i in range(m, n):
    num = [int(i) for i in str(i)]
    if sum(num) == 10:
        l.append(i)
print("Brojevi kojima je zbroj znamenaka jednak 10:\n", l)
