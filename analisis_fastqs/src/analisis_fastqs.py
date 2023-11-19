'''
NAME

    analisis_fastqs.py 

VERSION
    1.0.0

AUTHOR
    Miguel Ángel Flores Varela

CONTACT

    mfvarela@lcg.unam.mx

DESCRIPTION

    Este programa procesa archivos FASTQ, permite conocer el número de
    lecturas con un promedio de calidad mayor o menor (según lo elija 
    el ususario) a un umbral establecido por el usuario.

CATEGORY

    Genómica

USAGE

    % py analisis_fastqs.py <path_archivo_de_entrada> <umbral> <bajo_ubral>
  
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

parser= argparse.ArgumentParser(description='Este programa procesa archivos FASTQ, permite conocer el número de lecturas con un promedio de calidad mayor o menor (según se elija) a un umbral establecido por el usuario. El programa recibe como primer argumento el path o dirección del archivo de entrada, seguido del umbral sobre el cual se trabajará y como tercer argumento se especifica si se desea obtener las lecturas con un promedio mayor (False) o menor (True) al umbral espesificado.')

parser.add_argument('Path',
                    metavar='path',
                    type=str,
                    help='El path del archivo')

parser.add_argument('Threshold',
                    metavar='threshold',
                    type=float,
                    help='Umbral sobre el cual se analizan las lecturas')

parser.add_argument('Lower',
                    metavar='lower',
                    type=str,
                    help='Instrucción para indicar si se quiere obtener las lecturas con promedio de calidad menor al umbral especificado')


# Ejecutar método parse_args()
args = parser.parse_args()


# ===========================================================================
# =                            functions
# ===========================================================================



# ===========================================================================
# =                            main
# ===========================================================================

# Declarar variables constantes

threshold=args.Threshold
lower=args.Lower

accumulated_score=0
n_filtered_seqs=0
n_seqs=0


try: 
    # Abrir y procesar el archivo
    for record in SeqIO.parse(args.Path, "fastq"):
        scores=record.letter_annotations["phred_quality"]
        nt_number=len(scores)
    
        # Calcular promedio de calidad para cada lectura
        for score in scores:
            accumulated_score=accumulated_score+score
        mean_score=accumulated_score/nt_number
    
        # Contar las lecturas de interés de acuerdo al umbral
        if (lower=='True'):
            if mean_score<threshold:
                n_filtered_seqs+=1
        elif (lower=='False'):
            if mean_score>threshold:
                n_filtered_seqs+=1
        n_seqs+=1


    # Definir variables para imprimir mensaje

    if lower=='True':
        seq='menores'
    elif lower=='False':
        seq='menores'


    # Imprimir el resultado del conteo

    print("\nArchivo:",args.Path,"\nLecturas:",n_seqs,'\nLecturas', seq,"al umbral:",n_filtered_seqs,"\n")

except FileNotFoundError:
    print("No se encontró el archivo ingresado.")

