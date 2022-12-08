#vjezba5_zd5 Karlo Hasnek 18/11/2022

niz = str(input("Unesi niz znakova: "))
niz = [*niz]
eng = "qwxyQWXY"
hrv = "šđžčćŠĐŽČĆ"
for i in range(len(niz)):
    if niz[i].isalpha() or niz[i] in hrv:
        if niz[i] == "d" and niz[i+1] == "ž":
            print(niz[i]+niz[i+1])
        elif niz[i-1] == "d" and niz[i] == "ž":
            continue
        elif (niz[i] == "l" or niz[i] == "n") and niz[i+1] == "j":
            print(niz[i]+niz[i+1])
        elif niz[i] == "j" and (niz[i-1] == "l" or niz[i-1] == "n"):
            continue
        elif niz[i] in eng:
            continue
        else:
            print(niz[i])
