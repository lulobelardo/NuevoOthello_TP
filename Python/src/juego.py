from sys import argv # Obtener datos pasados por consola en argv[]
from random import choice # Jugada aleatoria PC nivel 0
from io import TextIOWrapper # File type
import os # Usa system (Limpiar consola) y name (Diff Windows - POSIX)

# Tablero := list[list[str]]

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

# obtener_tablero: File -> Tablero
# Recibe el archivo del tablero y lo retorna en forma de list[list[str]]
'''
En caso de que el tablero no se encuentre completo, o contenga caracteres 
erroneos, entonces la funcion devuelve la lista vacia. Esta funcion funciona 
siempre y cuando el puntero del archivo apunte al comienzo del tablero y este 
correctamente el formato.
Si el tablero posee algun estado imposible, el juego funcionara normalmente en 
todos los casos que el centro inicial tenga fichas.
'''
def obtener_tablero(archivo_tablero: TextIOWrapper) -> list[list[str]]:
  tablero = [['*'] * 8 for _ in range(8)] # Crea un tablero lleno de '*'
  
  for fila in range(8):
    line = archivo_tablero.readline().strip()
    if(len(line) == 8): # Sino, error de formato
      for columna, ficha in enumerate(line):
        if ficha in ('X', 'B', 'N'): # Sino, error de formato
          tablero[fila][columna] = ficha

  # Si el cuadrado central no contiene fichas, entonces tambien es invalido
  if not any(tablero[i][j] in ('B', 'N') for i, j in [(3, 3), (3, 4), (4, 3), (4, 4)]):
    return []

  # Chequea que sea valido el tablero
  validado = True
  i = 0
  while(validado and i < 8):
    if '*' in tablero[i]:
      validado = False
    i += 1

  if validado:
    return tablero
  else:
    return []

# obtener_turno: File -> String
# Recibe el archivo del turno y lo retorna en forma de string
'''
El archivo debe estar apuntando al comienzo de la linea donde la letra B o N 
deben estar escritas correctamente como el primer caracter de la linea. Ignora 
si el archivo posee otro texto. Luego, retorna dicha letra o 'X' si el color 
era inválido.
'''
def obtener_turno(archivo_tablero: TextIOWrapper) -> str:
  turno = archivo_tablero.read(1)
  if(color_invalido(turno)):
    return "X"
  return turno

# inicio_juego: None -> list:
# Retorna una lista con los valores iniciales completados
'''
La funcion se encarga de leer los datos de la consola y del archivo pasado por 
consola para luego almacenarlos en distintas variables y retornarlas en forma 
de lista.
La lista sera vacia si hay algun error o algun dato es inválido, y en caso 
contrario la lista tendra cuatro elementos:
[0] -> El tablero (list[list[str]]) con los datos del archivo ingresado por consola argv[1]
[1] -> El turno (str) con el dato del archivo ingresado por consola argv[1]
[2] -> El color_jugador (str) con el dato ingresado por consola argv[2]
[3] -> La dificultad (str) con el dato ingresado por consola argv[3]
'''
def inicio_juego() -> list:
  tablero = []
  turno = 'X'
  color_jugador = 'X'
  dificultad = '-1'

  try:
    archivo_tablero = open(argv[1], 'r')
  except:
    print("ERROR: El archivo no fue ingresado, no se pudo abrir o no existe.")
    return []
  else: # Meramente estético el else
    tablero = obtener_tablero(archivo_tablero)
    if(tablero == []):
      print("ERROR: El tablero está incompleto o es inválido.")
      archivo_tablero.close()
      return []
    
    turno = obtener_turno(archivo_tablero)
    if(turno == 'X'):
      print("ERROR: El turno no está escrito o es inválido.")
      archivo_tablero.close()
      return []

    archivo_tablero.close()
  try:
    if(color_invalido(argv[2])):
      print("ERROR: El color del jugador es invalido.")
      return []
    else:
      color_jugador = argv[2]
  except:
    print("ERROR: El color del jugador no se ingreso.")
    return []

  try:
    if(dificultad_invalida(argv[3])):
      print("ERROR: La dificultad es invalida")
      return []
    else:
      dificultad = argv[3] # nivel (0 o 1)
  except:
    print("ERROR: La dificultad no se ingreso.")
    return []

  return [tablero, turno, color_jugador, dificultad]

