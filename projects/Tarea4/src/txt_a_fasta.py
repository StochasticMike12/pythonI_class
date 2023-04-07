'''
NAME
     txt_a_fasta.py 

VERSION
        1.0

AUTHOR
        Miguel Ángel Flores Varela

DESCRIPTION
        Este programa arroja ciertas posiciones en especpifico dentro de una secuencia de DNA.

CATEGORY
        Genómica

USAGE

    % py txt_a_fasta.py
    
    
'''

# ===========================================================================
# =                            main
# ===========================================================================


# step 1.

# Preguntamos la ruta del archivo .txt que contiene la secuencia de DNA que deseamos convertir a formato FASTA.
print("\nIntroduce la ruta del archivo .txt que contiene la secuencia de DNA que desees convertir a formato FASTA:", end=" ")

# Guardamos la ruta del archivo en una variable para poder acceder a cualquier archivo que se desee cada vez que se abra el programa.
ruta_archivo = input()

# Preguntamos qué nombre se desea que tenga la secuencia.
print("\nIntroduce el nombre de la secuencia que desees convertir a formato FASTA:", end=" ")

# Guardamos el nombre de la secuencia en una variable para añadirlo más tarde al archivo FASTA.
nombre_secuencia = input()

# Preguntamos qué nombre se desea que contenga el archivo FASTA.
print("\nIntroduce el nombre que desees que tenga que archivo FASTA (sin la extensión .fasta):", end=" ")

# Guardamos el nombre del archivo FASTA  en una variable para nobarlo posteriormente.
nombre_fasta = input()

 # Preguntamos dónde se desea crear el archivo FASTA.
print("\nIntroduce la ruta donde desees que se cree el archivo FASTA:", end=" ")

# Guardamos la ruta del archivo FASTA para guardarlo ahí posteriormente.
ruta_fasta = input()

# Abrimos el archivo de texto con la opción de solo lectura.
archivo_txt = open(ruta_archivo, "r")

# Accedemos al contenido del archivo de texto y lo guardamos en una variabe para incertarlo en el archivo FASTA posteriormente y luego removemos saltos de línea que puedan encontrarse al final de la cadena.
secuencia_dna = archivo_txt.read().rstrip("\n")

# Cerramos el archivo de texto.
archivo_txt.close()

# Creamos el archivo FASTA.
ruta_completa_fasta = ruta_fasta + "\\" + nombre_fasta + ".fasta" 
archivo_fasta = open(ruta_completa_fasta, "w")

# Incertamos el nombre de la secuencia y la secuencia en formato FASTA dentro de archivo .fasta.
archivo_fasta.write(">" + nombre_secuencia + "\n" + secuencia_dna)

# Cerramos el archivo FASTA
archivo_fasta.close()

# Imprimimos un mensaje que indique que el archivo se ha creado exitosamente.
print("\nEl archivo se creó exitosamente en la siguiente ruta: " + ruta_completa_fasta + "\n\n");  