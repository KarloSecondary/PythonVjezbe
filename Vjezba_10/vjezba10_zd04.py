#vjezba10_zd4 Karlo Hasnek 09/01/2023
from turtle import *

n = int(textinput('Unos broja vrhova', 'Unesite broj vrhova'))

pu()
rt(90)
fd(100)
lt(90)
pd()

circle(100)
circle(100, 360, n)

Screen().exitonclick()
