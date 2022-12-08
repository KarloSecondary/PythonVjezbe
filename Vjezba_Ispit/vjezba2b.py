l = []
n = int(input("unesi cijeli broj: "))
djelitelj = n % i == 0
if n < 0:
    n = -1*n
if n == 0:
    print("Nema djelitelja.")
for i in range(1, n+1):
    if i % 2 == 1 and djelitelj:
        l.append(-i)
    if i % 2 == 0 and djelitelj:
        l.append(i)
l.sort()
print(l)