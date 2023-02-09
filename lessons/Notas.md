# Reporte de la tarea 4: Conteos
Flores Varela Miguel Ángel
7 de septiembre de 2022

## Introducción
Analizar el genoma o proteoma de los seres vivos requiere de manejar gran cantidad de información que nos tomaría mucho tiempo manejar si utilizamos comandos de manera aislada, razón por la cual es de mucha ayuda utilizar tuberías y argumentos que nos sirvan para realizar tareas complejas como conteos y comparaciones, que a su vez nos permitan responder las preguntas biológicas de nuestro interés de la manera más sencilla, práctica, fácil y simple.

## Metodología
1. Al ingresar en el servidor me situé automáticamente en mi home, de esta manera comencé por moverme al directorio **tareas**.
 `cd tareas`
2. Dentro del directorio **tareas** creé el directorio **tarea4**.
`mkdir tarea4`
3. Me dirigí al directorio **tarea4**.
`cd tarea4`
4. Dentro del directorio **tarea4** creé los directorios **bin**, **data** y **results**.
`mkdir bin data results`
5. Me moví a la carpeta **data**.
`cd data`
6. En la carpeta **data** descargué de la la base de datos del NCBI el archivo de anotación del genoma del organismo de mi interés (en este caso la cepa *Mycobacterium leprae TN*).
`wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/195/855/GCF_000195855.1_ASM19585v1/GCF_000195855.1_ASM19585v1_genomic.gff.gz`
7. Descomprimí el archivo de anotación del organismo de mi interés.
`gunzip GCF_000195855.1_ASM19585v1_genomic.gff.gz`
8. Utilicé el comando **grep** con el argumento **-v** para excluir los comentarios del archivo de anotación, después añadí un pipe y utilicé el comando **cut** con el argumento **-f** para quedarme solo la columna de mi interés, en este caso la uno (donde se especifica el cromosoma en el que se encuentran los features), posteriormente volví a agregar otro pipe para obtener los elementos que se repiten utilizando el comando **uniq**.
`grep -v "#" GCF_000195855.1_ASM19585v1_genomic.gff | cut -f1 | uniq`
9. De esta manera obtuve un solo cromosoma con el nombre **NC 002677.1**.  Una vez que obtuve los datos anteriores procedí a averiguar el número de features anotados en el del genoma de *Mycobacterium leprae TN*, para ello comencé por excluir los comentarios como en el caso anterior, después utilicé tuberías para extraer la columna 3 (la cual contiene las features del genoma), ordenar sus elementos y obtener lineas únicas sin repeticiones (con **sort -u**) para así poder contar el número total de features diferentes en el genoma de esta cepa (utilizando **wc -l**) . 
`grep -v "#" GCF_000195855.1_ASM19585v1_genomic.gff | cut -f3 | sort -u | wc -l
`
10. Al aplicar lo anterior obtuve que son 11 los features anotados en el genoma de *Mycobacterium leprae TN*, para saber qué features eran exactamente volví a utilizar los mismos comandos y tuberías, pero removiendo el comando **wc -l** .
`grep -v "#" GCF_000195855.1_ASM19585v1_genomic.gff | cut -f3 | sort -u`
11. De esta manera obtuve que los features anotados eran: CDS, exon, gene, pseudogene, region, riboswitch, RNase P RNA, rRNA, SRP RNA, tmRNA y tRNA. Después de conocer los features en este genoma procedí a extraer el número de CDS presentes en cada cadena, para ello nuevamente utilicé tuberías con la siguiente estructura: comencé por remover los comentarios; después extrage las columnas 3 y 7 ya que en la 3 es donde aparecen los CDS y en la 7 donde se especifica la cadena en la que se encuentran; luego introduje un **sort** para ordenar los resultados; finalmente utilicé un **uniq** con el argumento **-c** para contar cuántas veces se repetía que los CDS se encontraran en la cadena **+** y cuántas en la cadena **-**.
`grep -v "#" GCF_000195855.1_ASM19585v1_genomic.gff | cut -f3,7 | sort | uniq -c`
12. Después de ejecutar lo anterior obtuve que 1376 CDS se encontraban en la cadena **+** y 1424 se encontraban en la cadena **-**. Una vez que observé lo anterior regresé al directorio **tarea4**.
`cd ../`
13. Como último paso imprimí la estructura de la carpeta **tarea4**.
`tree`


	### Código completo:
```
cd tareas
mkdir tarea4
cd tarea4
mkdir bin data results
cd data
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/195/855/GCF_000195855.1_ASM19585v1/GCF_000195855.1_ASM19585v1_genomic.gff.gz
gunzip GCF_000195855.1_ASM19585v1_genomic.gff.gz
grep -v "#" GCF_000195855.1_ASM19585v1_genomic.gff | cut -f1 | uniq
grep -v "#" GCF_000195855.1_ASM19585v1_genomic.gff | cut -f3 | sort -u | wc -l
grep -v "#" GCF_000195855.1_ASM19585v1_genomic.gff | cut -f3 | sort -u
grep -v "#" GCF_000195855.1_ASM19585v1_genomic.gff | cut -f3,7 | sort | uniq -c
cd ../
tree
```

## Resultados obtenidos


![Resultado_tarea4.png](../_resources/Resultado_tarea4.png)



## Análisis y conclusiones
En efecto las tuberías nos facilitan en trabajo en gran medida, lo que les da mucha importancia porque mediante ellas podemos realizar tareas muy complejas en una sola línea de comando, como contar genes y comparar secuencias de nucleótidos. Sin embargo, para utilizar tuberías siempre hay que tener en cuenta el orden lógico y secuencial de los comandos, ya que de no ser así al final podríamos obtener un resultado erróneo y sesgado, lo que complicaría nuestra búsqueda de respuestas a preguntas biológicas y sería de poca utilidad para la ciencia.

## Bibliografía
- National Center for Biotechnology Information. (s. f.). Mycobacterium leprae TN. National Center for Biotechnology Information. Recuperado de: https://www.ncbi.nlm.nih.gov/data-hub/genome/GCF_000195855.1/
- National Center for Biotechnology Information. (s. f.) Genome assembly ASM19585v1. National Center for Biotechnology Information. Recuperado de: https://www.ncbi.nlm.nih.gov/data-hub/genome/GCF_000195855.1/