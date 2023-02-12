from src.juego import copiar_tablero

def test_copiar_tablero():
  tablero_1 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'B', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'B', 'B', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
  tablero_2 = tablero_1
  assert (tablero_2 is tablero_1) == True

  tablero_2 = copiar_tablero(tablero_1)
  assert tablero_2 == tablero_1
  assert (tablero_2 is tablero_1) == False

  tablero_1 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
  assert tablero_2 != tablero_1

  tablero_2 = [['B', 'B', 'B', 'B', 'B', 'B', 'N', 'B'],
               ['B', 'B', 'B', 'B', 'B', 'B', 'N', 'B'],
               ['B', 'B', 'B', 'B', 'B', 'N', 'N', 'B'],
               ['B', 'B', 'N', 'B', 'N', 'B', 'N', 'B'],
               ['B', 'B', 'B', 'N', 'N', 'B', 'B', 'B'],
               ['B', 'B', 'N', 'B', 'B', 'N', 'B', 'B'],
               ['B', 'N', 'B', 'B', 'B', 'N', 'N', 'B'],
               ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']]
  tablero_3 = tablero_2
  assert (tablero_3 is tablero_2) == True

  tablero_3 = copiar_tablero(tablero_2)
  assert tablero_3 == tablero_2
  assert (tablero_3 is tablero_2) == False

  tablero_3 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
               ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
  assert tablero_3 != tablero_2