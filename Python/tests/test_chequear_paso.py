from src.juego import chequear_paso

def test_chequear_paso():
  tablero = [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B'],
             ['X', 'X', 'B', 'B', 'B', 'N', 'N', 'N'],
             ['X', 'B', 'B', 'N', 'B', 'N', 'N', 'N'],
             ['B', 'B', 'B', 'N', 'B', 'N', 'N', 'N'],
             ['B', 'B', 'N', 'B', 'N', 'B', 'N', 'N'],
             ['B', 'N', 'B', 'N', 'N', 'N', 'N', 'N'],
             ['N', 'N', 'N', 'B', 'N', 'N', 'B', 'N'],
             ['B', 'B', 'B', 'B', 'N', 'N', 'B', 'N']]

  tablero_ = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'B', 'N', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'N', 'N', 'N', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
              ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

  assert True == chequear_paso(tablero, 'B')
  assert False == chequear_paso(tablero, 'N')
  assert False == chequear_paso(tablero_, 'B')
  assert False == chequear_paso(tablero_, 'N')