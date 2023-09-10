# Pruebas piedra-papel-tijera.py
| *Flores Varela Miguel Ángel* | *9 de septiembre de 2023* |
|--|--|

### Introducción

Pyhon nos permite realizar múltiples cosas, tales como generar valores aleatorio, crear loops y ciclos, crear condiciones complejas, etc. Debido a su interactividad este lenguage suele ser muy utilizado en el desarrollo de juegos, por lo que en esta ocasión el objetivo es realizar un juego iteractivo aplicando lo visto en clase respecto a conidiconales y ciclos.


### Metodología

El programa esta implementado en python, y sigue el sig algoritmo

1. Pide al usuario su nombre y opción (de entre piedra, papel o tijera).
2. El programa obtiene una opción en base a valores aleatorios, para competir con el usuario.
3. Se evalúan las respuestas del usuario y la computadora de acuerdo a ciertas condicione o reglas preestablecidas.
4. Se obtiene un resultado, anunciando si hubo empate o ganó alguien, y de ser así se muestra quién gano.
5. El programa pregunta al usuario si quiere volver a jugar, en dado caso de no ingresar una de las opciones definidas su vueve a preguntar hasta introducir una opción definida.


### Pruebas

#### Caso 1: El usuario pierde.

- Input: 
- Output:
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py piedra-papel-tijera.py
```

2. El programa pedirá lo siguiente:

```
Bienvenido al juego de piedra, papel o tijera.

Dame tu nombre: Usuario

Miguel, a la de 3, teclea tu opción (piedra, papel o tijera): piedra
```

3. El programa obtiene una opción aleatoria y la compara con la del usuario, obteniendo así un resultado.

```
Usuario: piedra

Computadora: tijera


¡Felicidades! Ganaste
```

4. El programa pregunta al usuario si desea volver a jugar, en caso de que se quiera volver a jugar reanuda el juego, en cado de que no se quiera volver a jugar termina el programa y en caso de ingresar una opción no especificada vuelve a preguntar hasta obtener una opción definida.
```
Introduce el número de la opción que desees


¿Quieres volver a jugar?

Sí(s)

No(n)
```

```
Introduce una opción válida


¿Quieres volver a jugar?

Sí(s)

No(n)
```

#### Caso 2: El usuario pierde

- Input: 
- Output:
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py piedra-papel-tijera.py
```

2. El programa pedirá lo siguiente:

```
Bienvenido al juego de piedra, papel o tijera.

Dame tu nombre: Usuario

Miguel, a la de 3, teclea tu opción (piedra, papel o tijera): piedra
```

3. El programa obtiene una opción aleatoria y la compara con la del usuario, obteniendo así un resultado.

```
Usuario: piedra

Computadora: pepel


Lo siento, perdiste
```

4. El programa pregunta al usuario si desea volver a jugar, en caso de que se quiera volver a jugar reanuda el juego, en cado de que no se quiera volver a jugar termina el programa y en caso de ingresar una opción no especificada vuelve a preguntar hasta obtener una opción definida.
```
Introduce el número de la opción que desees


¿Quieres volver a jugar?

Sí(s)

No(n)
```

```
Introduce una opción válida


¿Quieres volver a jugar?

Sí(s)

No(n)
```

#### Caso 3: El usuario y la computadora quedan empates

- Input: 
- Output:
- Descripción:

1. Se ejecuta el programa desde linea de comando

```{python}
py piedra-papel-tijera.py
```

2. El programa pedirá lo siguiente:

```
Bienvenido al juego de piedra, papel o tijera.

Dame tu nombre: Usuario

Miguel, a la de 3, teclea tu opción (piedra, papel o tijera): piedra
```

3. El programa obtiene una opción aleatoria y la compara con la del usuario, obteniendo así un resultado.

```
Usuario: piedra

Computadora: piedra


¡Empates!
```

4. El programa pregunta al usuario si desea volver a jugar, en caso de que se quiera volver a jugar reanuda el juego, en cado de que no se quiera volver a jugar termina el programa y en caso de ingresar una opción no especificada vuelve a preguntar hasta obtener una opción definida.
```
Introduce el número de la opción que desees


¿Quieres volver a jugar?

Sí(s)

No(n)
```

```
Introduce una opción válida


¿Quieres volver a jugar?

Sí(s)

No(n)
```
