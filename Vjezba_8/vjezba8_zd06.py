#vjezba8_zd6 Karlo Hasnek 30/11/2022

def unos_broja_u_listu(l):
    n = input("Unesi realan broj: ")
    if n:
        try:
            n = int(n)
            l.append(n)
        except ValueError:
            try:
                n = float(n)
                l.append(n)
            except ValueError:
                return l
    else:
        pass


def max_element(l):
    if len(l) > 0:
        maks = max(l)
        return maks
    else:
        pass


def main():
    l = []
    br = -1
    while len(l) > br:
        unos_broja_u_listu(l)
        br += 1
    else:
        print(max_element(l))
        print(l)


main()
