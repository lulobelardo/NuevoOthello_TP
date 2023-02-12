#include "tests.h"

void main() {
  test_crear_tablero();

  test_guardar_tablero();

  test_obtener_jugadores();

  test_cambiar_turno();

  test_convertir_columna();

  test_convertir_fila();

  test_fuera_del_tablero();

  test_posicion_ya_ocupada();

  test_obtener_ficha();

  test_colocar_ficha();

  test_realizar_jugada();

  test_chequear_paso();

  test_fin_del_juego();

  test_jugadores_validos();

  test_turno_valido();

  test_jugar();

  printf("TODOS LOS TESTS HAN SIDO PASADOS CORRECTAMENTE.\n");
}

void test_crear_tablero() {
  Tablero tablero = crear_tablero();

  for (int i = 0; i < DIMENSION_TABLERO; i++) {
    for (int c = 0; c < DIMENSION_TABLERO; c++) {
      if((i == 3 && c == 3) || (i == 4 && c == 4))
        assert(tablero[i][c] == FICHA_BLANCA);
      else if((i == 3 && c == 4) || (i == 4 && c == 3))
        assert(tablero[i][c] == FICHA_NEGRA);
      else
        assert(tablero[i][c] == POSICION_VACIA);
    }
  }

  liberar_tablero(tablero);
}

void test_guardar_tablero() {
  char path[511];
  if (getcwd(path, sizeof(path)) != NULL) {
    if(path[strlen(path) - 1] != 'C')
      strcat(path,"/C");
    strcat(path,"/RecursosTest/test_resultado_1.txt");


    Tablero tablero = crear_tablero();
    assert(guardar_tablero(path, tablero, 'B') == 0);

    FILE * fp = fopen(path, "r");
    for (int i = 0; i < DIMENSION_TABLERO; i++) {
      for (int c = 0; c < DIMENSION_TABLERO; c++) {
        assert(tablero[i][c] == fgetc(fp));
      }
      fgetc(fp);
    }

    assert(fgetc(fp) == 'B');

    fclose(fp);
    liberar_tablero(tablero);
  }
}

void test_obtener_jugadores() {
  char path[511];
  if (getcwd(path, sizeof(path)) != NULL) {
    if(path[strlen(path) - 1] != 'C')
      strcat(path,"/C");
    strcat(path,"/RecursosTest/test_partida_1.txt");
  
    FILE * fp = fopen(path, "r");

    Personas jugador = obtener_jugadores(fp);
    assert(strcmp("Luciano Belardo", jugador[0].nombre) == 0);
    assert('N' == jugador[0].color);
    assert(strcmp("Ignacio Basualdo", jugador[1].nombre) == 0);
    assert('B' == jugador[1].color);

    liberar_jugadores(jugador);
    fclose(fp);

    getcwd(path, sizeof(path));
    if(path[strlen(path) - 1] != 'C')
      strcat(path,"/C");
    strcat(path,"/RecursosTest/test_partida_2.txt");

    fp = fopen(path, "r");

    jugador = obtener_jugadores(fp);
    assert('X' == jugador[1].color);

    liberar_jugadores(jugador);
    fclose(fp);
  }
}

void test_cambiar_turno() {
  assert(FICHA_BLANCA == cambiar_turno(FICHA_NEGRA));
  assert(FICHA_NEGRA == cambiar_turno(FICHA_BLANCA));
}

void test_convertir_columna() {
  assert(convertir_columna('A') == 0);
  assert(convertir_columna('B') == 1);
  assert(convertir_columna('C') == 2);
  assert(convertir_columna('D') == 3);
  assert(convertir_columna('E') == 4);
  assert(convertir_columna('F') == 5);
  assert(convertir_columna('G') == 6);
  assert(convertir_columna('H') == 7);
  assert(convertir_columna('j') == -1);
}

void test_convertir_fila() {
  assert(convertir_fila('1') == 0);
  assert(convertir_fila('2') == 1);
  assert(convertir_fila('3') == 2);
  assert(convertir_fila('4') == 3);
  assert(convertir_fila('5') == 4);
  assert(convertir_fila('6') == 5);
  assert(convertir_fila('7') == 6);
  assert(convertir_fila('8') == 7);
}

