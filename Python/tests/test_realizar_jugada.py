from src.juego import realizar_jugada

def test_realizar_jugada():
  tablero0 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  tablero1 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
  assert False == realizar_jugada(tablero0, (9, 9), 'N')
  assert tablero0 == tablero1
  assert False == realizar_jugada(tablero0, (3, 3), 'N')
  assert tablero0 == tablero1

  tablero1 = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  assert True == realizar_jugada(tablero0, (2, 3), 'N')
  assert tablero0 == tablero1

  tablero0 = [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
              ['B', 'N', 'N', 'N', 'N', 'N', 'N', 'B'],
              ['B', 'N', 'N', 'N', 'N', 'N', 'N', 'B'],
              ['B', 'N', 'N', 'N', 'X', 'N', 'N', 'B'],
              ['B', 'N', 'N', 'N', 'N', 'N', 'N', 'B'],
              ['B', 'N', 'N', 'N', 'N', 'N', 'N', 'B'],
              ['B', 'N', 'N', 'N', 'N', 'N', 'N', 'B'],
              ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]

  tablero1 = [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
              ['B', 'N', 'B', 'N', 'B', 'N', 'B', 'B'],
              ['B', 'N', 'N', 'B', 'B', 'B', 'N', 'B'],
              ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
              ['B', 'N', 'N', 'B', 'B', 'B', 'N', 'B'],
              ['B', 'N', 'B', 'N', 'B', 'N', 'B', 'B'],
              ['B', 'B', 'N', 'N', 'B', 'N', 'N', 'B'],
              ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
  assert True == realizar_jugada(tablero0, (3, 4), 'B')
  assert tablero0 == tablero1