#include "funciones.h"
// #include <stdio.h>
#include <stdlib.h>
#include <string.h>

// crear_tablero: None -> Tablero
/* crear_tablero crea un Tablero en su estado inicial, es decir pide memoria 
para almacenarlo y coloca las respectivas fichas, para luego retornarlo. */
Tablero crear_tablero() {
  Tablero tablero = malloc(sizeof(char*) * DIMENSION_TABLERO);
  for (int i = 0; i < DIMENSION_TABLERO; i++) {
    tablero[i] = malloc(sizeof(char) * DIMENSION_TABLERO);
    for (int j = 0; j < DIMENSION_TABLERO; j++) {
      tablero[i][j] = POSICION_VACIA;
    }
  }
  tablero[3][3] = tablero[4][4] = FICHA_BLANCA;
  tablero[3][4] = tablero[4][3] = FICHA_NEGRA;

  return tablero;
}

// liberar_tablero: Tablero -> None
/* liberar_tablero toma un Tablero y libera la memoria utilizada por el mismo, 
a medida que borra sus datos. */
void liberar_tablero(Tablero tablero) {
  for (int i = 0; i < DIMENSION_TABLERO; i++) {
    free(tablero[i]);
    tablero[i] = NULL;
  }
  free(tablero);
  tablero = NULL;
}

// guardar_tablero: (char const *) Tablero char -> None
/* guardar_tablero toma el path de un archivo, un Tablero y un Turno, para 
luego guardar el tablero y el turno en el archivo especificado. Retorna 1 si 
hubo algun error al abrir/crear el archivo y 0 si no lo hubo. */
int guardar_tablero(char const *archivo_nombre, Tablero tablero, char turno) {
  FILE *archivo = fopen(archivo_nombre, "w+");
  if(archivo == NULL) {
    perror("Error opening file");
    return 1;
  }
  
  for (int i = 0; i < DIMENSION_TABLERO; i++) {
    for (int j = 0; j < DIMENSION_TABLERO; j++) {
      fputc(tablero[i][j], archivo);
    }
    fputc('\n', archivo);
  }
  fputc(turno, archivo);

  fclose(archivo);
  return 0;
}

// obtener_jugadores: (FILE *) -> Personas
/* obtener_jugadores toma un Archivo (valga la redundancia, ya abierto) y 
almacena en una "lista" los nombres y el turno de los jugadores. Para esto, 
crea la memoria necesaria para guardar dos Jugador (nombre + turno) y luego los 
retorna en forma de Personas, pidiendo tambien la memoria para el nombre. */
Personas obtener_jugadores(FILE *archivo_juego) {
  char temp[255];
  Personas jugador = malloc(sizeof(Jugador) * CANTIDAD_JUGADORES);

  for(int i = 0; i < CANTIDAD_JUGADORES; i++) {
    fscanf(archivo_juego, "%[^,]", temp);
    jugador[i].nombre = malloc(sizeof(char) * strlen(temp) + 1);
    strcpy(jugador[i].nombre, temp);

    fgetc(archivo_juego); // Desecha la ','

    jugador[i].color = fgetc(archivo_juego);
    if(fgetc(archivo_juego) != '\n') // Error de formato
      jugador[i].color = 'X';
    
    /* Si jugador[i].color contiene un dato incorrecto (cualquier char != 'B'
    o 'N'), el programa expone el error luego. */
  }

  return jugador;
}

// liberar_jugadores: Personas -> None
/* liberar_jugadores toma una "lista" de Jugador y libera la memoria (+ borra 
los datos) de cada uno asi como tambien de la lista en sí. */
void liberar_jugadores(Personas jugador) {
  for(int i = 0; i < CANTIDAD_JUGADORES; i++) {
    free(jugador[i].nombre);
    jugador[i].nombre = NULL;
  }
  free(jugador);
  jugador = NULL;
}

// cambiar_turno: char -> char
/* cambiar_turno toma un turno ('B' o 'N') y retorna el otro ('N' o 'B'). */
char cambiar_turno(char turno) {
  if(turno == FICHA_BLANCA)
    return FICHA_NEGRA;
  else
    return FICHA_BLANCA;
}

// obtener_turno: (FILE *) -> char
/* obtener_turno toma un archivo (apuntando a la linea correspondiente) y 
retorna que color comienza el juego. */
char obtener_turno(FILE *archivo_juego) {
  char turno = fgetc(archivo_juego);
  
  if(fgetc(archivo_juego) != '\n') // Desecha '\n', si no hay: ERROR de formato
    return 'X';
  
  /* Si retorna un dato incorrecto (cualquier char != 'B' o 'N'), el programa 
  expone el error luego. */

  return turno;
}

