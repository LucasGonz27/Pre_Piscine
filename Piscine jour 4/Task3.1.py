cle = int(input("entrez une clé : "))
message = input("entrez un message : ")
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

messageCrypt = ""

for char in message.lower():
    if char == " ":
        messageCrypt += " "
    if char in alphabet:
        place = alphabet.index(char)
        messageCrypt += alphabet[(place + cle) % 26]
print(messageCrypt)
































