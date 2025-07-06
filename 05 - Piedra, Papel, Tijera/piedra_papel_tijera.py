# Piedra, papel o tijera: Crea un juego interactivo donde el usuario juega contra la computadora.
'''
    Titulo: Piedra, papel o tijera
    Descripción: Crea un juego interactivo donde el usuario juega contra la computadora.
    Programador: José Gálvez
    Fecha: 06/07/2025
'''
import random
print("--- Piedra, papel o tijera ---")
opciones = ["piedra", "papel", "tijera"]

while True:
    print('''
    Escoje una opción:
    1.- Piedra
    2.- Papel
    3.- Tijera
    4.- Salir''')
    
    try:
        opcion_usuario = int(input("Escoje una opción: "))
    except ValueError:
        print("Opción no válida")
        continue

    if opcion_usuario in [1, 2, 3]:
        opcion_usuario = opciones[opcion_usuario - 1]
        opcion_computadora = random.choice(opciones)
        print(f"Tu opción: {opcion_usuario}")
        print(f"Opción de la computadora: {opcion_computadora}")

        if opcion_usuario == opcion_computadora:
            print("¡Es un empate!")
        elif (opcion_usuario == "piedra" and opcion_computadora == "tijera") or \
             (opcion_usuario == "papel" and opcion_computadora == "piedra") or \
             (opcion_usuario == "tijera" and opcion_computadora == "papel"):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")
    elif opcion_usuario == 4:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida")