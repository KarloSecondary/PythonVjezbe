#vjezba10_zd3 Karlo Hasnek 09/01/2023
from turtle import *

n = int(textinput('Unos broja vrhova', 'Unesite broj vrhova'))

for i in range(n):
    write(str(i+1))
    fd(100)
    lt(360/n)
