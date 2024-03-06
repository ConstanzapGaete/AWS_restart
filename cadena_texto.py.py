mi_cadena="hola soy una cadena de texto >:D"
print(mi_cadena)
print(type(mi_cadena))
print(mi_cadena+" Es de tipo "+str(type(mi_cadena)))
string1="agua"
string2="cayendo? "
string3=string1+string2
print(string3)
nombre=input("Como te llamas? ")
print("Buen día >:D "+nombre)
color=input("Cual es tu color favorito? ")
animal=input("Y....cual es tu animal favorito? ")
print("A "+nombre+" le gusta el color "+color+" y su animal favorito es "+animal.format(nombre+color+animal))