from math import *


def pgcd(a1, b1):
    sorti, swap, exa, a, b, reste = 1, 0, 0, a1, b1, 0

    print('On calcule le PGCD(', a1, ',', b1, '):')

    if (a < b):
        swap = b
        b = a
        a = swap

    while (sorti != 0):

        coef = floor(a / b)
        reste = a % b
        print(int(a), '=', int(b), '*', int(coef), '+', int(reste))

        if reste == 0:
            a, b = exa, a
            coef = floor(a / b)
            reste = a % b
            print("'", int(a), '=', int(b), '*', int(coef), '+', int(reste), "'")
            break
        exa, a, b = a, b, reste

    pgcd = reste
    print('PGCD(', int(a1), ',', int(b1), ') =', int(pgcd), '\n\n')

    return pgcd

