#vjezba4_zd1 Karlo Hasnek 08/11/2022

unos = str(input("unesite niz znakova: "))
#a)
duljina = len(unos)
print("Duljina unesenog stringa iznosi: ", duljina)

#b)
najveci = max(unos)
print("Najveci znak u zadanom stringu je: ", najveci)

#c)
najmanji = min(unos)
print("Najmanji znak u zadanom stringu je: ", najmanji)

#d)
if duljina > 2:
    print("Drugi znak u zadanom nizu je: ", unos[1])
else:
    print("Uneseni niz znakova je kraci od 2.")

#e)
print("Zadnji znak u zadanom nizu je: ", unos[duljina-1])

#f)
print("%s.%s.%s" % (unos, unos, unos))

#g)
if duljina < 2:
    print("Uneseni niz znakova je kraci od 2.")
else:
    print("Zadani niz bez prvog i zadnjeg znaka je: ", unos[1:(duljina-1)])

#h)
print("Zadani niz zapisan obrnutim redosljedom: ", unos[::-1])

#i)
print("Zadani niz, ali je ispisano svako drugo slovo: ", unos[1::2])

#j)
if "a" in unos:
    print("Slovo a je dio zadanog niza i nalazi se na %d. mjestu " % (unos.find("a")+1))
else:
    print("Slovo a nije dio zadanog stringa.")