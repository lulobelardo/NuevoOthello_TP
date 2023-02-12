from src.juego import color_invalido

def test_color_invalido():
  assert color_invalido('B') == False
  assert color_invalido('N') == False

  assert color_invalido('X') == True
  assert color_invalido('A') == True
  assert color_invalido('b') == True