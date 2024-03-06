usuario = input(" Necesitas enviar un paquete?  >si  >no ")
if usuario == "si":
    usuario = input("Te gustaria comprar sellos, sobres o una copia (Escribe sello, sobre o copia) ")
    if usuario == "sello":
        print("Cuantos sellos necesitas? ")
    elif usuario == "sobre":
        print("Tenemos muchos sobres con muchos tamaños :D ")
    elif usuario == "copia":
        copies = input("Cuantas copias necesitas? ingresa la cantidad en numeros >  ")
        print("  {} copias.".format(copies))
    else:
        print("Gracias vuelva pronto >:) ")
else:
    print("Vuelve cuando tengas un paquete que entregar >:| ")
    
