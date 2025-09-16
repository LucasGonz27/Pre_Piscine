def fun1(password , maxiCara):
	return len(password) >= maxiCara

def fun2(password, minSpec):
	specialChar = sum(not c.isalnum() for c in password)
	if specialChar >= minSpec:
		return True
	else:
		return False

def fun3(password, minNumb):
	Nombre = sum(c.isnumeric() for c in password)
	if Nombre >= minNumb:
		return True
	else:
		return False


def passcheck(fun , nb , chaine):
	if not isinstance(chaine, str):
		print('erreur')
		return None
	else:
		return fun(chaine, nb)




print(passcheck(fun2, 3, "7777777777===="))

#print(fun2('yy====yyy' ,3))
#print(fun3('rtttr' ,1))6