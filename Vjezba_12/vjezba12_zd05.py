#vjezba12_zd5 Karlo Hasnek 24/01/2023
from turtle import *

speed = 0
n = int(textinput("duljina", "Veci od 100 i manji od 300: "))

pu()
goto(0, -(n/2))
pd()
circle(n/2)
pencolor('gray')
fillcolor('gray')
begin_fill()
circle(n/2, 360, 5)
end_fill()
ht()
Screen().exitonclick()
