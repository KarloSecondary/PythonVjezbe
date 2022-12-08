#vjezba2_zd9 Karlo Hasnek 25/10/2022

'''9. Napišite program vjezba2_zd09.py koji od korisnika traži unos četveroznamenkastog cijelog
broja i potom u ispisuje znamenke tog broja u obrnutom redoslijedu. Npr. za unos 5018
ispisuje 8105 (ukoliko broj ima manje od 4 znamenke onda pretpostavljamo da su vodeće
znamenke 0).
'''

unos = int(input("unesite broj izmedu 1 - 9999: "))
a, ostatak1 = divmod(unos, 1000)
b, ostatak2 = divmod(ostatak1, 100)
c, d = divmod(ostatak2, 10)
print(d,c,b,a)
