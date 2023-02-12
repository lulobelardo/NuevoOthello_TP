from src.juego import cambiar_turno

def test_cambiar_turno():
  assert 'N' == cambiar_turno('B')
  assert 'B' == cambiar_turno('N')