// convertir_columna: char -> int
/* convertir_columna toma una letra que corresponde a una columna y retorna su 
respectivo valor numérico. */
int convertir_columna(char letra) {
  int columna;
  switch (letra)
  {
    case 'A': columna = 0; break;
    case 'B': columna = 1; break;
    case 'C': columna = 2; break;
    case 'D': columna = 3; break;
    case 'E': columna = 4; break;
    case 'F': columna = 5; break;
    case 'G': columna = 6; break;
    case 'H': columna = 7; break;
    
    default: columna = -1; break; // Expone el error luego
  }
  return columna;
}

// convertir_fila: char -> int
/* convertir_fila toma un digito en formato char (1-8) correspondiente a una fila y 
lo retorna en formato int (0-7). */
int convertir_fila(char letra) {
  return letra - '1'; // La convierte en int
  // En caso de ser un dato Erróneo el programa lo expone luego
}

// fuera_del_tablero: Posicion -> int
/* fuera_del_tablero toma una Posicion y retorna si esta (True) o no (False) 
fuera del tablero. */
int fuera_del_tablero(Posicion jugada) {
  int fila = jugada.fila, columna = jugada.columna;
  return (fila < 0 || fila > 7 || columna < 0 || columna > 7);
}

// posicion_ya_ocupada: Tablero Posicion -> int
/* posicion_ya_ocupada toma un Tablero y una Posicion y retorna True si la 
posicion esta ocupada o False en caso contrario. */
int posicion_ya_ocupada(Tablero tablero, Posicion posicion) {
  char ficha = tablero[posicion.fila][posicion.columna];
  return (ficha == FICHA_BLANCA || ficha == FICHA_NEGRA);
}

// obtener_ficha: Tablero Posicion -> char
/* obtener_ficha toma un Tablero y una Posicion y retorna la ficha que hay en 
dicha posicion. */
char obtener_ficha(Tablero tablero, Posicion posicion) {
  return tablero[posicion.fila][posicion.columna];
}

// colocar_ficha: Tablero Posicion char -> None
/* colocar_ficha toma un Tablero, una posicion y una ficha y coloca la ficha 
en dicha posicion. */
void colocar_ficha(Tablero tablero, Posicion posicion, char ficha) {
  tablero[posicion.fila][posicion.columna] = ficha;
}

// modificar_tablero: Tablero Posicion char Direccion -> int
/* modificar_tablero toma como parámetros el tablero, la posición jugada 
(VÁLIDA), de quién es el turno y la dirección que quiere modificar (8 posibles).
La función hace el movimiento COMPLETO en la dirección indicada, es decir,
voltea todas las fichas correspondientes en una dirección siempre y cuando haya
fichas que voltear.
Luego, returna 1 si se voltearon fichas o 0 si no. */
int modificar_tablero(Tablero tablero, Posicion jugada, char turno, Direccion direccion) {
  int fichas_a_voltear = 0, d_horiz, d_vert;

  d_horiz = direccion.horizontal;
  d_vert = direccion.vertical;
  
  Posicion posicion_actual; // Posicion a desplazar
  for(int fichas_desplazadas = 1, continuar = 1;
      continuar; fichas_desplazadas++) {

    // Desplaza la posicion hacia la dirección establecida
    posicion_actual.columna = jugada.columna + fichas_desplazadas * d_horiz;
    posicion_actual.fila = jugada.fila + fichas_desplazadas * d_vert; 
    
    if(fuera_del_tablero(posicion_actual)) { // Fuera del tablero
      continuar = 0; // False
    }
    else {
      char ficha_actual = obtener_ficha(tablero, posicion_actual);
      if(fichas_desplazadas == 1) { // Si es adyacente a la jugada
        if(ficha_actual == POSICION_VACIA || ficha_actual == turno) // Si no hay nada o es del mismo color, termina 
          continuar = 0;
      }
      else if(ficha_actual == POSICION_VACIA) // Si no hay nada, termina
        continuar = 0;
      // Si luego de haber fichas del otro color, se reencuentra con una propia, entonces debe voltear las fichas
      else if(ficha_actual == turno) {
        fichas_a_voltear = fichas_desplazadas;
        continuar = 0;
      }
    }
  }

  // Voltea las fichas correspondientes si las hubiera
  for(int delta = 1; delta < fichas_a_voltear; delta++) {
    posicion_actual.columna = jugada.columna + delta * d_horiz;
    posicion_actual.fila = jugada.fila + delta * d_vert;
    colocar_ficha(tablero, posicion_actual, turno);
  }

  if(fichas_a_voltear) // != 0
    return 1;
  else
    return 0;
}

