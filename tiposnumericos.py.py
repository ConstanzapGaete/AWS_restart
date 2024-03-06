#Python tiene tres tipos numericos: int, float y complex

# Entero
numero_entero = 10

# Decimal
numero_decimal = 3.14159

# Complejo
numero_complejo = 1 + 2j

# Operaciones básicas
suma = numero_entero + numero_decimal
resta = numero_decimal - numero_entero
multiplicacion = numero_entero * numero_decimal
division = numero_decimal / numero_entero

# Conversión de tipos
numero_entero_a_decimal = float(numero_entero)
numero_decimal_a_entero = int(numero_decimal)

# Comprobación de tipos
es_entero = isinstance(numero_entero, int)
es_decimal = isinstance(numero_decimal, float)
es_complejo = isinstance(numero_complejo, complex)

# Salida por pantalla
print("Número entero:", numero_entero, type(numero_entero))
print("Número decimal:", numero_decimal, type(numero_decimal))
print("Número complejo:", numero_complejo, type(numero_complejo))

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

print("Conversión entero a decimal:", numero_entero_a_decimal)
print("Conversión decimal a entero:", numero_decimal_a_entero)

print("Es entero:", es_entero)
print("Es decimal:", es_decimal)
print("Es complejo:", es_complejo)