#Vježba3_Zadatak2 Karlo Hasnek 31.10.

import math

print("Program za računanje površine trokuta")
print("-------------------------------------")
a = float(input("Unesite stranicu trokuta a: "))
b = float(input("Unesite stranicu trokuta b: "))
c = float(input("Unesite stranicu trokuta c: "))

if (a+b)>c and (a+c)>b and (b+c)>a:
    s = (a+b+c)/2
    P = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(round(P,2))
