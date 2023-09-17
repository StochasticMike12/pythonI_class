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

    Este programa permite ingresar los datos de un gato y realizar ciertas
    funciones dependiendo del tipo de gato.

CATEGORY

    Porgramación orientada a objetos.

USAGE

    % py gato.py <nombre_gato> <raza_de_gato> <color_de_ojos> <tipo_de_pelaje> <patron_de_pelaje> <color_de_pelaje> <funcion>

    EXAMPLE

    % py gato.py tatis gato_siames verdes esponjoso manchado cafe_con_gris maullar
      
'''


# ===========================================================================
# =                            imports
# ===========================================================================

# Importar librería para obtener argumentos de la línea de comandos.
import argparse


# ===========================================================================
# =                            Command Line Options
# ===========================================================================

# Describir el programa.
parser = argparse.ArgumentParser(description='Introduce los datos de un gato')


# Definir los argumentos.
parser.add_argument('Nombre',
                    metavar='nombre',
                    type=str,
                    help='Nombre del gato')

parser.add_argument('Raza',
                    metavar='raza',
                    type=str,
                    help='Raza del gato')

parser.add_argument('Ojos',
                    metavar='ojos',
                    type=str,
                    help='Color de ojos del gato')

parser.add_argument('Pelaje',
                    metavar='pelaje',
                    type=str,
                    help='Tipo de pelaje del gato')

parser.add_argument('Patron',
                    metavar='patron',
                    type=str,
                    help='Patrón de pelaje del gato')

parser.add_argument('Color',
                    metavar='color',
                    type=str,
                    help='Color(es) del pelaje del gato')

parser.add_argument('Funcion',
                    metavar='funcion',
                    type=str,
                    help='Función a realizar del gato')

# Ejecutar método parse_args()
args = parser.parse_args()


# ===========================================================================
# =                            main
# ===========================================================================

# Definir la clase padre
class gato():
    vertebrado = True
    mamifero = True
    placentario = True
    def __init__(self, color_de_ojos, tipo_de_pelaje, patron_de_pelaje, color_de_pelaje): 
        self.color_de_ojos = color_de_ojos
        self.tipo_de_pelaje = tipo_de_pelaje
        self.patron_de_pelaje = patron_de_pelaje
        self.color_de_pelaje = color_de_pelaje
    def maullar(self):
        print("Miau")
    def ronronear(self):
        print("Rrrrrrr")
    def prrmear(self):
        print("Prrrrrr")

#Defiir las subclases
class gato_siames(gato):
    def prrmear(self):
        print("Prrmiau")
    def maullar(self):
        print("Miou")

class gato_egipcio(gato):
    def prrmear(self):
        print("Prrmiou")

# Asignar argumentos a variables
nombre = args.Nombre
raza = args.Raza
ojos = args.Ojos
pelaje = args.Pelaje
patron = args.Patron
color = args.Color
funcion = args.Funcion

# Evaluar a qué subcalse pertenece el objeto para acceder a sus atributos y ejecutar sus funciones.
if raza == "gato_siames":
    nombre = gato_siames(ojos, pelaje, patron, color)
    print(nombre.__dict__)
    if funcion == "prrmear":
        nombre.prrmear()
    elif funcion == "maullar":
        nombre.maullar()
    elif funcion == "ronronear":
        nombre.ronronear()
elif raza == gato_egipcio:
    nombre = gato_egipcio(ojos, pelaje, patron, color)
    print(nombre.__dict__)
    if funcion == "prrmear":
        nombre.prrmear()
    elif funcion == "maullar":
        nombre.maullar()
    elif funcion == "ronronear":
        nombre.ronronear()