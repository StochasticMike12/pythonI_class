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


# Pedir la secuencia de DNA y los codones a buscar.

print("\n\nIntroduce una secuencia de DNA:")
secuencia=input()

print("\n\nIntroduce el codón de incio que desees buscar:")
c_inicio=input()

print("\n\nIntroduce el codón de término que desees buscar:")
c_termino=input()



# Obtener posiciones de codones y obtener el transcrito.

p_c_inicio=secuencia.find(c_inicio)
sec_1=secuencia[p_c_inicio:]

p_c_termino=sec_1.find(c_termino)+3
sec_2=sec_1[:p_c_termino]

transcrito_1=sec_2.replace('A','u').replace('T','a').replace('C','g').replace('G','c')
transcrito_2=transcrito_1.upper()



# Imprimir inforación correspondiente

print("\nSecuencia de DNA:", secuencia)
print("\n\nPosición del codon de inicio:", p_c_inicio) 
print("\n\nPosición donde termina el codón de paro: ", p_c_termino) 
print("\n\nFragmento que será RNA es:", transcrito_2, "\n")