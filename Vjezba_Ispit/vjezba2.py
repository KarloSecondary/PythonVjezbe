l = []
n = int(input("unesi cijeli broj: "))
if n < 0:
    n = -1 * (n)

for i in range(1, n+1):
        if i % 2 == 1:
            if n % i == 0:
                l.append(i)
print(l)