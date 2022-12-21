#vjezba9_zd5 Karlo Hasnek 20/12/2022

f = open('./ulaz5.txt', 'r')
f2 = open('./izlaz5.txt', 'w')
numbers = '0123456789'


def broji_znamenke(string):
    for i in string:
        for j in numbers:
            br_zn = i.count(j)
            rezultat = br_zn / len(i)
            if rezultat == 0.0:
                continue
            else:
                f2.write(f'{j} ==> {round(rezultat, 2)}\n')


broji_znamenke(f)

f.close()
f2.close()
