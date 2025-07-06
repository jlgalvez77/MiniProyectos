# Generador de contraseñas: Genera una contraseña aleatoria de una longitud específica con letras, 
# números y símbolos.
'''
    Titulo: Generador de contraseñas
    Descripción: Genera una contraseña aleatoria de una longitud específica con letras, números y símbolos.
    Programador: José Gálvez
    Fecha: 06/07/2025
'''

import secrets
import string

print("--- Generador de contraseñas ---")
numero_caracteres = int(input("Ingresa el número de caracteres que deseas en tu contraseña: "))
while True:
    if numero_caracteres < 8:
        print("La contraseña debe tener al menos 8 caracteres")
        continue
    else:
        break

letras = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation

contrasena = ''.join(secrets.choice(letras + numeros + simbolos) for _ in range(numero_caracteres))
print(f"Tu contraseña es: {contrasena}")

