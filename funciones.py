def doblealfabeto(alfabeto):
    doubleAlphabet = alfabeto + alfabeto
    return doubleAlphabet

def mensaje():
    stringToEncrypt = input("Ingresa mensaje para cifrar :  ")
    return stringToEncrypt

def clave():
    shiftAmount = input( "Ingresa clave en enteros de 1 a 25 : ")
    return shiftAmount
    
def encryptMessage(message, cipherKey, alfabeto):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alfabeto.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alfabeto:
            encryptedMessage = encryptedMessage + alfabeto[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

def decryptMessage(message, cipherKey, alfabeto):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alfabeto)

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'alfabeto: {myAlphabet}')
    myAlphabet2 = doblealfabeto(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = mensaje()
    print(myMessage)
    myCipherKey = clave()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
runCaesarCipherProgram()