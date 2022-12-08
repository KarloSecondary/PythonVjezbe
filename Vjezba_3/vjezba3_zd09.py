#Vježba3_Zadatak9 Karlo Hasnek 31.10.

unos = str(input("Unesi slovo (iz engleske abecede): "))
if unos.islower():
    print("Uneseno slovo je malo slovo: %s" %(unos))
    print("ASCII kod pridružen unesenom slovu je: ",ord(unos))
elif unos.isupper():
    print("Uneseno slovo je veliko slovo: %s" %(unos))
    print("ASCII kod pridružen unesenom slovu je: ", ord(unos))
else:
    print("Uneseni simbol nije valjan, pokušajte ponovno.")
