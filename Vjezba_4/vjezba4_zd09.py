#vjezba4_zd9 Karlo Hasnek 08/11/2022

unos = str(input("Unesite proizvoljni niz znakova: "))
duljina = len(unos)
lista = []
for char in unos:
    lista.append(char)
print("Lista unesenih znakova:\n", lista, "\n")
broj_razmaka = lista.count(" ")
print("Broj razmaka unutar liste: ", broj_razmaka, "\n")
lista.sort()
print("Uzlazno sortirana lista:\n", lista, "\n")
print("Uzlazna lista bez posljednjeg clana:\n", lista[:(duljina-1)], "\n")
if "a" in lista:
    lista.remove('a')
    print("Lista bez prvo pojavljenog slova a:\n", lista, "\n")
else:
    print("Slovo a nije dio liste.")

