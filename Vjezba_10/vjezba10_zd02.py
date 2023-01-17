#vjezba10_zd2 Karlo Hasnek 09/01/2023
from turtle import *


def kvadrat(duljina):
    ht()
    pu()
    goto(-duljina//2, -duljina//2)
    pd()

    for i in range(4):
        fd(duljina)
        lt(90)

    Screen().exitonclick()


def main():
    duljina = int(textinput("Unos Duljine", 'Unesite duljinu stranice'))
    if duljina <= 0:
        write('Unesena duljina nije valjana. Pokrenite program ponovno.')
        Screen().exitonclick()
    else:
        return kvadrat(duljina)


main()
