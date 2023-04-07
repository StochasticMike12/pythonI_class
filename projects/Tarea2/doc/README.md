# Reporte de la tarea 2 de python: Contar As, Ts, Gs, Cs
Flores Varela Miguel Ángel
29 de marzo de 2023

## Introducción
Contar el número de As, Ts, Gs y Cs es de ayuda en tareas como determinar la estabilidad de un primer para PCR. Para realizar el conteo de cada uno de estos nos puede ser de mucha ayuda los métodos de python, como es el caso de .cont(), el cual es fundamental para la realización de esta tarea.

## Metodología
1. En la carpeta src dentro del repositorio Tarea2 creé el archivo conteo_bases.py, en él coloqué el encabezado del programa basandome en la plantilla que nos sugirieron en cursos, posteriormente procedí a realizar mi código.
2. Comencé mi código preguntando al usuario la secuencia de DNA en la que se desee contar el número de cada base nitrogenada.
```
print("\nIntroduce la secuencia de DNA:", end=" ")
secuencia=input()
```
3. Después imprimí el número de cada base nitrogenada haciendo uso de la función .count().
```
print("\n\nEl total por base es:\n\nA:",secuencia.count('A'),"\nT:",secuencia.count('T'),"\nC:",secuencia.count('C'),"\nG:",secuencia.count('G'),"\n")
```
4. Finalmente corrí mi script desde la terminal de PowerShell.
```
py .\conteo_bases.py
```

## Resultados obtenidos
- Los resultados que obtuve al correr mi script en la terminal de PowerShell con la secuencia sugerida en la tarea fue el siguiente:
```
Introduce la secuencia de DNA: AGCTTTTCATTC


El total por base es:

A: 2
T: 6
C: 3
G: 1
```
- Y mi repositorio Tarea2 quedó de la siguiente manera:
```
+--- Tarea2
|   +--- data
|   +--- doc
|   |   +--- README.md
|   +--- lib
|   +--- results
|   +--- src
|   |   +--- conteo_bases.py
```

## Análisis y conclusiones
Python es muy útil para contar en número de caracteres en una cadena de caracteres, el método .count() nos permite realizar esta tarea de manera muy fácil y sencilla. En campos como la biología molecular, genómica y transcriptómica nos puede ser bastante útil lo mencionado anteriormente, pues nos permitiría conocer la estabilidad de una secuencia en específico, así como su peso molecular o su longitud, entre otras cosas.