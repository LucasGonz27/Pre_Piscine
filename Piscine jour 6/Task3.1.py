#Écrivez 3 fonctions, chacune prenant une chaîne s et un entier n comme paramètres et renvoyant une valeur booléenne :
#✓ funA vérifie si s contient au moins n caractères ;
#✓ funB vérifie si s contient au moins n caractères spéciaux ;
#✓ funC vérifie si s contient au moins n chiffres

def funA(s, n):
    return len(s) >= n


def funB(s, n):
    specialCara = set('!@#$%^&*()-_=+[]{}|;:\'",.<>?/`~')
    count = sum(1 for c in s if c in specialCara)
    return count >= n


def funC(s, n):
    count = sum(1 for c in s if c.isdigit())
    return count >= n

