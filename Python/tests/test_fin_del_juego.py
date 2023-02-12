from src.juego import fin_del_juego

def test_fin_del_juego():
  tablero = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'N', 'N', 'N', 'N', 'N', 'X', 'X'],
             ['X', 'X', 'X', 'N', 'N', 'N', 'X', 'X'],
             ['X', 'X', 'X', 'N', 'N', 'N', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'N', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'N', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
  assert True == fin_del_juego(tablero)

  tablero = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'N', 'N', 'N', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
  assert False == fin_del_juego(tablero)

  tablero = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
  assert True == fin_del_juego(tablero)

  tablero = [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
  assert True == fin_del_juego(tablero)

  tablero = [['N', 'N', 'N', 'N', 'N', 'N', 'B', 'N'],
             ['N', 'N', 'N', 'N', 'N', 'N', 'B', 'N'],
             ['N', 'N', 'N', 'N', 'N', 'B', 'B', 'N'],
             ['N', 'N', 'B', 'N', 'B', 'N', 'B', 'N'],
             ['N', 'N', 'N', 'B', 'B', 'N', 'N', 'N'],
             ['N', 'N', 'B', 'N', 'N', 'B', 'N', 'N'],
             ['N', 'B', 'N', 'N', 'N', 'B', 'B', 'N'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
  assert True == fin_del_juego(tablero)

  tablero = [['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'X'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'X', 'X'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'X', 'N'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'X'],
             ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]
  assert True == fin_del_juego(tablero)