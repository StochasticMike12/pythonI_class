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

    % py mk-fasta-format.py <input_file_name> <sequence_name> <output_fasta_name> <fasta_path>     
    
'''


# ===========================================================================
# =                            imports
# ===========================================================================


# Importar librerías necesarias.

import re
import argparse



# ===========================================================================
# =                            Command Line Options
# ===========================================================================


# Definir los argumentos.

descripcion=(" Este programa toma un archivo de texto plano y un nombre \n", 
             "para una secuencia de DNA para crear un archivo fasta.")
parser= argparse.ArgumentParser(description=descripcion)

parser.add_argument('Path',
                    metavar='path',
                    type=str,
                    help='El path del archivo')

parser.add_argument('nombre_secuencia',
                    type=str,
                    help='Identificador o nombre de la secuencia')

parser.add_argument('nombre_fasta',
                    type=str,
                    help='El nombre del archivo de salida con terminacion sin la terminación .fasta')

parser.add_argument('path_salida',
                    type=str,
                    help='El path del archivo donde se guardará el archivo fasta')

# Ejecutar método parse_args()
args = parser.parse_args()


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



# Preguntamos la ruta del archivo que contiene la secuencia de DNA.
print("\nIntroduce la ruta del archivo con la secuencia de DNA:", end=" ")

# Guardamos la ruta del archivo en una variable para poder acceder a cualquier archivo que se desee cada vez que se abra el programa.
ruta_archivo = input()

# Abrimos el archivo con la opción de solo lectura.
archivo = open(ruta_archivo, "r")

# Accedemos al contenido del archivo para leerlo y removemos saltos de línea que puedan encontrarse al final de la cadena.
dna = archivo.read().rstrip("\n")

# Obtenemos la longitud de la secuencia contenida en el archivo.
longitud_dna = len(dna)

# Contamos el número de ATs y GCs en la secuencia.
AT = dna.count("A")+dna.count("T")
GC = dna.count("G")+dna.count("C")

# Realizamos las operaciones correspondientes para obtener el porcentaje de ATs y GCs.
porcentaje_AT = (100*AT)/longitud_dna
porcentaje_GC = (100*GC)/longitud_dna

# Imprimimos la ruta del archivo y el porcentaje de ATs y GCs.
print("\n\n\nArchivo de secuencia: " + ruta_archivo + "\n\nPorcentaje de AT y GC:\n\nAT:", porcentaje_AT, "%\n\nGC:", porcentaje_GC, "%\n\n\n")

# Cerramos el archivo que contiene la secuencia de DNA.
archivo.close()