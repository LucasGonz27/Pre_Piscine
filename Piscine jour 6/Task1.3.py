def bread():
	print(" <===========> ")

def lettuce():
	print(" ~~~~~~~~~~~~ ")

def tomato():
	print(" ooooooooo ")

def ham():
	print(" ======== ")

listeIngredient = [
	[lettuce, tomato, ham, ham],
	[lettuce, ham, tomato, ham],
	[tomato, lettuce, ham, ham],
	[ham, ham, lettuce, tomato],
]

for i in range(4):
	print(f"\nBurger {i + 1}:")
	bread()
	ingredients = listeIngredient[i % len(listeIngredient)]
	for ingredient in ingredients:
		ingredient()
	bread()