# obtener_fichas_a_voltear: Tablero, (Int, Int), String, (Int, Int) -> Int
# Retorna según la dirección indicada la cantidad del fichas a voltear
'''
Toma como parámetros el tablero, la posición jugada (VÁLIDA), de quién es el
turno y la dirección que quiere calcular (8 posibles).
La función cuenta la cantidad de fichas a voltear en una direccion indicada, 
para el tablero, jugada y turno resprectivos.
Retorna dicho valor.
'''
def obtener_fichas_a_voltear(tablero: list[list[str]], jugada: tuple, turno: str, direccion: tuple) -> int:
  # Asignaciones
  j_fila = jugada[0] # jugada_fila
  j_colum = jugada[1] # jugada_columna
  vert = direccion[0] # Vertical: variación en las filas
  horiz = direccion[1] # Horizontal: variación en las columnas

  fichas_a_voltear = 0 # Representa la cantidad final de fichas a voltear
  delta = 1 # Contador momentáneo/hipotético de fichas a cambiar (desplazador)

  continuar = True
  while continuar:
    fila_actual = j_fila + delta * vert
    col_actual = j_colum + delta * horiz

    # Caso en el que la jugada se salga del tablero
    if (fuera_del_tablero((fila_actual, col_actual))):
      continuar = False
    elif delta == 1: # Solo si es adyacente a la jugada
      # Caso que haya una ficha del mismo color o no hay ninguna ficha
      if tablero[fila_actual][col_actual] in ('X', turno):
        continuar = False
    # Caso que no haya ninguna ficha
    elif tablero[fila_actual][col_actual] == 'X':
      continuar = False
    # Caso que haya una ficha del mismo color LUEGO de una o mas del otro color
    elif tablero[fila_actual][col_actual] == turno:
      fichas_a_voltear = delta - 1 # Se van a modificar del tablero delta - 1 fichas
      continuar = False
    # Desplaza delta para analizar la siguiente posición
    delta += 1
  
  return fichas_a_voltear

# modificar_tablero: Tablero, (Int, Int), String, (Int, Int) -> Bool
# Modifica según la dirección indicada los valores del tablero correspondientes
'''
Toma como parámetros el tablero, la posición jugada (VÁLIDA), de quién es el
turno y la dirección que quiere modificar (8 posibles).
La función hace el movimiento COMPLETO en una dirección indicada, es decir,
voltea todas las fichas correspondientes en una dirección siempre y cuando haya
fichas que voltear. NO MODIFICA la posicion jugada.
El parámetro 'dirección' es una tupla de dos números que pueden ser -1, 0 y 1.
Los mismos reflejan la dirección fila/columna en la que se está desplazando
respectivamente. La dirección (0, 0) no existe.
Retorna si el tablero se modifico en la direccion indicada.
'''
def modificar_tablero(tablero: list[list[str]], jugada: tuple, turno: str, direccion: tuple) -> bool:
  # Asignaciones
  j_fila = jugada[0] # jugada_fila
  j_colum = jugada[1] # jugada_columna
  vert = direccion[0] # Vertical: variación en las filas
  horiz = direccion[1] # Horizontal: variación en las columnas

  fichas_a_voltear = obtener_fichas_a_voltear(tablero, jugada, turno, direccion)

  # Cambia el color de las fichas encerradas (fichas_a_voltear fichas)
  for lugar in range(1, fichas_a_voltear + 1):
    tablero[j_fila + lugar * vert][j_colum + lugar * horiz] = turno

  if(fichas_a_voltear > 0):
    return True
  else:
    return False

# realizar_jugada: Tablero, (Int, Int), String -> Bool
# Si la jugada es válida, retorna True y la realiza, sino, retorna False
'''
Toma como parámetros el tablero, la jugada y el turno.
Si la jugada es inválida, retorna False y no modifica el tablero,
si en un principio la jugada es válida, entonces modifica el tablero según
corresponda en todas las direcciones, y si al hacerlo el tablero se modificó,
entonces la jugada era efectivamente válida (ya se realizo) y retorna True. Por
otro lado, si el tablero NO se modificó, entonces la jugada era inválida, por
lo que retorna False.
'''
def realizar_jugada(tablero: list[list[str]], jugada: tuple, turno: str) -> bool:
  # Caso jugada fuera de rango
  if fuera_del_tablero(jugada):
    return False
  # Caso posición ocupada por otra ficha
  if tablero[jugada[0]][jugada[1]] in ('B', 'N'):
    return False

  # Modifica (o no) el tablero en todas las direcciones
  se_modifico = False
  for i in range(-1,2):
    for c in range(-1,2):
      if (i != 0 or c != 0):
        se_modifico = (modificar_tablero(tablero, jugada, turno, (i, c)) or se_modifico)
  '''
  Notesé que si se modificó, ya no hace falta que se vuelva a modificar pues 
  trabaja sobre el tablero original, por lo que solo queda poner la ficha.
  '''
  if not se_modifico: # Si no se modificó, la jugada es inválida
    return False

  tablero[jugada[0]][jugada[1]] = turno # Coloco la ficha
  return True

