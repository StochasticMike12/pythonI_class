# Pruebas contenido_AT_GC.py
| *Flores Varela Miguel Ángel* | *9 de septiembre de 2023* |
|--|--|

### Introducción

Python también nos permite realizar operaciones aritméticas y obtener porcentajes, lo que resulta bastante útil para muchas personas que necesitan realizar operaciones constantemente con sus datos. En esta tarea se obtiene el porcentaje de ATs y GCs en una secuencia de DNA contenida en un archivo en específico.


### Metodología

El programa está implementado en python, y sigue el siguiente algoritmo:

1. El programa recibe desde la línea de comando el path del archivo de entrada donde se encuentra la secuencia de DNA.
2. Verifica que el archivo exista, que no esté vacío y que contenga solo ATGCs.
3. El programa obtiene el porcenja de AT y GC de la secuencia contenida en el archivo de entrada.

### Pruebas

#### Caso 1: El archivo de secuencia de entrada existe, no está vacío y contiene solo As, Ts, Gs y Cs.

- Input: data\dna.txt
- Output:
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py contenido_AT_GC.py ..\data\dna.txt
```

2. El programa obtiene el porcentaje de AT y GC de la secuencia.

```
Porcentaje de AT y GC:

AT: ... %

GC: ... %
```

#### Caso 2: El archivo de secuencia de entrada existe, no está vacío y contiene cualquier otro caracter aparte de As, Ts, Gs y Cs.

- Input: data\dna.txt 
- Output: 
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py contenido_AT_GC.py ..\data\dna.txt
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
py contenido_AT_GC.py ..\data\dna.txt
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
py contenido_AT_GC.py ..\data\dna.txt
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
py contenido_AT_GC.py ..\data\dna.txt
```

2. El programa detecta que el archivo de entrada no existe y desplega el siguiente mensaje:

```
No se encontró el archivo.
```
