#vjezba10_zd4 Karlo Hasnek 09/01/2023
from turtle import *

speed(0)
ht()

radijus = 150
colormode(1.0)
boja = 1.0

for i in range(10):
    pu()
    goto(0, -radijus)
    pd()

    fillcolor(boja, boja, boja)

    begin_fill()
    circle(radijus)
    end_fill()

    boja *= 0.95
    radijus *= 0.9
    
Screen().exitonclick()
