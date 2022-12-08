from sys import path
from math import sqrt
path = path.append('Vjezba_8')


def zbroj(a, b):
    c = a + b
    return c


def zbroj_znamenaka(n):
    n = [int(n) for n in str(n)]
    s = sum(n)
    return s


def udaljenost_od_0(x, y):
    d = sqrt(x**2+y**2)
    return d


def udaljenost_tocaka(x1, y1, x2, y2):
    dT = sqrt((x1-x2)**2+(y1-y2)**2)
    return dT


def palindrom(s):
    s = s.lower().replace(" ", "")
    if s == s[::-1]:
        print("Zadani niz znakova je palindrom!")
    else:
        print("Zadani niz znakova nije palindrom.")


def prost(n):
    br = 0
    for i in range(1, n+1):
        if n % i == 0:
            br += 1
    if br == 2:
        return True
    else:
        return False


def kalkulator_kombinacija(n, k):
    from math import factorial
    print("---Kalkulator kombinacija.---")
    print("PRIMJER. Loto 7/39. 7=k, 39=n")
    print("-----------------------------")
    if n > 0 and k > 0:
        comb = factorial(n) // (factorial(k) * factorial(n - k))
        print("Broj mogucih kombinacija:", comb)


def password_generator():
    # modules
    from string import ascii_letters, digits, punctuation
    from secrets import choice

    # textual guide
    print("------------------------------------------------------------------")
    print("Password Generator".center(66, "-"))
    print("------------------------------------------------------------------")
    char_count = int(input("Input number of characters (length of Password): "))
    print("------------------------------------------------------------------")
    print("Choose what type of characters you would want in your Password.")
    print(f'EXAMPLE. a = alpha, n = number, "s" = symbol.')
    print(f'Or you can even make combinations: as = alpha+symbol,...etc.')
    print("------------------------------------------------------------------")
    char_type = input("Your choice: ")
    print("------------------------------------------------------------------")

    # variables
    alpha, numbers, symbols = ascii_letters, digits, punctuation
    user_experience = ''

    # generator
    while user_experience == '':
        if char_type == 'a':
            Password = ''.join(choice(alpha) for i in range(char_count))
        elif char_type == 'n':
            Password = ''.join(choice(numbers) for i in range(char_count))
        elif char_type == 's':
            Password = ''.join(choice(symbols) for i in range(char_count))
        elif char_type == ('an' or 'na'):
            Password = ''.join(choice(alpha + numbers) for i in range(char_count))
        elif char_type == ('as' or 'sa'):
            Password = ''.join(choice(alpha + symbols) for i in range(char_count))
        elif char_type == ('ns' or 'sn'):
            Password = ''.join(choice(numbers + symbols) for i in range(char_count))
        elif char_type in 'ansasnsnasan':
            Password = ''.join(choice(alpha + numbers + symbols) for i in range(char_count))
        else:
            Password = None
            print("Inputed parameters are incorrect. Please try again.")
            exit()
        # user output
        print("Your Password is: ", Password)
        print(f'If you liked your Password press <q> to quit.')
        user_experience = input(f'If you would like a different Password press <Enter>: ')
        if user_experience:
            print("Thank you and goodbye :)")
            exit()


def rock_paper_scissors_game():
    from random import randint, seed
    from time import sleep
    seed()

    # intro/gamestate
    print("-----Rock, Paper, Scissors game.-----")
    conf = str(input(f'press <Enter> to play.'))

    if conf == '':
        continue_game = True
    else:
        continue_game = False
        print("Goodbye.")
        exit()

    # commands
    commands = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    print("--------------------------")
    print("choose one of the options:")
    print("\t1 = Rock")
    print("\t2 = Paper")
    print("\t3 = Scissors")
    print(f'To quit the game press <q>')
    print("--------------------------")

    # scoreboard
    player, ai = 0, 0

    # engine
    while continue_game:

        # inputs
        selection = input("Your choice: ")
        bot = randint(1, 3)

        # input check
        if selection == 'q':
            print("--------------------------------------------")
            print(f'Player score: {player}\n....AI score: {ai}.')
            print("Thank you for playing!")
            exit()
        elif int(selection) in range(1, 4):
            selection = int(selection)
        else:
            print("The value you inputed was incorrect.")
            print("please try again.\n")

        # game itself
        if selection == bot:
            print(f'You chose {commands[int(selection)]}')
            print(f'Bot chose...')
            sleep(2)
            print(f'{commands[bot]}.')
            print("Draw.")
        elif (selection == 1 and bot == 2) or (selection == 2 and bot == 3) or (selection == 3 and bot == 1):
            print(f'You chose {commands[int(selection)]}.')
            sleep(2)
            print(f'Bot chose {commands[int(bot)]}.')
            print('You lost.')
            ai += 1
        elif (selection == 1 and bot == 3) or (selection == 2 and bot == 1) or (selection == 3 and bot == 2):
            print(f'You chose {commands[int(selection)]}.')
            sleep(2)
            print(f'Bot chose {commands[int(bot)]}.')
            print("Player won.")
            player += 1
