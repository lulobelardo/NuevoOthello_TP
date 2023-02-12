from src.juego import dificultad_invalida

def test_dificultad_invalida():
  assert dificultad_invalida('0') == False
  assert dificultad_invalida('1') == False

  assert dificultad_invalida('X') == True
  assert dificultad_invalida('2') == True
  assert dificultad_invalida('-1') == True