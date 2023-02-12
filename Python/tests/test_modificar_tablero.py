from src.juego import modificar_tablero

def test_modificar_tablero():
  # Abajo
  tablero_0 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  tablero_1 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  modificar_tablero(tablero_0, (2, 3), 'N', (1, 0))
  assert tablero_1 == tablero_0

  # Derecha
  tablero_0 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  tablero_1 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'B', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  modificar_tablero(tablero_0, (4, 2), 'B', (0, 1))
  assert tablero_1 == tablero_0

  # Arriba
  tablero_0 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
               ['X', 'X', 'B', 'B', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  tablero_1 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
               ['X', 'X', 'B', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
  modificar_tablero(tablero_0, (5, 3), 'N', (-1, 0))
  assert tablero_1 == tablero_0

  # Izquierda
  tablero_0 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'B', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  tablero_1 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'B', 'N', 'N', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  modificar_tablero(tablero_0, (4, 5), 'N', (0, -1))
  assert tablero_1 == tablero_0

  # Diagonal arriba derecha
  tablero_0 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'B', 'N', 'N', 'N', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  tablero_1 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'B', 'B', 'N', 'N', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  modificar_tablero(tablero_0, (5, 2), 'B', (-1, 1))
  assert tablero_1 == tablero_0

  # Diagonal abajo izquierda
  tablero_0 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'B', 'B', 'N', 'N', 'X', 'X'],
               ['X', 'X', 'B', 'N', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  tablero_1 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'B', 'B', 'N', 'N', 'X', 'X'],
               ['X', 'X', 'B', 'N', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  modificar_tablero(tablero_0, (1, 5), 'N', (1, -1))
  assert tablero_1 == tablero_0

  # Diagonal arriba izquierda
  tablero_0 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'B', 'B', 'B', 'N', 'X', 'X'],
               ['X', 'X', 'B', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  tablero_1 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'B', 'B', 'B', 'N', 'X', 'X'],
               ['X', 'X', 'B', 'B', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  modificar_tablero(tablero_0, (6, 4), 'B', (-1, -1))
  assert tablero_1 == tablero_0

  # Diagonal abajo derecha
  tablero_0 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'N', 'N', 'N', 'N', 'N', 'X', 'X'],
               ['X', 'X', 'B', 'B', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  tablero_1 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
               ['X', 'N', 'N', 'N', 'N', 'N', 'X', 'X'],
               ['X', 'X', 'B', 'B', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  modificar_tablero(tablero_0, (1, 2), 'B', (1, 1))
  assert tablero_1 == tablero_0