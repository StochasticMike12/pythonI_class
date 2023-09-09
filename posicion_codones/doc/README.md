# Reporte de la tarea 1 de python: Secuencia de RNA
Flores Varela Miguel Ángel
29 de marzo de 2023

## Introducción
Con frecuencia necesitamos localizar los codones de inicio y de paro para saber dónde inicia un trnascrito. Python nos facilita la tarea de encontrar ciertos patrones de caracteres dentro de una cadena de caracteres, para esta tarea resulta fundamental el uso del método .find().

## Metodología
1. En la carpeta src dentro del repositorio Tarea1 creé el archivo posicion_codones.py, en él coloqué el encabezado del programa basandome en la plantilla que nos sugirieron en cursos, posteriormente procedí a realizar mi código.
2. Comencé mi código almacenando en una varible la secuencia establecida en la tarea, luego guardé los codones de inicio y de final cada uno en una variable.
```
secuencia="AAGGTACGTCGCGCGTTATTAGCCTAAT"
c_inicio="TAC"
c_termino="ATT"
```
3. Después imprimí la posición donde comenzaba el codón de inicio, la posición donde terminada el codón de terminación y el fragmento que sería transcrito a RNA.
```
print("\nSecuencia de DNA: AAGGTACGTCGCGCGTTATTAGCCTAAT\n\nPosición del codon de inicio:", secuencia.find(c_inicio), "\n\nPosición donde termina el codón de paro: ", secuencia.find(c_termino)+2, "\n\nFragmento que será RNA es: TACGTCGCGCGTT\n")
```
4. Finalmente corrí mi script desde la terminal de PowerShell.
```
py .\posicion_codones.py
```

## Resultados obtenidos
- Los resultados que obtuve al correr mi script en la terminal de PowerShell fue el siguiente:
```
Secuencia de DNA: AAGGTACGTCGCGCGTTATTAGCCTAAT

Posición del codon de inicio: 4

Posición donde termina el codón de paro:  19

Fragmento que será RNA es: TACGTCGCGCGTT
```
- Y mi repositorio Tarea1 quedó de la siguiente manera:
```
+--- Tarea2
|   +--- data
|   +--- doc
|   |   +--- README.md
|   +--- lib
|   +--- results
|   +--- src
|   |   +--- posicion_codones.py
```

## Análisis y conclusiones
Python es un lenguage bastante interactivo y fácil de utilizar, cuenta con diversos métodos y funciones que nos ayudan a realizar tareas de manera más simple, por lo que cualquier puede aprenderlo rápidamente. En el caso de la genómica y transcriptómica las funciones como .find() nos pueden ser de mucha ayuda en los casos en los que queramos encontrar cierta secuencia en específico en un fragmento de DNA o RNA.