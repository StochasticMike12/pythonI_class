# Pruebas posicion_codones.py
| *Flores Varela Miguel Ángel* | *9 de septiembre de 2023* |
|--|--|

## Introducción
Con frecuencia necesitamos localizar los codones de inicio y de paro para saber dónde inicia un trnascrito. Python nos facilita la tarea de encontrar ciertos patrones de caracteres dentro de una cadena de caracteres, para esta tarea resulta fundamental el uso del método .find().

## Metodología

El programa esta implementado en python, y sigue el siguiente algoritmo:

1. El programa recibe desde la línea de comando el path del archivo de entrada donde se encuentra la secuencia de DNA, así como el codón de inicio y de paro con el que se desee trabajar.
2. Verifica que el archivo exista, que no esté vacío y que contenga solo ATGCs.
3. El programa identifica la posición del codón de inicio y de paro, posteriormente proporciona el transcrito de RNA.


### Pruebas

#### Caso 1: El archivo de secuencia de entrada existe, no está vacío y contiene solo As, Ts, Gs y Cs.

- Input: data\dna.txt
- Output:
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py posicion_codones.py ..\data\dna.txt TAC ATT
```

2. El programa calcula el número de As. Ts, Gs y Cs en la secuencia dentro del archivo de entrada.

```
Secuencia de DNA: ...


Posición del codon de inicio: ...


Posición donde termina el codón de paro: ...


Fragmento que será RNA es: ...
```

#### Caso 2: El archivo de secuencia de entrada existe, no está vacío y contiene cualquier otro caracter aparte de As, Ts, Gs y Cs.

- Input: data\dna.txt 
- Output: 
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py posicion_codones.py ..\data\dna.txt TAC ATT
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
py posicion_codones.py ..\data\dna.txt TAC ATT
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
py posicion_codones.py ..\data\dna.txt TAC ATT
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
py posicion_codones.py ..\data\dna.txt TAC ATT
```

2. El programa detecta que el archivo de entrada no existe y desplega el siguiente mensaje:

```
No se encontró el archivo.
```
