'''
NAME

    iso_count_genbank.py 

VERSION
    1.0.0

AUTHOR
    Miguel Ángel Flores Varela

CONTACT

    mfvarela@lcg.unam.mx

DESCRIPTION

    Este programa procesa archivos genbank para conocer el aislado del cual
    proviene la(s) secuencia(s) dentro de este, así como el país de origen.

CATEGORY

    Genómica

USAGE

    % py iso_count_genbank.py  <path_archivo_de_entrada> 
  
'''


# ===========================================================================
# =                            imports
# ===========================================================================

# Importar librerías necesarias.

from Bio import SeqIO
import argparse


# ===========================================================================
# =                            Command Line Options
# ===========================================================================

# Definir los argumentos.

parser= argparse.ArgumentParser(description='Este programa procesa archivos genbank para conocer el aislado del cual proviene la(s) secuencia(s) dentro de este, así como el país de origen.')

parser.add_argument('Path',
                    metavar='path',
                    type=str,
                    help='El path del archivo')


# Ejecutar método parse_args()

args = parser.parse_args()



# ===========================================================================
# =                            functions
# ===========================================================================



# ===========================================================================
# =                            main
# ===========================================================================


try:

    # Abrir archivo y acceder a los elementos del atributo features
    for gb_record in SeqIO.parse(args.Path, "genbank"):
        # Acceder a los elementos de quaifiers por medio de llaves para obtener el aislado y país de origen
        print("\nArchivo:",args.Path,"\nIsolation source:",gb_record.features[0].qualifiers['isolation_source'],"\nCountry:",gb_record.features[0].qualifiers['country'],"\n")

except KeyError:
    print("El archivo no posee alguno de los elementos (aislado o país).")

except FileNotFoundError:
    print("No se encontró el archivo ingresado.")