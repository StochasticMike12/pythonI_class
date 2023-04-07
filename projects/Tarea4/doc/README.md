# Reporte de la tarea 4 de python: From raw to FastA
Flores Varela Miguel Ángel
29 de marzo de 2023

## Introducción
Los archivos FASTA son muy utilizados en biología, en ellos se guardan secuencias de DNA, RNA o proteínas. Este tipo de archivos son de mucha utilidad en bioinformática, por lo que es necesario saber cómo realizarlos, debido a esto, esta tarea tiene la finalidad de crear archivos FASTA a partir de un archivo de texto plano que contiene una secuencia de DNA.

## Metodología
1. En la carpeta src dentro del repositorio Tarea4 creé el archivo txt_a_fasta.py, en él coloqué el encabezado del programa basandome en la plantilla que nos sugirieron en cursos, posteriormente procedí a realizar mi código.
2. Comencé mi código preguntando al usuario la ruta del archivo .txt que contiene la secuencia de interés y lo guardé en una variable.
```
print("\nIntroduce la ruta del archivo .txt que contiene la secuencia de DNA que desees convertir a formato FASTA:", end=" ")
ruta_archivo = input()
```
3. Luego pregunté al usuario el nombre de la secuencia de DNA y lo guardé en una variable.
```
print("\nIntroduce el nombre de la secuencia que desees convertir a formato FASTA:", end=" ")
nombre_secuencia = input()
```
4. Después pregunté al usuario el nombre que desee que tenga el archivo de salida .fasta y lo guardé en una variable.
```
print("\nIntroduce el nombre que desees que tenga que archivo FASTA (sin la extensión .fasta):", end=" ")
nombre_fasta = input()
```
5. También pregunté al usuario la ruta donde deseara que se creara el archivo FASTA y lo guardé en una variable.
```
print("\nIntroduce la ruta donde desees que se cree el archivo FASTA:", end=" ")
ruta_fasta = input()
```
6. De esta manera procedí a abrir el archivo .txt utilizando el argumento "r" de lectura y la variable donde se guardó su ruta. Guardé el contenido del archivo en una varible y eliminé el salto de línea que contenía el string del archivo dna.txt (que se encuentra en la carpeta data de Tarea4). Además por buenas prácticas, al terminar de utilizar el archivo lo cerré.
```
archivo_txt = open(ruta_archivo, "r")
secuencia_dna = archivo_txt.read().rstrip("\n")
archivo_txt.close()
```
7. Luego utilicé una varaible para construir la ruta completa donde se crearía el archivo FASTA y posteriormente hice uso de ella para crearlo. Al crear el archivo FASTA hice uso del argumento "w" para escribir sobre él.
```
ruta_completa_fasta = ruta_fasta + "\\" + nombre_fasta + ".fasta" 
archivo_fasta = open(ruta_completa_fasta, "w")
```
8. Utilicé el método .write() para escribir en el archivo FASTA, comencé por agregar un ">" seguido de concatenar el nombre de la secuencia, un salto de línea y la secuencia de DNA. Una vez realizado lo anterior procedí a cerrar el archivo.
```
archivo_fasta.write(">" + nombre_secuencia + "\n" + secuencia_dna)
archivo_fasta.close()
```
9. Para saber que todo ocurrió correctamente imprimí un mensaje que indicara que el archivo se creó exitosamente.
```
print("\nEl archivo se creó exitosamente en la siguiente ruta: " + ruta_completa_fasta + "\n\n");  
```
10. Finalmente corrí mi script en la terminal de PowerShell.
```
py txt_a_fasta.py
```

## Resultados obtenidos
- Los resultados que obtuve al correr mi script en la terminal de PowerShell con la secuencia sugerida en la tarea fue el siguiente:
```
Introduce la ruta del archivo .txt que contiene la secuencia de DNA que desees convertir a formato FASTA: ..\data\dna.txt

Introduce el nombre de la secuencia que desees convertir a formato FASTA: sequence_1

Introduce el nombre que desees que tenga que archivo FASTA (sin la extensión .fasta): sequence_1

Introduce la ruta donde desees que se cree el archivo FASTA: ..\results

El archivo se creó exitosamente en la siguiente ruta: ..\results\sequence_1.fasta
```
- Y mi repositorio Tarea4 quedó de la siguiente manera:
```
+--- Tarea2
|   +--- data
|   +--- doc
|   |   +--- README.md
|   +--- lib
|   +--- results
|   |   +--- sequence_1.fasta
|   +--- src
|   |   +--- txt_a_fasta.py
```

## Análisis y conclusiones
Saber cómo procesar archivos de texto plano para procesar datos y arrojar datos o archivos de salida es de gran importancia, python nos permiten manipular archivos .txt de manera fácil y sencilla, por lo que podemos procesar una cantidad considerable de estos archivos. Esto resulta muy útil para el trabajo bioinformático y, ahora que ya sabemos cómo crear archivos FASTA, podemos haccerlo libremente para procesar de manera más ordenada y eficiente nuestros datos.