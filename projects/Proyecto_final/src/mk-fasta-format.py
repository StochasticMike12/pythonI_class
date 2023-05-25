'''
NAME
     mk-fasta-format.py 

VERSION
        2.0

AUTHOR
        Miguel Ángel Flores Varela

CONTACT

        mfvarela@lcg.unam.mx

DESCRIPTION

     Convierte una secuencia de dna en formato plano a formato fastA.
     
     De manera interactiva pide 
          - la secuencia de dna en formato raw
          - el nombre de la secuencia o identificador
          - el nombre del archivo de salida
          
     formato raw: la secuencia viene en un solo renglon en el archivo.

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
# =                            functions
# ===========================================================================


# Definir función convertidora de txt a fasta.

def txt_a_fasta(nombre_secuencia, nombre_fasta, ruta_fasta):
    """ Convertir un archivo txt a fasta
    
        Parámetros:
        argument1 (str): nombre de la secuencia de DNA
        argument2 (str): nombre del archivo fasta
        argument3 (str): ruta de salida
        
        Returns:
        Crea un archivo fasta

        """
    ruta_completa_fasta = ruta_fasta + "\\" + nombre_fasta + ".fasta" 
    archivo_fasta = open(ruta_completa_fasta, "w")
    archivo_fasta.write(">" + nombre_secuencia + "\n" + secuencia)
    archivo_fasta.close()



# ===========================================================================
# =                            main
# ===========================================================================


# Definir exepciones.
try:
    archivo = open(args.Path, "r")
    secuencia = archivo.read().rstrip("\n")
    
    # Verificar que el archivo no esté vacío.
    if not secuencia:
        print("El archivo está vacío.")
        archivo.close()
    
    # Verificar que al archivo contenga solo As, Ts, Gs y Cs.
    elif re.search(r"[ATGC]", secuencia):
        for caracter in secuencia:
            if (caracter != 'A') and (caracter != 'T') and (caracter != 'G') and (caracter != 'C'): 
                print("El archivo contiene caracteres no válidos.")
                archivo.close()
                break
        
    # Convertir archivo .txt a .fasta.
        else:
            txt_a_fasta(args.nombre_secuencia, args.nombre_fasta, args.path_salida)
            archivo.close()
    else:
        print("El archivo no contiene una secuencia de DNA.")
except IOError:
    print("No se encontró el archivo.")