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


# step

print("\nIntroduce la ruta del archivo con la secuencia de DNA: ", end=" ")
ruta_archivo = input()
archivo = open(ruta_archivo, "r")
dna = archivo.read()
longitud_dna = len(dna)
AT = dna.count("A")+dna.count("T")
GC = dna.count("G")+dna.count("C")
porcentaje_AT = (100*AT)/longitud_dna
porcentaje_GC = (100*GC)/longitud_dna
print("\n\n\nArchivo de secuencia:",ruta_archivo, "\n\nPorcentaje de AT y GC:\n\nAT:", porcentaje_AT, "\n\nGC:", porcentaje_GC, "\n\n\n")
archivo.close()