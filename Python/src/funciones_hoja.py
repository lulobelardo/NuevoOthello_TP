'''
Este archivo contiene todas las funciones que no llaman a otras 
funciones.
'''

import os # Usa system (Limpiar consola) y name (Diff Windows - POSIX)

# limpiar_pantalla: None -> None
# Limpia la pantalla en consola
def limpiar_pantalla() -> None:
  os.system('cls' if os.name == 'nt' else 'clear')

# imprimir_tablero: Tablero -> None
# Imprime el tablero
def imprimir_tablero(tablero: list[list[str]]) -> None:
  print()
  print('    A B C D E F G H')
  print('    ---------------')
  for i, fila in enumerate(tablero):
    print(i + 1, end = ' | ')
    for valor in fila:
      print(valor, end = ' ')
    print('|', i + 1)
  print('    ---------------')
  print('    A B C D E F G H')
  print()

# copiar_tablero: Tablero -> Tablero
# Retorna una copia del tablero
'''
Toma un tablero.
Crea una matriz nueva, y luego copia -sin referenciar- (duplica en memoria) 
cada fila del tablero original en copia_tablero, así modificar uno no modifica 
el otro. Luego lo retorna.
'''
def copiar_tablero(tablero: list[list[str]]) -> list[list[str]]:
  copia_tablero = [[], [], [], [], [], [], [], []]
  for indice, fila in enumerate(tablero):
    copia_tablero[indice] = fila[:] # [:] para perder referencia a memoria
  return copia_tablero

# fuera_del_tablero: (Int, Int) -> Bool
# Retorna si una jugada esta fuera del tablero
def fuera_del_tablero(jugada: tuple) -> bool:
  return (jugada[0] not in range(8) or jugada[1] not in range(8))

# color_invalido: String -> Bool
# Recibe una string de una caracter y retorna FALSO si se es 'B' o 'N'
def color_invalido(color: str) -> bool:
  if color in ('B', 'N'):
    return False
  return True

# dificultad_invalida: String -> Bool
# Recibe una string de una caracter y retorna FALSO si es '0' o '1'
def dificultad_invalida(dificultad: str) -> bool:
  if dificultad in ('1', '0'):
    return False
  return True

# cambiar_turno: String -> String
# Cambia el turno, si era del B ahora es del N, y viceversa
def cambiar_turno(turno: str) -> str:
  return ("B" if turno == "N" else "N")

# traducir_posicion: (Int, Int) -> String
# Toma una posicion como tupla y la retorna como string en lenguaje ordinario
def traducir_posicion(posicion: tuple) -> str:
  resultado = ""
  letras = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
  resultado += letras[posicion[1]]
  resultado += str(posicion[0] + 1)
  return resultado

# convertir_fila: String -> Int
# Toma un número como string y retorna el número como Int - 1
'''
Toma como parámetro una string de dos caracteres en donde el segundo representa 
la fila. Este debería ser un dígito.
Si es un entero, retorna el anterior a dicho valor, pues traduce el conteo
'Humano' (comienza por 1) al informático (comienza por 0). Por otra parte, si
es una letra o cualquier otro caracter, retorna -1 como aviso de que es erróneo
el dato (si toma '0' también es erróneo, por lo que no genera problema).
Si toma '9', el movimiento igualmente será fuera de rango, por lo que no afecta.
'''
def convertir_fila(jugada: str) -> int:
  try:
    return int(jugada[1]) - 1
  except:
    return -1 # El programa sólo verifica que el dato es erróneo luego

# convertir_columna: String -> Int
# Toma una letra como string y retorna el número de columna correspondiente
'''
Toma como parámetro una string de dos caracteres en donde el primero representa 
la columna. Este debería ser una letra en el rango A-H.
Retorna el valor asociado de cada letra al número de columna.
Si el dato es erróneo, retorna -1 como aviso del fallo.
'''
def convertir_columna(jugada: str) -> int:
  # Diccionario de columnas con su representación numérica
  letras = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
  try:
    return letras[jugada[0]]
  except:
    return -1
