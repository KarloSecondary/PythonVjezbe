#vjezba8_zd2 Karlo Hasnek 30/11/2022

print("Funkcija za provjeravanje palindroma.")


def palindrom(s):
    s = s.lower().replace(" ", "") #provjera za palindrome poput: 'Ana voli Milovana'
    if s == s[::-1]:
        print("Zadani niz znakova je palindrom!")
    else:
        print("Zadani niz znakova nije palindrom.")


palindrom(s=input("Unesi niz znakova: "))
