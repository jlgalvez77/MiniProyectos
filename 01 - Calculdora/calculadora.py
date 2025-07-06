# Calculadora básica: Crea una calculadora que pueda sumar, restar, multiplicar y dividir dos números.

print("--- Calculadora básica ---")

while True:
    print('''
    Escoje una opción:
    1.- Sumar
    2.- Restar
    3.- Multiplicar
    4.- Dividir
    5.- Salir''')
    try:
        opcion = int(input("Escoje una opción: "))
    except ValueError:
        print("Opción no válida")
        continue

    if opcion in [1, 2, 3, 4]:
        numero1 = float(input("Escribe el primer número: "))
        numero2 = float(input("Escribe el segundo número: "))
        if opcion == 1:
            resultado = numero1 + numero2
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == 2:
            resultado = numero1 - numero2
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == 3:
            resultado = numero1 * numero2
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == 4:
            if numero2 == 0:
                print("Error: No se puede dividir por cero")
            else:
                resultado = numero1 / numero2
                print(f"El resultado de la división es: {resultado}")
    elif opcion == 5:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida")
