#vjezba2_zd7 Karlo Hasnek 25/10/2022

'''7. Napišite program vjezba2_zd07.py koji od korisnika traži unos triju brojeva x, y i z
(respektivno). Nakon unosa zamijenite vrijednosti u varijablama na način da u varijabli x bude
vrijednost z, u varijabli y vrijednost x i u varijabli z vrijednost y, te ih ispišite početnim
redoslijedom (x, y, z). Program napravite prvo bez korištenja višestrukog pridruživanja, a
potom korištenjem višestrukog pridruživanja.'''

x = int(input("Unesi prvi broj:"))
y = int(input("Unesi drugi broj:"))
z = int(input("Unesi treci broj:"))

#bez visestrukog pridruzivanja
a = x
b = y
x = z
y = a
z = b
print(x,y,z)

#visestruko pridruzivanje
#x,y,z = z,x,y
#print(x,y,z)
