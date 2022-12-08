#vjezba5_zd10 Karlo Hasnek 18/11/2022

print("Program za ispis najblizeg broja unosu, ali da ima svojstvo da je palindrom. PRIMJER. 1331 ")
print("-------------------------------------------------------------------------------------------")
n = int(input("unesi prirodni broj: "))
if n > 0:
    for i in range(n, 0, -1):
        num = [str(i) for i in str(i)]
        num_rev = num.copy()
        num_rev.reverse()
        if num == num_rev:
            num = ''.join(num)
            print("prvi prirodni broj manji ili jednak od %d koji ima svojstvo da je palindrom: %s" % (n, num))
            break
