#vjezba10_zd4 Karlo Hasnek 09/01/2023
from turtle import *

n = int(textinput('Unos broja vrhova', 'Unesite broj vrhova'))

pu()
rt(90)
fd(100)
lt(90)
pd()

fillcolor('red')
begin_fill()
circle(100)
end_fill()

fillcolor('blue')
begin_fill()
circle(99, 360, n)
end_fill()

Screen().exitonclick()
