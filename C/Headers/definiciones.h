#ifndef __DEFINICIONES_H__
#define __DEFINICIONES_H__

#define DIMENSION_TABLERO 8
#define CANTIDAD_JUGADORES 2
#define POSICION_VACIA 'X'
#define FICHA_BLANCA 'B'
#define FICHA_NEGRA 'N'

/* A cada jugador se lo representa como una estructura que contiene un 
char *nombre y un char color. Seria el equivalente a una tupla de una string y 
un char. */
typedef struct {
  char *nombre, color;
} Jugador;

// Personas := Jugador * (Personas[0], Personas[1], etc.)
typedef Jugador * Personas;

/* A cada posicion del tablero (x,y) se lo representa como una estructura de 
dos int: fila, columna. Es decir cada posicion es una tupla de numeros. */
typedef struct {
  int fila, columna;
} Posicion;

/* A cada direccion se la representa como una estructura de dos int: 
horizontal, vertical. En donde cada uno puede valer -1, 0 o 1; siempre y cuando 
no tengan ambos simultaneamente 0. Representa las 8 direcciones del tablero. 
Cada dirección es una tupla de numeros. */
typedef struct {
  int horizontal, vertical;
} Direccion;

// Tablero := char ** (Tablero[fila][columna])
typedef char ** Tablero;

/* Representa los codigos de error que puede tener la evaluacion del archivo. */
typedef struct {
  int hay_lineas_extra, posicion_ilegal;
  int fin_de_archivo, error_de_formato, pasar_incorrecto;
  int linea;
} CDError;

/* Los codigos serán puntero para modificarlos dentro de cualquier funcion, por 
lo tanto se accede a cada dato mediante ->. la idea no es crear listas como en 
el caso de Personas. */
// Codigos := CDError *
typedef CDError * Codigos;

#endif