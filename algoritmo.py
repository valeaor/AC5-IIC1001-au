import random

print("Calculadora del Amor")

a = input("Dime tu nombre: ")
b = input("Dime el nombre de tu Amor: ")

cantidad_letras = len(a) + len(b)
if cantidad_letras < 10:
    compatibilidad = "Incompatible"
elif cantidad_letras >= 10 and cantidad_letras <= 20:
    compatibilidad = "Poco compatible"
elif cantidad_letras > 20:
    compatibilidad = "Compatible"

print(compatibilidad)