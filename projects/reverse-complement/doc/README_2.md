# Reporte de la tarea 2: Comparar versiones y restaurara archivos
Flores Varela Miguel Ángel
28 de febrero de 2023

## Introducción
Debido a que git lleva un control de todas las versiones de los archivos que editamos es posible realizar comparaciones entre estas versiones y restaurar alguna en específico. El objeto de esta práctica es mostrar cómo se realizan estas comparaciones y restaurar una versión en específico.

## Metodología
1. Me posicioné en la carpeta data del proyecto reverse-complement y añadí la secuencia del gen araB en el archivo fasta.utilizado en la tarea anterior, posteriormente guardé este cambio y agregué un commit para ello.
```
nano e_coli.fasta
git add e_coli.fasta
git commit -m "Secuencia del gen araB añadida"
```
2. Luego realicé 3 cambios en las bases del gen araC y posteriormente guardé estos cambios.
```
nano e_coli.fasta
git add e_coli.fasta
git commit -m "Mutaciones gen araC agregadas"
```
3. Después realicé la comparación de la última versión con la penúltima y posteriormente con la antepenúltima.
```
git diff HEAD~1 e_coli.fasta
git diff HEAD~2 e_coli.fasta
```
4. Una vez realizado lo anterior procedí a restaurar la versión del archivo fastas sin las mutaciones y agregué un commit para este cambio.
```
git checkout head~1 e_coli.fasta
git commit -m "Versión sin mutaciones restaurada"
```
5. Al haber terminado esto agregué el archivo markdown a la carpeta doc del proyecto reverse-complement, le realicé un add para que git pudiera controlarlo y lo reporté con un commit.
```
git add README_2.md
git commit -m "Reporte markdown de la tarea dos agregado"
```
7. Finalmente relicé un git status para segurarme de que no faltara cofirmar algún cambio, así mismo llevé los cambios locales al servidor remoto.
```
git status
git push origin master
```

## Resultados obtenidos
+--- reverse-complement
|   +--- data
|   |   +--- e_coli.fasta
|   |   +--- sequence.txt
|   +--- doc
|   |   +--- README_1.md
|   |   +--- README_2.md
|   +--- lib
|   +--- src
|   |   +--- reverse-complement.py



## Análisis y conclusiones
Sin duda nos puede ser de gran ayuda que git controle nuestros repositorios donde realizamos cosas importantes, ya que si en algún momento realizamos un cambio del cual nos arrepientamos luego podremos enmendarlo, así mismo git nos permite realizar comparaciones entre las distintas versiones, lo que nos puede ayudar a identificar errores o bien optimizar el código de algún programa que estemos realizando.