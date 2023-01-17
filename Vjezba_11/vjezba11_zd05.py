#vjezba11_zd5 Karlo Hasnek 16/01/2023
from turtle import *
speed(0)

n = int(textinput('Unos broja', 'Unesite broj izmedu 0 i 50: '))

colormode(1.0)
boja = 0.80
br = 0

for i in range(5):
    fillcolor(boja, boja, boja)
    begin_fill()
    fd(300-n*br)
    lt(120)
    fd(300-n*br)
    lt(120)
    fd(300-n*br)
    lt(120)
    home()
    end_fill()
    br += 1

    boja *= 0.75

Screen().exitonclick()

