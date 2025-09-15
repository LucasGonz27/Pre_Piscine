import string

def chekerPalindrome(chaine):
    chaine = chaine.translate(str.maketrans('', '', string.punctuation)).lower().replace(' ', '')
    if len(chaine) <= 1:
        return True
    # Si les extrémités sont différentes  ce n'est pas un palindrome
    if chaine[0] != chaine[-1]:
        return False

    return chekerPalindrome(chaine[1:-1])

chaineCara = input('ecris un truc : ')
if chekerPalindrome(chaineCara):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")





