#secuencia de preproinsulina humana en variable preproinsulina
preproInsulin ="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr"\
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
# elementos restantes de la secuencia de la insulina humana en variables:
lsInsulin="malwmrllpllallalwgpdpaaa"
bInsulin="fvnqhlcgshlvealylvcgergffytpkt"
aInsulin="giveqcctsicslyqlenycn"
cInsulin="rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin
#mostrar en consola :
print("Secuencia de preproinsulin:")
print(preproInsulin)
print("Secuencia de insulina: " + aInsulin)

# Calculo de peso molecular de insulina 
# Lista de los pesos de los aminoacidos  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  
# Contar cantidad de aminoacidos 
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  
# Multiplicar x peso
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("Peso molecular aproximado de insulina : " +
str(molecularWeightInsulin))
molecularWeightInsulinActual = 5807.63
print("Porcentaje de error : " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
