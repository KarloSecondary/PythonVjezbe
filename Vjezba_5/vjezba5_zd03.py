#vjezba5_zd3 Karlo Hasnek 16/11/2022

m = int(input("unesi prvi broj: "))
n = int(input("unesi drugi broj: "))
nzd = 0
if m<=0 or n<=0:
    print("Brojevi moraju biti veci od nule.")
else:
    for i in range(1,m+1):
        if n % i == 0 and m % i == 0:
            nzd = i
    print("Najveci zajednici djelitelj je: ",nzd)
