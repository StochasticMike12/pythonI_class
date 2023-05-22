'''
NAME
     txt_a_fasta.py 

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

    % py txt_a_fasta.py
   
  
  
'''

# ===========================================================================
# =                            main
# ===========================================================================


# step 1.

# Pedir la ruta y archivo que contiene la secuencia de DNA
print("\nRuta y nombre del archivo .txt que contiene la secuencia de DNA:", end=" ")
ruta_archivo = input()

# Pedir nombre o identificador de la secuencia
print("\nIntroduce el nombre de la secuencia que desees convertir a formato FASTA:", end=" ")
nombre_secuencia = input()

# Pedir ruta y nombre del archivo de salida
print("\nNombre del archivo de salida (sin la extensión .fasta):", end=" ")
nombre_fasta = input()
print("\nIntroduce la ruta donde desees que se cree el archivo FASTA:", end=" ")
ruta_fasta = input()

# Leer la secuencia en formato raw desde el archivo
archivo_txt = open(ruta_archivo, "r")
secuencia_dna = archivo_txt.read().rstrip("\n")
archivo_txt.close()

# Generar formato fastA y guardarla en archivo de salida
ruta_completa_fasta = ruta_fasta + "\\" + nombre_fasta + ".fasta" 
archivo_fasta = open(ruta_completa_fasta, "w")
archivo_fasta.write(">" + nombre_secuencia + "\n" + secuencia_dna)
archivo_fasta.close()

print("\nEl archivo se creó exitosamente en la siguiente ruta: " + ruta_completa_fasta + "\n\n"); 

