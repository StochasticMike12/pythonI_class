# Pruebas conteo_bases.py
| *Flores Varela Miguel Ángel* | *9 de septiembre de 2023* |
|--|--|

### Introducción

Contar el número de As, Ts, Gs y Cs es de ayuda en tareas como determinar la estabilidad de un primer para PCR. Para realizar el conteo de cada uno de estos nos puede ser de mucha ayuda los métodos de python, como es el caso de .cont(), el cual es fundamental para la realización de esta tarea.


### Metodología

El programa esta implementado en python, y sigue el siguiente algoritmo:

1. El programa recibe desde la línea de comando el path del archivo de entrada donde se encuentra la secuencia de DNA.
2. Verifica que el archivo exista, que no esté vacío y que contenga solo ATGCs.
3. El programa cuenta cuántas veces aparece cada una de las bases nitrogenadas en la secuencia.


### Pruebas

#### Caso 1: El archivo de secuencia de entrada existe, no está vacío y contiene solo As, Ts, Gs y Cs.

- Input: data/dna.txt
- Output:
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py conteo_bases.py ..\data\dna.txt
```

2. El programa calcula el número de As. Ts, Gs y Cs en la secuencia dentro del archivo de entrada.

```
El total por base es:

A: ...
T: ...
C: ...
G: ...
```

#### Caso 2: El archivo de secuencia de entrada existe, no está vacío y contiene cualquier otro caracter aparte de As, Ts, Gs y Cs.

- Input: data/dna.txt 
- Output: 
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py conteo_bases.py ..\data\dna.txt
```

2. El programa detecta que hay un caracter diferente a A,T, G y C, por lo que desplega el siguiente mensaje.

```
El archivo contiene caracteres no válidos.
```

#### Caso 3: El archivo de secuencia de entrada existe, no está vacío y contiene una secuencia sin As, Ts, Gs y Cs.

- Input: data/dna.txt
- Output: 
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py conteo_bases.py ..\data\dna.txt
```

2. El programa detecta que no hay As, Ts, Gs ni Cs, por lo que desplega el siguiente mensaje.

```
El archivo no contiene una secuencia de DNA.
```

#### Caso 4: El archivo de secuencia de entrada existe, pero está vacío.

- Input: data/dna.txt
- Output: 
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py conteo_bases.py ..\data\dna.txt
```

2. El programa detecta que el archivo de entrada está vacío y desplega el siguiente mensaje:

```
El archivo está vacío.
```

#### Caso 5: El archivo de secuencia de entrada no existe.

- Input: data/dna.txt
- Output: 
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py conteo_bases.py ..\data\dna.txt
```

2. El programa detecta que el archivo de entrada no existe y desplega el siguiente mensaje:

```
No se encontró el archivo.
```
