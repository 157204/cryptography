from chiffre_affine import *


print('BONJOUR !')
key = verif_key()
print(key)

chiffre = chiffrage_lettre(key[0], key[1], input('Saisir un text : '))
print(''.join(chiffre))