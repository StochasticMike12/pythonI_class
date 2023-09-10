'''
NAME

    conteo_bases.py 

VERSION

    2.0

AUTHOR

    Miguel Ángel Flores Varela

CONTACT

    mfvarela@lcg.unam.mx

DESCRIPTION

    Este programa cuenta el número de cada base nitrogenada en una 
    secuencia dada.

CATEGORY

    Genómica

USAGE

    % py conteo_bases.py <path_archivo_de_entrada>
      
'''


# ===========================================================================
# =                            imports
# ===========================================================================

# Importar las librerías necesarias.

import argparse
import re



# ===========================================================================
# =                            Command Line Options
# ===========================================================================

# Definir la función del programa.

descripcion = ("Este programa cuenta el número de cada base nitrogenada \n",
             "en una secuencia dada.")
parser = argparse.ArgumentParser(description=descripcion)


# Definir los argumentos.

parser.add_argument('Path',
                    metavar='path',
                    type=str,
                    help='El path del archivo')


# Ejecutar método parse_args()
args = parser.parse_args()



# ===========================================================================
# =                            main
# ===========================================================================

# Pedir el pad del archivo

ruta_archivo = args.Path


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