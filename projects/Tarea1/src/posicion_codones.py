'''
NAME
     posicion_codones.py 

VERSION
        1.0

AUTHOR
        Miguel Ángel Flores Varela

DESCRIPTION
        Este programa arroja ciertas posiciones en específico dentro de una secuencia de DNA.

CATEGORY
        Genómica

USAGE

    % py posicion_codones.py
    
    
'''

# ===========================================================================
# =                            main
# ===========================================================================


# step 1.

# Guardar la secuencia de DNA, el codón de inicio y el codón de final en una variable cada uno.
secuencia="AAGGTACGTCGCGCGTTATTAGCCTAAT"
c_inicio="TAC"
c_termino="ATT"

# Imprimir la secuencia, la posición donde comienza el codón de inicio y la posición donde termina el codón de terminación.
print("\nSecuencia de DNA: AAGGTACGTCGCGCGTTATTAGCCTAAT\n\nPosición del codon de inicio:", secuencia.find(c_inicio), "\n\nPosición donde termina el codón de paro: ", secuencia.find(c_termino)+2, "\n\nFragmento que será RNA es: TACGTCGCGCGTT\n")

