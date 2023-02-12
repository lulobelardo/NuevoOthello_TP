# [GitHub]

# Othello
Trabajo Final Othello para Programación 2 realizado por:
- Luciano Belardo
---
## Funcionamiento
Consta de dos programas, uno en C y otro en Python.
El programa en C toma un Archivo con una partida con el respectivo formato, y realiza todas las jugadas presentes. Si el juego finaliza, entonces muestra el resultado del mismo; si hubo algun error, lo muestra; y si el juego es correcto pero incompleto, entonces guarda el mismo en otro archivo tambien pasado como argumento.
Por otro lado, el programa en Python toma el archivo resultante del programa en C, y se encarga de manejar la ejecucion del juego como tal, con el tablero inicial presentado y con la idea de que el ejecutante del programa juege frente a la máquina, con el color indicado y la dificultad tambien indicada.

---
## Python
### Ejecución del Programa

#### _Windows_:
```sh
python ./Python/src/juego.py ./Recursos/resultado.txt _COLOR_ _NIVEL_
```
_COLOR_: 'N' - 'B'
_NIVEL_: 0 - 1
#### _Linux_:
```sh
python3 ./Python/src/othello.py
```
---
### Ejecución de los Tests
#### _Windows_:
```sh
python -m pytest
```
#### _Linux_:
```sh
python3 -m pytest
```
### C
#### _Windows_:
```sh
python -m pytest
```
#### _Linux_:
```sh
python3 -m pytest
```

[Github]: https://github.com/lulobelardo/Nuevo_Othello