# contar_fichas_volteadas: Tablero, (Int, Int), String -> Bool
# Retorna la cantidad de fichas que se voltearian si se hiciera dicha jugada
def contar_fichas_volteadas(tablero: list[list[str]], jugada: tuple, turno: str) -> int:
  fichas_volteadas = 0
  for i in range(-1,2):
    for c in range(-1,2):
      if (i != 0 or c != 0):
        fichas_volteadas += obtener_fichas_a_voltear(tablero, jugada, turno, (i, c))
  return fichas_volteadas

# jugada_pc: Tablero, String, String -> None
# Toma el tablero, el color de la PC y el nivel de la PC y hace su jugada
'''
La funcion calcula todas las jugadas en base al tablero y turno indicados, para 
luego, en base al nivel de la PC, realizar una jugada aleatoria o realizar la 
jugada que voltee mayor cantidad de fichas (frente a la igualdad es aleatorio).
Imprime en pantalla la jugada realizada.
'''
def jugada_pc(tablero: list[list[str]], turno: str, dificultad: str) -> None:
  # Calcula las posibles jugadas y las fichas que voltea
  jugadas_posibles = {}
  fichas_volteadas = 0
  for fila, lista in enumerate(tablero):
    for columna, ficha in enumerate(lista):
      if(tablero[fila][columna] == 'X'):
        fichas_volteadas = contar_fichas_volteadas(tablero, (fila, columna), turno)
      if(fichas_volteadas > 0):
        jugadas_posibles[(fila, columna)] = fichas_volteadas
      fichas_volteadas = 0
  
  limpiar_pantalla()
  print("La jugada de la PC (" + turno + ") fue: ", end = '')

  # Realiza la jugada correspondiente
  posicion_final = (-1, -1)
  if jugadas_posibles == {}: # Debe pasar
    print("PASAR")
    return None
  elif dificultad == '0':
    posicion_final = choice(list(jugadas_posibles.keys()))
    realizar_jugada(tablero, posicion_final, turno)
  else:
    posiciones_finales = []
    valor_max = 0
    for posicion, valor in jugadas_posibles.items():
      if valor > valor_max:
        posiciones_finales = [posicion]
        valor_max = valor
      elif valor == valor_max:
        posiciones_finales += [posicion]

    posicion_final = choice(posiciones_finales)
    realizar_jugada(tablero, posicion_final, turno)
    
  print(traducir_posicion(posicion_final))

  print("\nLuego de la jugada de la PC, el tablero es el siguiente:")
  imprimir_tablero(tablero)

# jugada_jugador: Tablero, String -> None
# Toma el tablero y el color del jugador, y realiza la jugada tomada por pantalla
'''
La funcion muestra el tablero y pide por consola que el jugador escriba su 
jugada para luego validarla y realizarla. El mismo no finaliza hasta que el 
jugador haya incertado una jugada valida. 
Se entiende que la acción de "pasar" es mas bien obligatoria, pero permite al 
jugador observar el tablero de manera momentanea previo a que la pc juege 
nueveamente, ademas de poner en conocimiento al jugador de que esta pasando. 
'''
def jugada_jugador(tablero: list[list[str]], turno: str) -> None:
  continuar = True
  while(continuar):
    print("El tablero es el siguiente:")
    imprimir_tablero(tablero)
    jugada = input("Ingrese su jugada (" + turno + ") (Si debe pasar, escriba 'PASO'): ")
    limpiar_pantalla()

    if jugada == "PASO":
      if(chequear_paso(tablero, turno)):
        continuar = False
        print("Usted (" + turno + ") PASO!")
      else:
        print("ERROR: No se puede pasar en esta posicion!")
    elif(len(jugada) == 2): # Intenta jugar
      fila = convertir_fila(jugada) # int(jugada[1]) - 1
      columna = convertir_columna(jugada) # letras[jugada[0]]
      
      if realizar_jugada(tablero, (fila, columna), turno):
        print("Usted (" + turno + ") jugo: " + jugada)
        continuar = False
      else:
        print("ERROR: Jugada ilegal!")
    else:
      print("ERROR: Su jugada debe contener solo DOS (2) CARACTERES o ser 'PASO'!.")
    if continuar:
      print("\nIntentelo de nuevo.\n")
  
  print("\nLuego de su jugada, el tablero es el siguiente:")
  imprimir_tablero(tablero)

