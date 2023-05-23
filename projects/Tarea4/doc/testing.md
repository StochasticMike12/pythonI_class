## Pruebas del Convertidor de formato raw a fastA

Flores Varela Miguel Ángel 29 de marzo de 2023

### Introducción

Los archivos FASTA son muy utilizados en biología, en ellos se guardan secuencias de DNA, RNA o proteínas. 
Este tipo de archivos son de mucha utilidad en bioinformática, por lo que es necesario saber cómo realizarlos, debido a esto, esta tarea tiene la finalidad de crear archivos FASTA a partir de un archivo de texto plano que contiene una secuencia de DNA.

### Metodología

El programa esta implementado en python, y sigue el sig algoritmo

1. El programa pide el archivo con la secuencia en formato raw (path y nombre)
2. Se pide el identificador o nombre de la secuencia
3. El programa pide el nombre del archivo de salida (path y nombre)
4. Se lee la secuencia del archivo de entrada
5. Se convierte la secuencia a formato fastA
6. Se guarda la secuencia en el archivo de salida


### Pruebas

#### Caso 1: El archivo de secuencia de entrada existe y se genera la secuencia en fastA

Input: data/dna.txt
Output: results/sequence_1.fasta
Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py txt_a_fasta.py
```

2. El programa pedirá lo siguiente:

```
Introduce la ruta del archivo .txt que contiene la secuencia de DNA que desees convertir a formato FASTA: ..\data\dna.txt

Introduce el nombre de la secuencia que desees convertir a formato FASTA: sequence_1

Introduce el nombre que desees que tenga que archivo FASTA (sin la extensión .fasta): sequence_1

Introduce la ruta donde desees que se cree el archivo FASTA: ..\results

El archivo se creó exitosamente en la siguiente ruta: ..\results\sequence_1.fasta
```

#### Caso 2: El archivo de secuencia de entrada NO existe

Input: 
Output: 
Descripción:

#### Caso 3: El archivo de secuencia de entrada no contiene datos

Input: 
Output: 
Descripción:

#### Caso 4: El archivo de secuencia de entrada no contiene secuencia de dna

Input: 
Output: 
Descripción: