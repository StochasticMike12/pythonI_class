'''
NAME

    org_date_genbank.py 

VERSION
    1.0.0

AUTHOR
    Miguel Ángel Flores Varela

CONTACT

    mfvarela@lcg.unam.mx

DESCRIPTION

    Este programa procesa archivos genbank para conocer el organismo del cual
    proviene la(s) secuencia(s) dentro de este, así como su fecha de 
    recuperación.

CATEGORY

    Genómica

USAGE

    % py org_date_genbank.py  <path_archivo_de_entrada> 
  
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

parser= argparse.ArgumentParser(description='Este programa procesa archivos genbank para conocer el organismo del cual proviene la(s) secuencia(s) dentro de este, así como su fecha de recuperación.')

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
    # Abrir archivo y obtener la fecha y el organismo del atributo annotations
    for gb_record in SeqIO.parse(args.Path, "genbank"):
        print("\nFile:",args.Path,"\norganism:",gb_record.annotations['organism'],"\ndate:",gb_record.annotations['date'],"\n")

except FileNotFoundError:
    print("No se encontró el archivo ingresado.")