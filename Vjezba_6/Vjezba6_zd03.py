#vjezba6_zd3 Karlo Hasnek 29/11/2022

m = int(input("Unesi prvi prirodni broj: "))
n = int(input("Unesi drugi prirodni broj: "))

for i in range(1, m*n+1):
    if i % m == 0 and i % n == 0:
        print(i)
        break
