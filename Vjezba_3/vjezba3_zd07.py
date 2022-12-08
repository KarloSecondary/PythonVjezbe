#Vježba3_Zadatak7 Karlo Hasnek 31.10.

import math

arg = float(input("Unesi argument: "))
if arg>0:
    baza = float(input("Unesi bazu: "))
    if baza>0 and baza!=1:
        print("Logaritam zadanog unosa iznosi: ",round(math.log(arg,baza), 2))
    else:
        print("Baza je krivo unešena, pokušajte ponovno!")
else:
    print("Argument je krivo unešen, pokušajte ponovno!")
