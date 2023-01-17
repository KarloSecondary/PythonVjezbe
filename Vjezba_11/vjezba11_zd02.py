#vjezba11_zd2 Karlo Hasnek 16/01/2023

svi_samoglasnici = 'aeiou'


def samoglasnici(s):
    br = 0
    for i in s:
        if i in svi_samoglasnici:
            br += 1

    print(f'U zadanom stringu "{s}" ima {br} samoglasnika sto cini {round(br/len(s)*100, 2)}%')


def main():
    s = input('unesite proizvolnjni string: ')

    return samoglasnici(s)


main()
