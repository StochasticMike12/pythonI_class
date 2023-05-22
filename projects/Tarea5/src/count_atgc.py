'''
NAME
     conteo_bases.py 

VERSION
        1.0

AUTHOR
        Miguel Ángel Flores Varela

DESCRIPTION
        Este programa cuenta el número de cada base nitrogenada en una secuencia dada.

CATEGORY
        Genómica

USAGE

    % py conteo_bases.py
    
    
'''

# ===========================================================================
# =                            main
# ===========================================================================


# step 1.


# Primero indicamos al usuario que introduzca una secuencia de DNA que desee.

print("\nIntroduce la secuencia de DNA:", end=" ")
secuencia=input()


# Obtenemos el número de cada base nitrogenada en la secuencia.

A=secuencia.count('A')
T=secuencia.count('T')
C=secuencia.count('C')
G=secuencia.count('G')


# Imprimimos el total de cada base nitrogenada.

print("\n\nEl total por base es:\n\nA:", A,"\nT:", T,"\nC:", C,"\nG:", G,"\n")