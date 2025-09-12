valeur = int(input('donne moi un entier '))
    
if valeur == 42:
    print('a')
elif valeur <= 21:
    print('b')
elif valeur % 2 == 0:
    print('c')
elif valeur / 2 < 21:
    print('d')
elif valeur % 2 != 0 and valeur >= 45:
    print('e')
else:
    print('f')
