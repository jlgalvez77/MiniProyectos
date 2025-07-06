# Temporizador de cuenta regresiva: Permite al usuario establecer un tiempo y muestra una cuenta regresiva.
'''
    Titulo: Temporizador de cuenta regresiva
    Descripción: Permite al usuario establecer un tiempo y muestra una cuenta regresiva.
    Programador: José Gálvez
    Fecha: 06/07/2025
'''
import time

def temporizador_cuenta_atras(segundos):
    while segundos:
        mins, secs = divmod(segundos, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        segundos -= 1
    print("¡Tiempo terminado!")
if __name__ == "__main__":
    try:
        tiempo = int(input("Introduce el tiempo en segundos: "))
        if tiempo < 0:
            raise ValueError("El tiempo no puede ser negativo.")
        print(f"Comenzando el temporizador de {tiempo} segundos...")
        temporizador_cuenta_atras(tiempo)
    except ValueError as e:
        print(f"Error: {e}")