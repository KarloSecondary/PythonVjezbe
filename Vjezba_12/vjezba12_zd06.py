#vjezba12_zd6 Karlo Hasnek 25/01/2023
from random import randint


def izvuci_broj():
    n = randint(1, 10)

    return n


def main():
    print("Pogodite nasumicni broj izmedu 1 i 10.")
    broj = izvuci_broj()
    brojac = 0
    state = True
    while state:
        n = int(input("Unos: "))
        brojac += 1
        if n == 0:
            exit()
        elif n == broj:
            print("Pogodak!")
            print(f'Pogodili ste iz {brojac}. pokusaja!')
            state = False
        elif n != broj:
            print("Nije, pokusajte ponovno.")


main()
