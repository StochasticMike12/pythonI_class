# Reporte de la tarea 1: Git y gitHub : add, commits

Flores Varela Miguel Ángel
28 de febrero de 2023

## Introducción
Git es una herramienta importante para el manejo de versiones de archivos, lo cual nos puede ser muy útil en el ámbito de la bioinformática, pues nos permite llevar un control de las modificaciones y cambios que realizamos a nuestros programas. Por lo anterior es importante saber menjar esta herramienta, así que en esta práctica se muestra la manera de añadir archivos y documentar cambios.

## Metodología
1. Me posicioné en la carpeta data detro del proyecto reverse-complement y cree un archivo de texto para pegar la secuencia del gene araC de E. Coli.
`nano e_coli.fasta`
2. Después de pegar la secuencia del gene araC en el archivo utilicé un add para que git pudiera controlar el archivo.
`git add e_coli.fasta`
3. Luego usé un commit para documentar el cambio en el repositorio.
`git commit -m "Archivo fasta agregado"`
4. Para verificar que todo se ejecutó correctamente utilicé un git status.
`git status`
5. Después de verificar que todo se ejecutó correctamente procedí a llevar todos los cambios locales al servidor remoto.
`git push origin master`
6. Después moví mi archivo markdown a la carpeta doc dentro del proyecto reverse-complemente e igualmente le apliqué un add para que git pudiera controlarlo.
`git add README.md`
7. Volví a emplear un commit para documentar este cambio.
`git commit -m "Archivo markdown agregado"`
8. Finalmente volví a aplicar un git status para verificar que todo se haya ejecutado correctamente.
`git status`


## Resultados obtenido

```
+--- reverse-complement
|   +--- data
|   |   +--- e_coli.fasta
|   |   +--- sequence.txt
|   +--- doc
|   |   +--- README_1.md
|   +--- lib
|   +--- src
|   |   +--- reverse-complement.py
```


## Análisis y conclusiones
Es importante llevar un control de nuestros repositorios bajo el dominio de git para saber qué es lo que está ocurriendo exactamente con nuestros archivos, por lo que siempre es necesario documentar los cambios que realicemos en él. De esta manera es importante siempre hacer uso de commits cada vez que añadamos un nuevo documento al repositorio.
