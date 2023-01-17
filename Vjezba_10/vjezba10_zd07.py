#vjezba10_zd4 Karlo Hasnek 09/01/2023
from turtle import *
from random import *

n = int(textinput('Unos broja tocaka', 'Unesite broj tocaka: '))
m = int(textinput('Unos polumjera tocaka', 'Unesite polumjer tocaka: '))

hideturtle()
speed(0)
colormode(255)

for i in range(n):

    x = randint(-300, 300)
    y = randint(-300, 300)

    pu()
    goto(x, y-m)
    pd()
    write(f'({str(x)}, {str(y)})')

    pu()
    goto(x, y)
    pd()

    fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))

    begin_fill()
    circle(m)
    end_fill()

Screen().exitonclick()