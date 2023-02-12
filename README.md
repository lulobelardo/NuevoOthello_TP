# [GitHub]
[Github]: https://github.com/lulobelardo/Nuevo_Othello

# Othello / Reversi
Trabajo Final para Programación 2 LCC 2022 realizado por:
*Luciano Manuel Belardo*

---
## Funcionamiento
Consta de dos programas, uno en C y otro en Python.

---
## Othello en C
El programa en C toma dos archivos como argumento por consola. El primero contiene una partida de Othello con su respectivo formato, y realiza todas las jugadas presentes. *Si el juego finaliza*, entonces muestra el resultado del mismo; *si hubo algun error*, dice cuál es; y *si el juego es correcto pero incompleto*, entonces guarda el tablero resultante de haber realizado todas las jugadas escritas en el segundo archivo, seguido del color que le corresponde jugar.

### Ejecución del Programa
### Make

#### _Windows_:
```sh
mingw32-make.exe -C ./C
```
#### _Linux_:
```sh
make -C ./C
```
Luego de ejecutar el make:
- PATH/1: Archivo contenedor del archivo origen, la partida incompleta. (`./Recursos/partida.txt`)
- PATH/2: Archivo destino. Donde se guardará el tablero. (`./Recursos/resultado.txt`)
#### _Windows_:
```sh
./C/main.exe PATH/1 PATH/2 
```
#### _Linux_:
```sh
./C/main PATH/1 PATH/2 
```

### Ejecución de los Tests
#### _Windows_:
```sh
./C/tests.exe
```
#### _Linux_:
```sh
./C/tests
```
---
## Othello en Python
El programa en Python toma el archivo resultante del programa en C (contenedeor del tablero), y se encarga administrar el juego entre el usuario y la computadora, Ademas, tambien toma como argumento el COLOR que desea ser el usuario y el nivel en el que se desea que juegue la computadora.
- Nivel 0: el programa debe determinar cuáles son las jugadas posibles y en forma aleatoria elegir una de ellas.
- Nivel 1: el programa elige la jugada a realizar analizando cuál de ellas genera mayores cambios en el tablero (da vuelta más fichas del contrario).

A continuacion, se comienza a jugar hasta que la partida finaliza y muestra los resultados finales.
### Ejecución del Programa
- _PATH_: Archivo con el juego incompleto. `./Recursos/resultado.txt`
- _COLOR_: `'N'` `'B'`
- _NIVEL_: `0` `1`
#### _Windows_:
```sh
python ./Python/src/juego.py PATH COLOR NIVEL
```
#### _Linux_:
```sh
python3 ./Python/src/juego.py PATH COLOR NIVEL
```

### Ejecución de los Tests
#### _Windows_:
```sh
python -m pytest
```
#### _Linux_:
```sh
python3 -m pytest
```