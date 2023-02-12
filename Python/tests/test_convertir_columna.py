from src.juego import convertir_columna

def test_convertir_columna():
  caracter = 'ABCDEFGH'
  assert 0 == convertir_columna("A1")
  assert 1 == convertir_columna("B1")
  assert 2 == convertir_columna("C2")
  assert 3 == convertir_columna("D1")
  assert 4 == convertir_columna("E1")
  assert 5 == convertir_columna("F1")
  assert 6 == convertir_columna("G6")
  assert 7 == convertir_columna("H5")

  assert -1 == convertir_columna("g1")
  assert -1 == convertir_columna("h1")
  assert -1 == convertir_columna("W1")
  assert -1 == convertir_columna("L1")