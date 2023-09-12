'''
NAME

    gato.py 

VERSION

    1.0

AUTHOR

    Miguel Ángel Flores Varela

CONTACT

    mfvarela@lcg.unam.mx

DESCRIPTION

    ...

CATEGORY

    Porgramación orientada a objetos.

USAGE

    % py conteo_bases.py <path_archivo_de_entrada>
      
'''


# ===========================================================================
# =                            imports
# ===========================================================================


# ===========================================================================
# =                            Command Line Options
# ===========================================================================


# ===========================================================================
# =                            main
# ===========================================================================

class gato():
    vertebrado : True
    mamifero : True

    def __init__(self, color_de_ojos, pelaje, color_de_pelo, patron_pelaje):
        self.color_de_ojos = color_de_ojos
        self.pelaje = pelaje
        self.color_de_pelo : color_de_pelo
        self.patron_pelaje : patron_pelaje

    def maullar(self):
        print("Miauuuu")
    
    def ronronear(self):
        print("Rrrrrrrrrr")
    
    def prmear(self):
        print("Pr")

class gato_egipcio(gato):
    
