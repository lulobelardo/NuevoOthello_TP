from src.juego import obtener_fichas_a_voltear

def test_obtener_fichas_a_voltear():
  tablero = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'B', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'B', 'B', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
             ['X', 'X', 'N', 'X', 'X', 'N', 'B', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  # Solo algunos casos posibles

  assert obtener_fichas_a_voltear(tablero, (4, 2), 'N', (0, 1)) == 1
  assert obtener_fichas_a_voltear(tablero, (3, 2), 'N', (0, 1)) == 0
  assert obtener_fichas_a_voltear(tablero, (5, 4), 'B', (0, -1)) == 0
  assert obtener_fichas_a_voltear(tablero, (5, 4), 'B', (-1, 0)) == 1
  assert obtener_fichas_a_voltear(tablero, (2, 5), 'N', (1, -1)) == 2
  assert obtener_fichas_a_voltear(tablero, (0, 0), 'B', (0, 1)) == 0