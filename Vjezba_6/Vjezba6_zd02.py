#vjezba6_zd2 Karlo Hasnek 29/11/2022

n = int(input("Unesi prirodni broj: "))

if n > 0:
    br = 0
    for i in range(1, n*2):
        if br == n:
            break
        else:
            if i % 2 == 0 or i % 3 == 0:
                print(i)
                br += 1

