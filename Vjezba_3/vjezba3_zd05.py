#Vježba3_Zadatak5 Karlo Hasnek 31.10.

import math

a = float(input("unesi prvi koeficijent a: "))
b = float(input("unesi prvi koeficijent b: "))
c = float(input("unesi prvi koeficijent c: "))

D = b*b-4*a*c

if a==0:
    print('Ovo nije kvadratna jednadžba')
elif D>0:
    x1 = -b+math.sqrt(b**2-(4*a*c))/(2*a)
    x2 = -b-math.sqrt(b**2-(4*a*c))/(2*a)
    print("Dva rješenja ove kvadratne jednadžbe iznose: x1=%d i x2 = %d" %(x1,x2))
elif D==0:
    x1 = -b+math.sqrt(b**2-(4*a*c))/(2*a)
    print("Ova kvadratna jednadžba ima jedinstveno rješenje koja iznosi = ",x1)
else:
    print("Ova kvadratna jednadžba nema realnih rješenja")
