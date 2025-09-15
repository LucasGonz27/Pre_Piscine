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

def legume():
    print(" ssssssss ")

def hamburger(bool):
    sandDefault = [lettuce, tomato, ham, ham]
    hambVege = [legume, legume]
    if bool == 1:
        bread()
        for ingredient in sandDefault:
            ingredient()
        bread()
    elif bool == 0:
        bread()
        for ingredient in hambVege:
            ingredient()
        bread()

hamburger(1)
