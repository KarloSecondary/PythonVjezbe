#vjezba8_zd3 Karlo Hasnek 30/11/2022
x = int(input("Unesi x koordinatu: "))
y = int(input("Unesi y koordinatu: "))


def kvadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    elif x == 0 and y == 0:
        return 0
    elif y == 0:
        return 'x'
    else:
        return 'y'


if kvadrant(x, y) in range(1,5):
    print(f'Zadana tocka se nalazi u {kvadrant(x, y)}. kvadrantu')
elif kvadrant(x, y) == 0:
    print("Zadana tocka se nalazi u ishodistu.")
else:
    print(f'Tocka {(x, y)} se nalazi na {kvadrant(x, y)} osi.')
