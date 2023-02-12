from src.juego import fuera_del_tablero

def test_fuera_del_tablero():
  jugada = (0, 5)
  assert fuera_del_tablero(jugada) == False

  jugada = (-1, 5)
  assert fuera_del_tablero(jugada) == True
  jugada = (0, -1)
  assert fuera_del_tablero(jugada) == True
  jugada = (8, 5)
  assert fuera_del_tablero(jugada) == True
  jugada = (0, 8)
  assert fuera_del_tablero(jugada) == True
  jugada = (8, -1)
  assert fuera_del_tablero(jugada) == True