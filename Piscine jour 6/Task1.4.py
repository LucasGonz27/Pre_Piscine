def bread():
    print(" <===========> ")

def lettuce():
    print(" ~~~~~~~~~~~~ ")

def tomato():
    print(" ooooooooo ")

def ham():
    print(" ======== ")

def cheese():
    print(" ########## ")

def chicken():
    print(" //////// ")

def hamburger(nbSand):
    listeIngredient = [
        [lettuce, tomato, ham],
        [lettuce, cheese, chicken],
        [tomato, ham, cheese],
        [lettuce, chicken, tomato]
    ]
    for i in range(nbSand):
        print(f"\nBurger {i+1}:")
        bread()
        ingredients = listeIngredient[i % len(listeIngredient)]
        for ingredient in ingredients:
            ingredient()
        bread()

hamburger(4)