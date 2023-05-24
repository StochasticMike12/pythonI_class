'''
NAME
     piedra-papel-tijera.py 

VERSION
        1.0

AUTHOR
        Miguel Ángel Flores Varela

DESCRIPTION
        Este programa simula un juego de piedra papel o tijera, el usuario elige su opción y
        juega contra la computadora, la cual elije su opción al azar.

CATEGORY
        Genómica

USAGE

    % py piedra-papel-tijera.py
    
    
'''

# ===========================================================================
# =                            main
# ===========================================================================



# Importar la librería random para generar valores aleatorios.

import random


# Declarar os elementos constantes en el código.

opciones=['tijera','piedra','papel']
op1 = "tijera"
op2 = "piedra"
op3 = "papel"


# Comenzar el programa

print("\n\nBienvenido al juego de piedra, papel o tijera.")

# Repetir el programa las veces que el usuario desee.
iniciador = "s"
while iniciador == "s":
        nombre=input("\nDame tu nombre: ")
        opcion_entrada=input("\n" + nombre + ", a la de 3, teclea tu opción (piedra, papel o tijera): ")
        
        # Convertir a minúsculas para procesar mejor
        opcion_usuario=opcion_entrada.lower()
        
        # Obtener valores aleatorios para la elección de la computadora
        opcion_a_elegir=random.randint(0, 2)
        opcion_compu=opciones[opcion_a_elegir]

        print("\n\n" + nombre + ": " + opcion_usuario)
        print("\nComputadora: " + opcion_compu + "\n\n")

        # Definir el resultado en cada caso posible.
        if opcion_usuario == opcion_compu:
                print("¡Empate!\n\n")
        elif opcion_usuario == op1:
                if opcion_compu == op3:
                        print("¡Felicidades! Ganaste\n\n")
                elif opcion_compu == op2:
                        print("Lo siento, perdiste\n\n")
        elif opcion_usuario == op2:
                if opcion_compu == op1:
                        print("¡Felicidades! Ganaste\n\n")
                elif opcion_compu == op3:
                        print("Lo siento, perdiste\n\n")
        elif opcion_usuario == op3:
                if opcion_compu == op2:
                        print("¡Felicidades! Ganaste\n\n")
                elif opcion_compu == op1:
                        print("Lo siento, perdiste\n\n")
        print("\nIntroduce el número de la opción que desees\n\n")
        
        # Preguntar al usuario si quiere continuar el juego.
        iniciador = input("¿Quieres volver a jugar?\n\nSí(s)\n\nNo(n)\n\n")
        
        # Volver a preguntar al usuario en dado caso de que ingrese una opción no especificada.
        while iniciador!="s" and iniciador!="n":
                print("\n\nIntroduce una opción válida\n\n")
                iniciador=input("¿Quieres volver a jugar?\n\nSí(s)\n\nNo(n)\n\n")