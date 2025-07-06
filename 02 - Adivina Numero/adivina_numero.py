# Juego de adivinar el número: El programa elige un número aleatorio y el usuario debe adivinarlo. El programa le da pistas (mayor o menor).
'''
    Titulo: Juego de adivinar el número
    Descripción: El programa elige un número aleatorio y el usuario debe adivinarlo. El programa le da pistas (mayor o menor).
    Programador: José Gálvez
    Fecha: 06/07/2025
'''
import random

print("--- Juego de adivinar el número ---")

try:
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            numero = int(input("Adivina el número (entre 1 y 100): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        intentos += 1

        if numero < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        elif numero > numero_secreto:
            print("El número es menor. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
except KeyboardInterrupt:
    print("\n¡Gracias por jugar!")
    exit()