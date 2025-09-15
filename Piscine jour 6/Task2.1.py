def calcul(entier):
    if entier <= 0:
        return 0
    else:
        return entier + calcul(entier - 1)

print(calcul(42))