#vjezba12_zd4 Karlo Hasnek 25/01/2023


def projekcija_na_os_x(T):
    Tx = (T[0], 0)

    return Tx


def main():
    x, y = int(input("Unesi x koordinatu: ")), int(input("Unesi y koordinatu: "))
    T = (x, y)

    print(projekcija_na_os_x(T))


main()
