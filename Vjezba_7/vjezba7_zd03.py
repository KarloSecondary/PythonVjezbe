#vjezba7_zd3 Karlo Hasnek 29/11/2022

m = int(input("Unesi prvi cijeli broj: "))
n = int(input("Unesi drugi cijeli broj: "))

if m < n:
    umn = 1
    for i in range(m+1, n):
        umn = umn * i
else:
    print("m je veci ili jednak n!")

print(umn)