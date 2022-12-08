#vjezba5_zd2 Karlo Hasnek 16/11/2022

a = []
n = int(input("Unesi prirodni broj: "))

if n > 0:
    for i in range(n):
        if n % (i+1) == 0:
            a.append(i+1)

print(a)
if len(a) == 2:
    print("broj je prost i ima %d djelitelja." %(len(a)))
elif len(a) > 2:
    print("broj je slozen i ima %d djelitelja." %(len(a)))
else:
    print("broj 1 nije niti prost niti slozen.")
    