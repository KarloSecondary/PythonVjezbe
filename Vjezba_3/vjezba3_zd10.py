#Vježba3_Zadatak10 Karlo Hasnek 31.10.

unos = str(input("Unesite niz znakova duljine 5: "))
a,b,c,d,e = list(unos)
if a+b+c+d+e == e+d+c+b+a:
    print("Zadani unos je palindrom!")
    print(id(a),id(b),id(c),id(d),id(e))
else:
    print("Zadani unos nije palindrom.")
    
