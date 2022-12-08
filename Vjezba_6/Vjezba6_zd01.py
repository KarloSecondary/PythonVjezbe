#vjezba6_zd1 Karlo Hasnek 29/11/2022
from math import sqrt

a = float(input("Unesi decimalni broj: "))

if a > 0:
    P = (a**2*sqrt(3))/4

print(round(P, 2))