def verif_key():
    key_right_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    key_b = True
    key_a = (int(input('a = ')))

    if key_a in key_right_a:
        print("clé 'a' valide")
        while key_b:
            key_b = (int(input('b = ')))
            if key_b > 0 and key_b < 26:
                key = [key_a, key_b]
                return key
            else:
                print('Veuiller rentrer une clé b compris entre 0 et 26 exclus.')
    else:
        print('clé non valide\nLes clés valides sont : 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25')
        return verif_key()


def chiffrage_lettre(a, b, text):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    textchiffre = []
    for i in text:
        x = ord(i)
        if x >= 97 and x <= 122:
            x -= - 97
            print(x)
            y = a * x + b
            print('y = ', a, '*', x, '+', 'b = ', y)
            while y > 26:
                y %= 26
                print(y)
            print('y = ', y, '[26]')
            y = alphabet[y]
            textchiffre.append(y)
        elif x >= 65 and x <= 90:
            x -= - 65
            print(x)
            y = a * x + b
            print('y = ', a, '*', x, '+', 'b = ', y)
            while y > 26:
                y %= 26
                print(y)
            print('y = ', y, '[26]')
            y = alphabet[y]
            textchiffre.append(y)



    return textchiffre
