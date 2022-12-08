#vjezba7_zd2 Karlo Hasnek 29/11/2022

k = int(input("Unesi prirodni broj: "))

if k > 0:
    br = 0
    l = []
    for i in range(1, k**2):
        if br == k:
            break
        else:
            if i % 2 == 0:
                if i % 3 == 0 or i % 5 == 0:
                    l.append(i)
                    br += 1

s = ''.join(str(i) for i in l)
print(s)
