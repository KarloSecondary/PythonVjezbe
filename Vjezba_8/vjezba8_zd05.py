#vjezba8_zd5 Karlo Hasnek 30/11/2022


def unos_int():
    n = float(input("Unesi cijeli broj: "))
    return int(n)


def prost(n):
    br = 0
    for i in range(1, n+1):
        if n % i == 0:
            br += 1
    if br == 2:
        return True
    else:
        return False


def main():
    if prost(unos_int()):
        print("Uneseni broj je prost.")
    else:
        print("Uneseni broj nije prost.")


main()
