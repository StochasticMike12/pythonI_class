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


# Abrir archivo y extraer información del archivo de entrada.

print("\nIntroduce la ruta del archivo que desee abrir:", end=" ")
ruta_archivo = input()
try:
    archivo = open(ruta_archivo, "r")
    secuencia = archivo.read().rstrip("\n")
    if not secuencia[]:
        print("El archivo está vacío.")
        archivo.close()
    elif re.search(r"[ATGC]", secuencia):
        if re.search(r"[^ATGC]", secuencia): 
            archivo.close()
        else:
        A=secuencia.count('A')
        T=secuencia.count('T')
        C=secuencia.count('C')
        G=secuencia.count('G')
        archivo.close()
except IOError:
    print("No se encontró el archivo.")



# Imprimimos el total de cada base nitrogenada.

print("\n\nEl total por base es:\n\nA:", A,"\nT:", T,"\nC:", C,"\nG:", G,"\n")