# [GitHub]
[Github]: https://github.com/lulobelardo/Nuevo_Othello

# Othello / Reversi
Trabajo Final para Programación 2 LCC realizado por:
==Luciano Manuel Belardo==
---
## Funcionamiento
Consta de dos programas, uno en C y otro en Python.
El programa en C toma un Archivo con una partida con el respectivo formato, y realiza todas las jugadas presentes. Si el juego finaliza, entonces muestra el resultado del mismo; si hubo algun error, lo muestra; y si el juego es correcto pero incompleto, entonces guarda el mismo en otro archivo tambien pasado como argumento.
Por otro lado, el programa en Python toma el archivo resultante del programa en C, y se encarga de manejar la ejecucion del juego como tal, con el tablero inicial presentado y con la idea de que el ejecutante del programa juege frente a la máquina, con el color indicado y la dificultad tambien indicada.

---
## C
### Ejecución del Programa
'_PATH_1_': Archivo contenedor del archivo origen, la partida incompleta. (`./Recursos/partida.txt`)
'_PATH_2_': Archivo destino. Donde se guardará el tablero. (`./Recursos/resultado.txt`)
#### _Windows_:
```sh
> ./C/main.exe 'PATH_1' 'PATH_2' 
```
#### _Linux_:
```sh
$ ./C/main 'PATH_1' 'PATH_2' 
```

### Ejecución de los Tests
#### _Windows_:
```sh
> ./C/tests.exe
```
#### _Linux_:
```sh
$ ./C/tests
```
---
## Python
### Ejecución del Programa
'_PATH_': Archivo con el juego incompleto. `./Recursos/resultado.txt`
'_COLOR_': `'N'` `'B'`
'_NIVEL_': `0` `1`
#### _Windows_:
```sh
> python ./Python/src/juego.py 'PATH' 'COLOR' 'NIVEL'
```
#### _Linux_:
```sh
$ python3 ./Python/src/juego.py 'PATH' 'COLOR' 'NIVEL'
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

