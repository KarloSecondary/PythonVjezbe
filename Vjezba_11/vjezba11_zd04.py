#vjezba11_zd4 Karlo Hasnek 16/01/2023


def povrsina_trokuta(t1, t2, t3):
    p = 0.5 * abs(t1[0]*(t2[1]-t3[1]) + t2[0]*(t3[1]-t1[1]) + t3[0]*(t1[1]-t2[1]))
    if p <= 0:
        print('unesene koordinate nisu valjane.')
    else:
        print(f'povrsina iznosi: {p}')


def main():
    print('Unesite koordinate triju tocaka.')
    x1, y1 = int(input('x1: ')), int(input('y1: '))
    x2, y2 = int(input('x2: ')), int(input('y2: '))
    x3, y3 = int(input('x3: ')), int(input('y3: '))
    t1 = (x1, x2)
    t2 = (x2, y2)
    t3 = (x3, y3)
    return povrsina_trokuta(t1, t2, t3)


main()
