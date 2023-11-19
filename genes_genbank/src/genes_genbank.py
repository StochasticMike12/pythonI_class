'''
NAME

    genes_genbank.py 

VERSION
    1.0.0

AUTHOR
    Miguel Ángel Flores Varela

CONTACT

    mfvarela@lcg.unam.mx

DESCRIPTION

    Este programa obtiene determinados metadatos de un archivo genbak,
    así como el nombre, secuencia de DNA, secuencia de RNA y secuencia 
    proteica de determinados genes especificados por el usuario.

CATEGORY

    Genómica

USAGE

    % py genes_genbank.py <path_archivo_de_entrada> <lista_genes>
  
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

parser= argparse.ArgumentParser(description='Este programa obtiene determinados metadatos de un archivo genbak, así como el nombre, secuencia de DNA, secuencia de RNA y secuencia proteica de determinados genes especificados por el usuario. El programa recibe como argumentos la ruta del archivo de entrada seguido de la lista de genes de los cuales se desea extraer información, estos deben ser ingresados de la siguiente manera: X,L,..,Z . En caso de ser solo un gen debe ingresarse solo el nombre de este gen (X).')

parser.add_argument('Path',
                    metavar='path',
                    type=str,
                    help='El path del archivo')

parser.add_argument('Genes',
                    metavar='genes',
                    type=str,
                    help='Lista de genes a los que se les extraerá información')


# Ejecutar método parse_args()
args = parser.parse_args()



# ===========================================================================
# =                            functions
# ===========================================================================

# Convertir una lista a una cadena de caracteres excluyendo los símbolos "['']"

def list_to_str(list):
    string=str(list)
    end=len(string)-2
    string=string[2:end]
    return string


# Convertir una cadena de caracteres a una lista

def str_to_list(genes_str):
    genes_list=[]
    for gene in genes_str:
        if gene==",":
            next
        else:
            genes_list.append(gene)
    return genes_list


# Obtener los datos deseados

def parser(file,genes):
    
    #Verificar que el archivo ingresado exista
    try:
        for gb_record in SeqIO.parse(file, "genbank"):
            country=list_to_str(gb_record.features[0].qualifiers['country'])
    except FileNotFoundError:
            print("No se encontró el archivo ingresado.")
    else:

            # verificar que el metadato isolate exista            
            try:
                isolate=list_to_str(gb_record.features[0].qualifiers['isolate'])
                print("\nFile:", file,"\nOrganism:",gb_record.annotations['organism'],"\nDate:",gb_record.annotations['date'],
                    "\nCountry:",country,"\nIsolate",isolate)
            except KeyError:
                print("\nEl archivo no posee el metadato isolate\n\nFile:", file,"\nOrganism:",gb_record.annotations['organism'],"\nDate:",gb_record.annotations['date'],
                "\nCountry:",country)
            
            # Extarer la información deseada de la lista de genes
            finally:
                n=1
                genes=str_to_list(genes)
                for gene in genes:
                    for feature in gb_record.features:
                        if (feature.type == 'gene'):
                            gene_name=list_to_str(feature.qualifiers['gene'])
                            if gene_name==gene:
                                start=feature.location.nofuzzy_start
                                end=feature.location.nofuzzy_end
                                DNA=gb_record.seq[start:end]
                                RNA=DNA.transcribe()
                                Protein=DNA.translate(to_stop=True)
                                print("\n> Gen",n,":", gene_name,"\n> DNA:", DNA,"\n> RNA:",RNA,"\n> Protein:",Protein,"\n")
                                n+=1



# ===========================================================================
# =                            main
# ===========================================================================

# Enviar los datos ingresados a la función que extraerá la información de los genes
parser(args.Path, args.Genes)