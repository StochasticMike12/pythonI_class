'''
NAME
     count_atgc.py 

VERSION
        1.0

AUTHOR
        Miguel Ángel Flores Varela

DESCRIPTION
        Este programa cuenta el número de cada base nitrogenada en una secuencia dada.

CATEGORY
        Genómica

USAGE

    % py count_atgc.py
    
    
'''

# ===========================================================================
# =                            main
# ===========================================================================


# step 1.

# Importar librería re para utilizar expresiones regulares.

import re


# Pedir el pad del archivo

ruta_archivo = input('Introduce la ruta del archivo que desee abrir: ')


# Verificar que el archivo exista.

try:
    archivo = open(ruta_archivo, "r")
    secuencia = archivo.read().rstrip("\n")
    
    # Verificar que el archivo no esté vacío.
    if not secuencia:
        print("El archivo está vacío.")
        archivo.close()
    
    # Verificar que al archivo contenga solo As, Ts, Gs y Cs.
    elif re.search(r"[ATGC]", secuencia):
        if re.search(r"[^ATGC]", secuencia): 
            print("El archivo contiene caracteres no válidos.")
            archivo.close()
        
        # Contar bases nitrogenadas.
        else:
            A=secuencia.count('A')
            T=secuencia.count('T')
            C=secuencia.count('C')
            G=secuencia.count('G')
            archivo.close()
            print("\n\nEl total por base es:\n\nA:", A,"\nT:", T,"\nC:", C,"\nG:", G,"\n")
    else:
        print("El archivo no contiene una secuencia de DNA.")
except IOError:
    print("No se encontró el archivo.")