# chequear_paso: Tablero, String -> Bool
# Retorna True si es válido que el jugador 'pase', caso contrario retorna False
'''
Toma como parámetros el tablero y de quién es el turno.
Para ver si pasar es válido, la función chequea si efectivamente ninguno de los
64 movimientos posibles es válido, caso en el que 'pasar' es correcto y retorna
True.
Si tan solo 1 movimiento es válido, entonces 'pasar' es incorrecto, termina de
hacer chequeos y retorna False.
'''
def chequear_paso(tablero: list[list[str]], turno: str) -> bool:
  # Para no modificar el tablero original, trabaja sobre una copia
  copia_tablero = copiar_tablero(tablero)

  # Recorre o todo el tablero o hasta que encuentre un movimiento válido
  continuar = True
  fila = 0
  while fila < 8 and continuar:
    columna = 0
    while columna < 8 and continuar:
      continuar = not realizar_jugada(copia_tablero, (fila, columna), turno)
      columna += 1
    fila += 1
  return continuar

# fin_del_juego: Tablero -> Bool
# Toma un tablero y retorna si el juego ha finalizado o no
'''
Para ello chequea que ambos colores deban pasar, si esto es correcto entonces 
el juego ha terminado.
'''
def fin_del_juego(tablero: list[list[str]]) -> bool:
  return (chequear_paso(tablero, 'B') and chequear_paso(tablero, 'N'))

# evaluar_y_mostrar_resultado: Tablero, String, String -> None
# Muestra en consola el tablero final y el resultado final del juego
'''
Toma el tablero, el color del juegador y la dificultad de la PC, para luego 
imprimir en pantalla el tablero, y decir quien gana con detalle el juego.
'''
def evaluar_y_mostrar_resultado(tablero: list[list[str]], color_jugador: str, dificultad: str) -> None:
  limpiar_pantalla()
  print("El tablero FINAL es el siguiente:")
  imprimir_tablero(tablero)

  # Cuenta fichas de cada color
  jugador = 0
  pc = 0
  color_pc = cambiar_turno(color_jugador)
  for fila in tablero:
    for ficha in fila:
      if ficha == color_jugador:
        jugador += 1
      elif ficha == color_pc:
        pc += 1

  if jugador > pc:
    print("HA GANADO EL JUGADOR (" + color_jugador + ") A LA PC NIVEL " + dificultad + "!\nFELICITACIONES!")
  elif pc > jugador:
    print("Ha ganado la PC (" + color_pc + ") nivel " + dificultad + ".")
  else:
    print("Ha habido un empate. Nivel PC: " + dificultad)

  print("\nPuntos jugador (" + color_jugador + "): " + str(jugador))
  print("\nPuntos PC (" + color_pc + "): " + str(pc))
    
# jugar: Tablero, String, String, String -> None
# Toma los datos necesarios y comienza el juego versus la PC
'''
Se encarga de realizar toda la accion del juego de Reversi del jugador contra 
la PC, para luego mostrar los resultados finales. Si recibe un tablero ya 
completo, entonces mostrara los resultados del juego.
'''
def jugar(tablero: list[list[str]], turno: str, color_jugador: str, dificultad: str) -> None:
  continuar = True
  while(continuar):
    if(fin_del_juego(tablero)):
      continuar = False
    elif(turno == color_jugador):
      jugada_jugador(tablero, turno)
    else:
      jugada_pc(tablero, turno, dificultad)
    if continuar:
      input("Presione enter para continuar.")
      limpiar_pantalla()
    
    turno = cambiar_turno(turno)

  evaluar_y_mostrar_resultado(tablero, color_jugador, dificultad)

# main: None -> None
# Obtiene los datos necesarios y llama a jugar al Othello
def main() -> None:

  datos = inicio_juego()

  if(datos == []):
    return 1 # Error de set up
  
  tablero = datos[0]
  turno = datos[1]
  color_jugador = datos[2]
  dificultad = datos[3]

  print("\nEl tablero es el siguiente:")
  imprimir_tablero(tablero)
  input("Presione enter para continuar.")
  limpiar_pantalla()

  jugar(tablero, turno, color_jugador, dificultad)

main()