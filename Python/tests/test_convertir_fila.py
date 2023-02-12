from src.juego import convertir_fila

def test_convertir_fila():
  caracteres = '0123456789'
  
  assert -1 == convertir_fila("A0")
  assert 0 == convertir_fila("A1")
  assert 1 == convertir_fila("A2")
  assert 2 == convertir_fila("A3")
  assert 3 == convertir_fila("A4")
  assert 4 == convertir_fila("A5")
  assert 5 == convertir_fila("A6")
  assert 6 == convertir_fila("A7")
  assert 7 == convertir_fila("A8")
  assert 8 == convertir_fila("A9")
  
  assert -1 == convertir_fila("B ")
  assert -1 == convertir_fila("BG")
  assert -1 == convertir_fila("BC")
  assert -1 == convertir_fila("B.")
  assert -1 == convertir_fila("BA")
  assert -1 == convertir_fila("BL")
  assert -1 == convertir_fila("CG")
  assert -1 == convertir_fila("")