#vjezba4_zd8 Karlo Hasnek 08/11/2022

even = []
odd = []
n = int(input("Unesite broj veci od 1: "))
for i in range(n//2):
    even.append(2*(i+1))
    odd.append(2*i+1)
if n % 2 == 1:
    arr = even+odd+[n]
else:
    arr = even+odd
arr.sort()
print(arr)