void test_fuera_del_tablero() {
  Posicion jugada;
  jugada.fila = 1;
  jugada.columna = 1;
  assert(fuera_del_tablero(jugada) == 0);

  jugada.fila = 5;
  jugada.columna = 7;
  assert(fuera_del_tablero(jugada) == 0);

  jugada.fila = -1;
  jugada.columna = 1;
  assert(fuera_del_tablero(jugada) != 0);

  jugada.fila = 1;
  jugada.columna = 10;
  assert(fuera_del_tablero(jugada) != 0);
}

void test_posicion_ya_ocupada() {
  Tablero tablero = crear_tablero();

  Posicion jugada;
  jugada.fila = 1;
  jugada.columna = 7;
  assert(posicion_ya_ocupada(tablero, jugada) == 0);

  jugada.fila = 3;
  jugada.columna = 3;
  assert(posicion_ya_ocupada(tablero, jugada) != 0);

  jugada.fila = 3;
  jugada.columna = 4;
  assert(posicion_ya_ocupada(tablero, jugada) != 0);

  liberar_tablero(tablero);
}

void test_obtener_ficha() {
  Tablero tablero = crear_tablero();

  Posicion jugada;
  jugada.fila = 1;
  jugada.columna = 7;
  assert(obtener_ficha(tablero, jugada) == 'X');

  jugada.fila = 3;
  jugada.columna = 3;
  assert(obtener_ficha(tablero, jugada) == 'B');

  jugada.fila = 3;
  jugada.columna = 4;
  assert(obtener_ficha(tablero, jugada) == 'N');

  liberar_tablero(tablero);
}

void test_colocar_ficha() {
  Tablero tablero = crear_tablero();

  Posicion jugada;
  jugada.fila = 3;
  jugada.columna = 2;
  assert(obtener_ficha(tablero, jugada) == 'X');
  colocar_ficha(tablero, jugada, 'N');
  assert(obtener_ficha(tablero, jugada) == 'N');

  liberar_tablero(tablero);
}

void test_realizar_jugada() {
  Tablero tablero = crear_tablero();

  Posicion jugada;
  jugada.fila = 3;
  jugada.columna = 2;

  assert(realizar_jugada(tablero, jugada, 'N'));

  assert(tablero[3][2] == 'N');
  assert(tablero[3][3] == 'N');

  liberar_tablero(tablero);
}

void test_chequear_paso() {
  Tablero tablero = crear_tablero();

  assert(chequear_paso(tablero, 'N') == 0);
  assert(chequear_paso(tablero, 'B') == 0);

  liberar_tablero(tablero);
}

void test_fin_del_juego() {
  Tablero tablero = crear_tablero();

  assert(fin_del_juego(tablero) == 0);

  liberar_tablero(tablero);
}

void test_jugadores_validos() {
  char path[511];
  if (getcwd(path, sizeof(path)) != NULL) {
    if(path[strlen(path) - 1] != 'C')
      strcat(path,"/C");
    strcat(path,"/RecursosTest/test_partida_1.txt");

    FILE * fp = fopen(path, "r");

    Personas jugador = obtener_jugadores(fp);

    assert(jugadores_validos(jugador) != 0);

    liberar_jugadores(jugador);
    fclose(fp);

    getcwd(path, sizeof(path));
    if(path[strlen(path) - 1] != 'C')
      strcat(path,"/C");
    strcat(path,"/RecursosTest/test_partida_2.txt");

    fp = fopen(path, "r");

    jugador = obtener_jugadores(fp);
    assert(jugadores_validos(jugador) == 0);

    liberar_jugadores(jugador);
    fclose(fp);
  }
}

void test_turno_valido() {
  assert(turno_valido('X') == 0);
  assert(turno_valido('B') != 0);
  assert(turno_valido('N') != 0);
}

void test_jugar() {
  char path[511];
  if (getcwd(path, sizeof(path)) != NULL) {
    if(path[strlen(path) - 1] != 'C')
      strcat(path,"/C");
    strcat(path,"/RecursosTest/test_partida_1.txt");
  
    FILE * fp = fopen(path, "r");
    Personas jugador = obtener_jugadores(fp);
    char turno = obtener_turno(fp);

    Tablero tablero = crear_tablero();
    Codigos codigos = iniciar_codigos();

    assert(jugar(fp, tablero, codigos, turno) == 'B');

    liberar_codigos(codigos);
    liberar_tablero(tablero);
    liberar_jugadores(jugador);
    fclose(fp);
  }
}