#vjezba12_zd2 Karlo Hasnek 24/01/2023
from string import *


def upper_lower(s):
    vel = 0
    mal = 0
    znk = 0
    for i in s:
        if i in ascii_uppercase:
            vel += 1
        elif i in ascii_lowercase:
            mal += 1
        else:
            znk += 1

    return vel, mal, znk


def main():
    s = input("Unesi string: ")

    return upper_lower(s)


print(main())
