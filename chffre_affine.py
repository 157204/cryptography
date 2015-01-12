
def verif_key():
    key_right_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    key_b = True
    key_a = (int(input('a = ')))

    if key_a in key_right_a:
        print("clé 'a' valide")
        while key_b:
            key_b = (int(input('b = ')))
            if key_b > 0 and key_b < 26:
                key  = [key_a, key_b]
                return key
            else:
                print('Veuiller rentrer une clé b compris entre 0 et 26 exclus.')
    else:
        print('clé non valide\nLes clés valides sont : 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25')
        return verif_key()

key = verif_key()
print(key)