// realizar_jugada: Tablero Posicion char -> int
/* realizar_jugada toma como parámetros el tablero, la jugada y el turno.
Si la jugada es inválida, retorna False y no modifica el tablero.
Si en un principio la jugada es válida, entonces modifica el tablero según
corresponda en todas las direcciones, y si al hacerlo el tablero se modificó,
entonces la jugada era efectivamente válida, la realiza y retorna True. Por
otro lado, si el tablero NO se modificó, entonces la jugada era inválida, por
lo que retorna False.*/
int realizar_jugada(Tablero tablero, Posicion jugada, char turno) {
  
  if(fuera_del_tablero(jugada)) // Posicion fuera de rango?
    return 0; // False
  if(posicion_ya_ocupada(tablero, jugada)) // Posicion ocupada?
    return 0; // False

  Direccion direccion;
  int se_modifico = 0;
  for (int i = -1; i < 2; i++) {
    direccion.vertical = i;
    for (int j = -1; j < 2; j++) {
      direccion.horizontal = j;
      if (i || j) { // La direccion (0,0) no existe
        se_modifico = (modificar_tablero(tablero, jugada, turno, direccion) || se_modifico);
      }
    }
  }
  
  if(!se_modifico) {
    return 0;
  }

  colocar_ficha(tablero, jugada, turno);
  return 1;
}

// copiar_tablero: Tablero Tablero -> None
/* copiar_tablero toma dos Tableros. El primero es la copia y el segundo el 
original. La funcion copia los datos del segundo en el primero. */
void copiar_tablero(Tablero copia_tablero, Tablero tablero) {
  for(int i = 0; i < DIMENSION_TABLERO; i++) {
    for(int j = 0; j < DIMENSION_TABLERO; j++) {
      copia_tablero[i][j] = tablero[i][j];
    }
  }
}

// chequear_paso: Tablero char -> int
/* chequear_paso toma un tablero y un turno, y returna True si es válido pasar 
en ese tablero para esa persona, caso contrario retorna False.
Para ello chequea todas las posibles jugadas en una copia del tablero, y si 
algún tablero se modificó, entonces es ilegal "pasar". */
int chequear_paso(Tablero tablero, char turno) {
  Tablero copia_tablero = crear_tablero();
  
  copiar_tablero(copia_tablero, tablero);

  int continuar = 1;
  Posicion jugada;
  for(int i = 0; i < DIMENSION_TABLERO && continuar; i++) {
    jugada.fila = i;
    for(int j = 0; j < DIMENSION_TABLERO && continuar; j++) {
      jugada.columna = j;
      continuar = !realizar_jugada(copia_tablero, jugada, turno);
    }
  }
  
  liberar_tablero(copia_tablero);
  return continuar;
}

// imprimir_tablero: Tablero -> None
/* imprimir_tablero toma un tablero y lo imprime en consola. */
void imprimir_tablero(Tablero tablero) {
  printf("\n    A B C D E F G H\n");
  printf("    ---------------\n");

  for (int i = 0; i < DIMENSION_TABLERO; i++) {
    printf("%d | ", i + 1);
    for (int j = 0; j < DIMENSION_TABLERO; j++) {
      printf("%c ", tablero[i][j]);
    }
    printf("| %d\n", i + 1);
  }
  printf("    ---------------\n");
  printf("    A B C D E F G H\n\n");
}

// fin_del_juego: Tablero -> int
/* fin_del_juego toma un tablero y retorna si el juego ha terminado o no. */
int fin_del_juego(Tablero tablero) {
  return (chequear_paso(tablero, FICHA_NEGRA) && chequear_paso(tablero, FICHA_BLANCA)); 
}

// evaluar_y_mostrar_resultado: Tablero, Personas -> None
/* evaluar_y_mostrar_resultado toma un tablero de un juego finalizado y la 
lista de jugadores y muestra en pantalla los datos finales del juego. */
void evaluar_y_mostrar_resultado(Tablero tablero, Personas jugadores) {
  int blancas = 0, negras = 0, ficha;
  for (int i = 0; i < DIMENSION_TABLERO; i++) {
    for (int j = 0; j < DIMENSION_TABLERO; j++) {
      ficha = tablero[i][j];
      if(ficha == FICHA_BLANCA)
        blancas++;
      else if(ficha == FICHA_NEGRA)
        negras++;
    }
  }

  char jugador_blanco[255], jugador_negro[255];
  if(jugadores[0].color == FICHA_BLANCA) {
    strcpy(jugador_blanco, jugadores[0].nombre);
    strcpy(jugador_negro, jugadores[1].nombre);
  } else {
    strcpy(jugador_negro, jugadores[0].nombre);
    strcpy(jugador_blanco, jugadores[1].nombre);
  }
  
  printf("Fichas Blancas (%s): %d.\n", jugador_blanco, blancas);
  printf("Fichas Negras (%s): %d.\n", jugador_negro, negras);

  if(negras < blancas)
    printf("\nGanan blancas (%s).\n\n", jugador_blanco);
  else if(negras > blancas)
    printf("\nGanan negras (%s).\n\n", jugador_negro);
  else
    printf("\nEmpate.\n\n");
}

