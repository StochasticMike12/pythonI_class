'''
NAME
     contenido_AT_CG.py 

VERSION
        1.0

AUTHOR
        Miguel Ángel Flores Varela

DESCRIPTION
        Este programa pide la ruta de un archivo con una secuencia de DNA y arroja el procentaje de AT y GC de la secuencia dada.

CATEGORY
        Genómica

USAGE

    % py contenido_AT_CG.py
    
    
'''

# ===========================================================================
# =                            main
# ===========================================================================


# step 1.

# Preguntamos la ruta del archivo que contiene la secuencia de DNA.
print("\nIntroduce la ruta del archivo con la secuencia de DNA: ", end=" ")

# Guardamos la ruta del archivo en una variable para poder acceder a cualquier archivo que se desee cada vez que se abra el programa.
ruta_archivo = input()

# Abrimos el archivo con la opción de solo lectura.
archivo = open(ruta_archivo, "r")

# Accedemos al contenido del archivo para leerlo.
dna = archivo.read()

# Obtenemos la longitud de la secuencia contenida en el archivo.
longitud_dna = len(dna)

# Contamos el número de ATs y GCs en la secuencia.
AT = dna.count("A")+dna.count("T")
GC = dna.count("G")+dna.count("C")

# Realizamos las operaciones correspondientes para obtener el porcentaje de ATs y GCs.
porcentaje_AT = (100*AT)/longitud_dna
porcentaje_GC = (100*GC)/longitud_dna

# Imprimimos la ruta del archivo y el porcentaje de ATs y GCs.
print("\n\n\nArchivo de secuencia:",ruta_archivo, "\n\nPorcentaje de AT y GC:\n\nAT:", porcentaje_AT, "%\n\nGC:", porcentaje_GC, "%\n\n\n")

# Cerramos el archivo que contiene la secuencia de DNA.
archivo.close()