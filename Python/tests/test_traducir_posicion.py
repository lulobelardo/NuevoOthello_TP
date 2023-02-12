from src.juego import traducir_posicion

def test_traducir_posicion():
  # Creo y chequeo los 64 casos posibles
  for i in range(8):
    for j in range(8):
      assert traducir_posicion((i, j)) == chr(65 + j) + str(i + 1)
