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

# Imprimimos el número de bases nitrogenadas en la secuencia utilizando la función .count.
print("\n\nEl total por base es:\n\nA:",secuencia.count('A'),"\nT:",secuencia.count('T'),"\nC:",secuencia.count('C'),"\nG:",secuencia.count('G'),"\n")