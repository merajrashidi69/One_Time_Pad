#vignere_cipher
import random
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def vignere(message,key,mode):
    amount = 0
    result = ''
    for letters in message:
        if letters.upper() in alpha:
            index = alpha.index(letters.upper())
            if mode == 'encrypt' : index += alpha.index(key[amount].upper())
            if mode == 'decrypt' : index -= alpha.index(key[amount].upper())
            index %= len(alpha)
            if letters.isupper() : result += alpha[index]
            if letters.islower() : result += alpha[index].lower()
            amount += 1
            if amount == len(key):
                amount = 0
        else:
            result += letters
    return result
def keyGen(length):
    result = ''
    for value in range(0,length):
        result += random.choice(alpha)
    #print(result)
    return result
def menu():
    option = input('\n\nDo you want to (e)ncrypt or (d)ecrypt : ')
    message = input('Enter your message : ')
    if option == 'e':
        option = 'encrypt'
        key = keyGen(len(message))
    else:
        option = 'decrypt'
        key = input('Enter your key: ')
    ciphertext = vignere(message,key,option)
    print(ciphertext)
looping = True
while looping:
    try : menu()
    except : looping = False
    



    

        

        
