# Pruebas txt_a_fasta.py
| *Flores Varela Miguel Ángel* | *7 de mayo de 2023* |
|--|--|
### Introducción

Los archivos FASTA son muy utilizados en biología, en ellos se guardan secuencias de DNA, RNA o proteínas. Este tipo de archivos son de mucha utilidad en bioinformática, por lo que es necesario saber cómo realizarlos, debido a esto, esta tarea tiene la finalidad de crear archivos FASTA a partir de un archivo de texto plano que contiene una secuencia de DNA.


### Metodología

El programa esta implementado en python, y sigue el sig algoritmo

1. Desde la línea de comando el programa recibe el path del archivo de entrada, el identificador o nombre de la secuencia, el nombre del archivo de salida y el path donde se guardará este.
2. Posteriormente el programa lee la secuencia del archivo de entrada.
3. Convierte la secuencia a formato fastA.
4. Guarda la secuencia en el archivo de salida, el cual se crea en el path proporcionado en la lpinea de comando.

### Pruebas

#### Caso 1: El archivo de secuencia de entrada existe, no está vacío y contiene solo As, Ts, Gs y Cs.

- Input: data\dna.txt
- Output: results\sequence_1.fasta
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py txt_a_fasta.py ..\data\dna.txt sequence_1 sequence_1 ..\results 
```

2. El archivo de salida se crea exitosamente en la carpeta results.

#### Caso 2: El archivo de secuencia de entrada existe, no está vacío y contiene cualquier otro caracter aparte de As, Ts, Gs y Cs.

- Input: data\dna.txt 
- Output: 
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py txt_a_fasta.py ..\data\dna.txt sequence_1 sequence_1 ..\results 
```

2. El programa detecta que hay un caracter diferente a A,T, G y C, por lo que desplega el siguiente mensaje.

```
El archivo contiene caracteres no válidos.
```

#### Caso 3: El archivo de secuencia de entrada existe, no está vacío y contiene una secuencia sin As, Ts, Gs y Cs.

- Input: data\dna.txt
- Output: 
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py txt_a_fasta.py ..\data\dna.txt sequence_1 sequence_1 ..\results 
```

2. El programa detecta que no hay As, Ts, Gs ni Cs, por lo que desplega el siguiente mensaje.

```
El archivo no contiene una secuencia de DNA.
```

#### Caso 4: El archivo de secuencia de entrada existe, pero está vacío.

- Input: data\dna.txt
- Output: 
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py txt_a_fasta.py ..\data\dna.txt sequence_1 sequence_1 ..\results 
```

2. El programa detecta que el archivo de entrada está vacío y desplega el siguiente mensaje:

```
El archivo está vacío.
```

#### Caso 5: El archivo de secuencia de entrada no existe.

- Input: data\dna.txt
- Output: 
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py txt_a_fasta.py ..\data\dna.txt sequence_1 sequence_1 ..\results 
```

2. El programa detecta que el archivo de entrada no existe y desplega el siguiente mensaje:

```
No se encontró el archivo.
```
