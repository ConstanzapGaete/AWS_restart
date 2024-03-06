archivo=open("lsinsulin-seq-clean.txt","r")
c=archivo.read()
total=len(c)
cadena="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
ami1 = cadena[:24]
ami2 = cadena[25:55]
ami3 = cadena[55:90]
ami4 =cadena[90:110]
con1=len(ami2)
con2=len(ami1)
con3=len(ami3)
con4=len(ami4)
print("aminoácidos 1–24--->"+ami1+" cantidad de caracteres-->"+str(con2))
print("aminoácidos 25–54--->"+ami2+" cantidad de caracteres-->"+str(con1))
print("aminoácidos 55–89--->"+ami3+" cantidad de caracteres-->"+str(con3))
print("aminoácidos 90–110--->"+ami4+" cantidad de caracteres-->"+str(con4))

