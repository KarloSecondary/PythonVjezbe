#vjezba8_zd4 Karlo Hasnek 1/12/2022

def binarno_pretrazivanje(l, s):
    prvi = 0
    zadnji = len(l)-1
    izraz = False

    while prvi <= zadnji and not izraz:

        sredina = (prvi+zadnji)//2
        if l[sredina] == s:
            izraz = True
        else:
            if s < l[sredina]:
                zadnji = sredina-1
            else:
                prvi = sredina+1
    return izraz


l = [1, 4, 5, 9, 8, 7, 18, 12, 16, 98, 51, 23, 16, 84, 45, 12]
l.sort()
print(l)
s = 4
print(binarno_pretrazivanje(l, s))
