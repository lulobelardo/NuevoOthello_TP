from src.juego import contar_fichas_volteadas

def test_contar_fichas_volteadas():
  tablero = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  assert 0 == contar_fichas_volteadas(tablero, (9, 9), 'N')

  tablero = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  assert 0 == contar_fichas_volteadas(tablero, (3, 3), 'N')

  tablero = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'N', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'N', 'N', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'N', 'B', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  assert 1 == contar_fichas_volteadas(tablero, (2, 2), 'B')

  tablero = [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
             ['B', 'N', 'N', 'N', 'N', 'N', 'N', 'B'],
             ['B', 'N', 'N', 'N', 'N', 'N', 'N', 'B'],
             ['B', 'N', 'N', 'N', 'X', 'N', 'N', 'B'],
             ['B', 'N', 'N', 'N', 'N', 'N', 'N', 'B'],
             ['B', 'N', 'N', 'N', 'N', 'N', 'N', 'B'],
             ['B', 'N', 'N', 'N', 'N', 'N', 'N', 'B'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]

  assert  19 == contar_fichas_volteadas(tablero, (3, 4), 'B')