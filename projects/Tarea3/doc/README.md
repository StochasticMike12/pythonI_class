# Reporte de la tarea 3 de python: Contenido de AT y GC
Flores Varela Miguel Ángel
29 de marzo de 2023

## Introducción
Python también nos permite realizar operaciones aritméticas y obtener porcentajes, lo que resulta bastante útil para muchas personas que necesitan realizar operaciones constantemente con sus datos. En esta tarea se obtiene el porcentaje de ATs y GCs en una secuencia de DNA contenida en un archivo en específico.

## Metodología
1. En la carpeta src dentro del repositorio Tarea3 creé el archivo contenido_AT_CG.py, en él coloqué el encabezado del programa basandome en la plantilla que nos sugirieron en cursos, posteriormente procedí a realizar mi código.
2. Comencé mi código preguntando al usuario la ruta del archivo .txt que contiene la secuencia de interés y lo guardé en una variable.
```
print("\nIntroduce la ruta del archivo con la secuencia de DNA:", end=" ")
ruta_archivo = input()
```
3. Luego abrí el archivo utilizando la variable donde guardé la dirección del archivo .txt, guardé en una varibale el string contenido el el archivo y posteriormente obtuve su longitud. Para abrir el archivo utilicé el argumento "r" para indicar que el contenido sería leído exclusivamente y al almacenar el string en la varibale dna utilicé el método .rstrip() para eliminar el salto de línea que se encontraba en el archivo sugerido dna.txt (que se encuentra en la carpeta data de Tarea1), pues de no hacerlo sesgaría los resultados.
```
archivo = open(ruta_archivo, "r")
dna = archivo.read().rstrip("\n")
longitud_dna = len(dna)
```
4. Luego conté el número de ATs y GCs almacenandonos en una varaible cada uno.
```
AT = dna.count("A")+dna.count("T")
GC = dna.count("G")+dna.count("C")
```
5. Procedí a obtener los porcentajes de ATs y GCs en el string.
```
porcentaje_AT = (100*AT)/longitud_dna
porcentaje_GC = (100*GC)/longitud_dna
```
6. Después imprimí la ruta del archivo .txt con el que trabajamos, así como el procentaje de ATs y GCs del string que contenía. De igual manera, por buenas prácticas, cerré el archivo .txt.
```
print("\n\n\nArchivo de secuencia: " + ruta_archivo + "\n\nPorcentaje de AT y GC:\n\nAT:", porcentaje_AT, "%\n\nGC:", porcentaje_GC, "%\n\n\n")
archivo.close()
```
7. Finalmente corrí mi script en la terminal de PowerShell.
```
py contenido_AT_CG.py
```

## Resultados obtenidos
- Los resultados que obtuve al correr mi script en la terminal de PowerShell con la secuencia sugerida en la tarea fue el siguiente:
```
Introduce la ruta del archivo con la secuencia de DNA: ..\data\dna.txt



Archivo de secuencia: ..\data\dna.txt

Porcentaje de AT y GC:

AT: 51.07398568019093 %

GC: 48.92601431980907 %
```
- Y mi repositorio Tarea3 quedó de la siguiente manera:
```
+--- Tarea2
|   +--- data
|   +--- doc
|   |   +--- README.md
|   +--- lib
|   +--- results
|   +--- src
|   |   +--- contenido_AT_CG.py
```

## Análisis y conclusiones
Obtener porcentajes es una tarea de mucha ayuda en campos como la genómica, por lo que es importante saber cómo obtenerlos en lenguages como python. Sin duda python es muy fácil de utilizar y sus métodos nos facilitan la obtención de porcentajes.