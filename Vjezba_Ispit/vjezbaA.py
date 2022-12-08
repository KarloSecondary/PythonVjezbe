for i in range(10):
    [i] = []
    print([i])
    for j in range(10):
        for k in range(10):
            [i] = [i].join(str(j)+str(k)+' ')
print([i])