# Contador de palabras: Pide al usuario que ingrese un texto y cuenta el número de palabras.
'''
    Titulo: Contador de palabras
    Descripción: Pide al usuario que ingrese un texto y cuenta el número de palabras.
    Programador: José Gálvez
    Fecha: 06/07/2025
'''
def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

if __name__ == "__main__":
    texto_usuario = input("Introduce un texto: ")
    numero_palabras = contar_palabras(texto_usuario)
    print(f"El número de palabras en el texto es: {numero_palabras}")