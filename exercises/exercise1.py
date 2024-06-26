"""Aritmética Básica"""


"""
Calcular el área del cuadrado usando las variables disponibles.
Restricción: Usar el operador de multiplicación
"""

lado_cuadrado = 5

# COMPLETAR - INICIO

area_cuadrado = lado_cuadrado * lado_cuadrado
print(f"El area del cuadrado es: {area_cuadrado}")

# COMPLETAR - FIN

assert area_cuadrado == 25


"""
Re-Escribir usando el operador de potencia.
"""

lado_cuadrado = 5

# COMPLETAR - INICIO

area_cuadrado_pow = lado_cuadrado ** 2

print(f"El area del cuadrado usando potencias es: {area_cuadrado_pow}")

# COMPLETAR - FIN

assert area_cuadrado == 25


"""
Re-Escribir usando la función pow.
"""

lado_cuadrado = 5

# COMPLETAR - INICIO
area_cuadrado = pow(lado_cuadrado,2)
print(f"El area del cuadrado usando pow es: {area_cuadrado}")

# COMPLETAR - FIN

assert area_cuadrado == 25


"""
Calcular la cantidad de unidades a comprar.
Restricción: Usar el operador de división entera.
"""

precio = 3.74
presupuesto_disponible = 10

# COMPLETAR - INICIO
cantidad_a_comprar = presupuesto_disponible // precio
print(f"La cantidad a comprar es: {cantidad_a_comprar}")
# COMPLETAR - FIN

assert cantidad_a_comprar == 2


"""
Determinar si el número de la variable es divisible por 7.
Restricción: Usar el operador módulo.
"""

numero_incalculable = 2 ** 54 - 1

# COMPLETAR - INICIO
es_divisible_por_siete = numero_incalculable % 7
print(f"El resultado es: {es_divisible_por_siete}")
# COMPLETAR - FIN

assert es_divisible_por_siete