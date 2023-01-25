#vjezba11_zd6 Karlo Hasnek 24/01/2023
from random import randint
from time import sleep


def izvlacenje_brojeva():
    lista2 = []
    state = True
    while state:
        n = randint(1, 39)
        if n in lista2:
            continue
        else:
            lista2.append(n)
        if len(lista2) == 7:
            state = False
    print(lista2)

    return lista2


def usporedi(lista1, lista2):
    br = set(lista1) & set(lista2)
    broj_pogodenih = len(br)
    if broj_pogodenih == 7:
        print("JACKPOT!")
    else:
        print(f'broj pogodenih: {broj_pogodenih}')


def main():
    print("Loto 7/39".center(60, '-'))
    print("pravila:\nunesite 7 brojeva izmedu 1 i 39\nunosom broja 0 izlazite iz programa\nzabavite se!")
    print("-"*60)
    lista = []
    state = True
    while state:
        n = int(input("Unesite broj: "))
        if n == 0:
            exit()
        elif n in lista:
            print(f' Broj {n} je vec unesen, probajte ponovno.')
        else:
            lista.append(n)
        if len(lista) == 7:
            state = False

    print(f'Vaši brojevi su: {lista}')
    print("Izvuceni brojevi su...")
    sleep(2)
    usporedi(lista, izvlacenje_brojeva())


main()