// jugadores_validos: Personas -> int
/* jugadores_validos toma la "lista" de juegadores y chequea que los datos sean 
válidos. */
int jugadores_validos(Personas jugadores) {
  char color_0 = jugadores[0].color;
  char color_1 = jugadores[1].color;

  if(color_0 == FICHA_BLANCA)
    if(color_1 == FICHA_NEGRA)
      return 1;
  if(color_0 == FICHA_NEGRA)
    if(color_1 == FICHA_BLANCA)
      return 1;

  return 0;
}

// turno_valido: char -> int
/* turno_valido toma un turno (quien empieza) y retorna si es válido o no. */
int turno_valido(char turno) {
  return (turno == FICHA_BLANCA || turno == FICHA_NEGRA);
}

// iniciar_codigos: None -> Codigos
/* Inicializa los codigos de error del programa en 0 en una variable de tipo 
Codigo. */
Codigos iniciar_codigos() {
  Codigos codigos = malloc(sizeof(CDError));

  codigos->hay_lineas_extra = 0;
  codigos->posicion_ilegal = 0;
  codigos->fin_de_archivo = 0;
  codigos->error_de_formato = 0;
  codigos->pasar_incorrecto = 0;
  codigos->linea = 61; // Maximo de jugadas posibles

  return codigos;
}

void liberar_codigos(Codigos codigos) {
  free(codigos);
  codigos = NULL;
}

char jugar(FILE * archivo_juego, Tablero tablero, Codigos codigos, char turno) {
  char lectura;
  Posicion jugada;
  int pasar = 0;
  for(int continuar = 1; continuar && codigos->linea; codigos->linea--) {
    lectura = fgetc(archivo_juego);
    if(lectura == EOF){
      continuar = 0;
      codigos->fin_de_archivo = 1;
    }
    else if(lectura != '\n') {
      jugada.columna = convertir_columna(lectura);
      jugada.fila = convertir_fila(fgetc(archivo_juego));
      
      continuar = realizar_jugada(tablero, jugada, turno);
      if(continuar) {
        pasar = 0;
        lectura = fgetc(archivo_juego); // desecho \n y si no hay, esta mal o EOF
        if(lectura != '\n') {
          continuar = 0; // error de formato o EOF?
          if(lectura == EOF) {
            codigos->fin_de_archivo = 1;
            turno = cambiar_turno(turno); //para seguir jugando
          } else
            codigos->error_de_formato = 1;
        }
      } else {
        codigos->posicion_ilegal = 1;
        codigos->hay_lineas_extra = 1;
      }
    } else {
      continuar = chequear_paso(tablero, turno);
      if(continuar)
        pasar++;
      else
        codigos->pasar_incorrecto = 1;
    }
    if(continuar) {
      turno = cambiar_turno(turno);
    }
    if(pasar == 2)
      continuar = 0;
  }
  if(codigos->hay_lineas_extra == 0 && fgetc(archivo_juego) != EOF)
    codigos->hay_lineas_extra = 1;
  
  return turno;
}

int juego_terminado(Tablero tablero, Personas jugadores, Codigos codigos) {
  if(fin_del_juego(tablero)) {
    if(codigos->hay_lineas_extra)
      printf("\nADVERTENCIA: El juego finalizo correctamente pero hay lineas de mas en el archivo.\n");
    imprimir_tablero(tablero);
    evaluar_y_mostrar_resultado(tablero, jugadores);
  } else {
    if(codigos->posicion_ilegal || codigos->error_de_formato) {
      printf("\nMovimiento invalido: Posicion ilegal o Error de formato (Linea %d del archivo).\n", 64 - codigos->linea);
      imprimir_tablero(tablero);
    }
    else if(codigos->pasar_incorrecto) {
      printf("\nMovimiento invalido: 'Pasar' no es valido en esta posicion (Linea %d del archivo).\n", 64 - codigos->linea);
      imprimir_tablero(tablero);
    }
    else if(codigos->fin_de_archivo)
      return 0;
  }
  return 1;
}