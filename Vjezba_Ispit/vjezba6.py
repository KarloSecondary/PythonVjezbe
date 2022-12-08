l = []
for i in range(10):
    print(' '.join(l))
    l.clear()
    for j in range(10):
        if i != j:
            l.append("%d%d" % (i, j))
        if i == j:
            l.append(str(i)+str(j))
        if (i and j) == 9:
            print(' '.join(l))