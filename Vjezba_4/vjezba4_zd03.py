#vjezba4_zd3 Karlo Hasnek 08/11/2022

niz = input("Unesite niz znakova: ")
broj = int(input("Unesite cijeli broj: "))
if str(broj+1) in niz:
    print(broj+1, "je dio zadanog niza.")
else:
    print(broj+1, "nije dio zadanog niza.")