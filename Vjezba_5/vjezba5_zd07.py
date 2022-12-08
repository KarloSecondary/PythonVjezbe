#vjezba5_zd7 Karlo Hasnek 18/11/2022

l = []
n = int(input("unesi dvoznamenkasti broj: "))
if n > 10 or n < 100:
    for i in range(10):
        for j in range(10):
            if (str(i)+str(j)) < str(n):
                if i % 2 == 1 and j % 2 == 1:
                    l.append("%d%d" % (i, j))
    print("svi brojevi sa neparnim znamenkama do unesenog broja:\n", l)
else:
    print("Unesen je broj koji nije dvoznamenkasti.")
