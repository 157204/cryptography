from chiffre_affine import *
from pgcd import *

print('BONJOUR !\n\n')
print('PGCD[1]\n'
      'Chiffrage affine[2]\n'
      'Déchiffrage affine[3]\n'
      'Chiffrage de Hill[4]\n'
      'Déchiffrage de Hill[5]\n')
choix = int(input('choisisser une opération : '))

if choix == 1:  # PGCD
    pgcd(float(input('Premier nombre: ')), float(input('Deuxième nombre: ')))
elif choix == 2:  # Chiffrage affine
    key = verif_key()
    print(key)
    chiffre = chiffrage_lettre(key[0], key[1], input('Saisir un text : '))
    print(''.join(chiffre))
elif choix == 3:  # Déchiffrage affine

#elif choix == 4:  # Chiffrage de Hill
#elif choix == 5:  # Déchiffrage de Hill