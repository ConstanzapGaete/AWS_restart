import random
print("Adivino tu numerooo >:D ")
print("Es simple tu piensas un numero y yo lo adivino muahaha ")
numero = random.randint(1,10)
adivino = False
while adivino != True:
    guess = input("Adivina el numero del 1 al 10 >:D ")
    if int(guess) == numero:
        print("Adivinaste :D {}!  <--- Es correcto! :D ".format(guess))
        adivino = True
    else:
        print("No adivinaste :c {}  <--- Lo siento no es correcto pipipi".format(guess))