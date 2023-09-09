'''
NAME
     mk-fasta-format.py 

VERSION
        1.0

AUTHOR
        Miguel Ángel Flores Varela

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

    % py mk-fasta-format.py
   
  
  
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
        
        # Convertir archivo .txt a .fasta.
        else:
          print("\nIntroduce el nombre de la secuencia que desees convertir a formato FASTA:", end=" ")
          nombre_secuencia = input()
          print("\nNombre del archivo de salida (sin la extensión .fasta):", end=" ")
          nombre_fasta = input()
          print("\nIntroduce la ruta donde desees que se cree el archivo FASTA:", end=" ")
          ruta_fasta = input()
          ruta_completa_fasta = ruta_fasta + "\\" + nombre_fasta + ".fasta" 
          archivo_fasta = open(ruta_completa_fasta, "w")
          archivo_fasta.write(">" + nombre_secuencia + "\n" + secuencia)
          archivo_fasta.close()
          archivo.close()
    else:
        print("El archivo no contiene una secuencia de DNA.")
except IOError:
    print("No se encontró el archivo.")