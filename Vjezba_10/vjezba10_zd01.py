#vjezba10_zd1 Karlo Hasnek 09/01/2023
from turtle import *

pu()
goto(-200, -200)
pd()

for i in 'ABCD':
    write(i)
    fd(400)
    lt(90)

goto(200, 200)
goto(-200, 200)
goto(200, -200)
