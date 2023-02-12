// #include <stdio.h>
#include <stdlib.h>
#include "funciones.h"

// argv[1] va a contener el nombre o path del archivo de JUGADAS a LEER
// argv[2] va a contener el nombre o path del archivo RESULTADO a ESCRIBIR
int main(int argc, char const *argv[]) {
  FILE *archivo_juego = fopen(argv[1], "r");
  if(archivo_juego == NULL) {
    printf("\nError al abrir el archivo 1\n\n");
    return 1;
  }

  Personas jugadores = obtener_jugadores(archivo_juego);
  if(!jugadores_validos(jugadores)) {
    printf("\nAlguno de los jugadores esta mal ingresado.\n\n");
    liberar_jugadores(jugadores);
    fclose(archivo_juego);
    return 2;
  }
  
  char turno = obtener_turno(archivo_juego);
  if(!turno_valido(turno)) {
    printf("\nNo esta correctamente indicado que jugador comienza.\n\n");
    liberar_jugadores(jugadores);
    fclose(archivo_juego);
    return 2;
  }

  Tablero tablero = crear_tablero();
  Codigos codigos = iniciar_codigos();

  turno = jugar(archivo_juego, tablero, codigos, turno);

  if(!juego_terminado(tablero, jugadores, codigos))
    if(guardar_tablero(argv[2], tablero, turno) == 1)
      printf("\nError al abrir/crear el archivo 2.\n\n");

  fclose(archivo_juego);
  liberar_codigos(codigos);
  liberar_jugadores(jugadores);
  liberar_tablero(tablero);
  return 0;
}