# Conversor de unidades: Convierte unidades de temperatura (Celsius a Fahrenheit), 
# distancia (metros a kilómetros), etc.
'''
    Titulo: Conversor de unidades
    Descripción: Convierte unidades de temperatura (Celsius a Fahrenheit), distancia (metros a kilómetros), etc.
    Programador: José Gálvez
    Fecha: 06/07/2025
'''

print("--- Conversor de unidades ---")

while True:
    print('''
    Selecciona lo que quieres convertir:
    1.- Temperatura (Celsius a Fahrenheit)
    2.- Distancia (metros a kilómetros)
    3.- Peso (kilogramos a libras)
    4.- Volumen (litros a galones)
    5.- Salir   ''')

    try:
        opcion = int(input("Selecciona una opción: "))
    except ValueError:
        print("Opción no válida")
        continue

    if opcion in [1, 2, 3, 4]:
        if opcion == 1:
            celsius = float(input("Ingresa la temperatura en Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C es igual a {fahrenheit}°F")
        elif opcion == 2:
            metros = float(input("Ingresa la distancia en metros: "))
            kilometros = metros / 1000
            print(f"{metros} metros es igual a {kilometros} kilómetros")
        elif opcion == 3:
            kilogramos = float(input("Ingresa el peso en kilogramos: "))
            libras = kilogramos * 2.20462
            print(f"{kilogramos} kilogramos es igual a {libras} libras")
        elif opcion == 4:
            litros = float(input("Ingresa el volumen en litros: "))
            galones = litros * 0.264172
            print(f"{litros} litros es igual a {galones} galones")
    elif opcion == 5:
        print("¡Gracias por usar el conversor de unidades!")
        break
    else:
        print("Opción no válida")