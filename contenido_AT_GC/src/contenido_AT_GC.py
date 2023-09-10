'''
NAME
    
    contenido_AT_CG.py 

VERSION
    
    2.0

AUTHOR
    
    Miguel Ángel Flores Varela

CONTACT

    mfvarela@lcg.unam.mx

DESCRIPTION
    
    Este programa pide la ruta de un archivo con una secuencia de DNA y 
    arroja el procentaje de AT y GC de la secuencia dada.

CATEGORY
    
    Genómica

USAGE

    % py contenido_AT_CG.py <path_archivo_de_entrada>      
    
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

descripcion = ("Este programa pide la ruta de un archivo con una secuencia \n",
             "de DNA y arroja el procentaje de AT y GC de la secuencia dada.")
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


        # Obtener porcentajes de AT y GC

        else:
            longitud_dna = len(secuencia)
            AT = secuencia.count("A")+secuencia.count("T")
            GC = secuencia.count("G")+secuencia.count("C")
            porcentaje_AT = (100*AT)/longitud_dna
            porcentaje_GC = (100*GC)/longitud_dna
            print("\n\n\nArchivo de secuencia: " + ruta_archivo) 
            print("\nPorcentaje de AT y GC:\n")
            print("AT:", porcentaje_AT, "%\n\nGC:", porcentaje_GC, "%\n\n\n") 

    else:
        print("El archivo no contiene una secuencia de DNA.")         

except IOError:
    print("No se encontró el archivo.")