#ifndef __FUNCIONES_H__
#define __FUNCIONES_H__

#include "definiciones.h"
#include <stdio.h>

Tablero crear_tablero();

void liberar_tablero(Tablero tablero);

int guardar_tablero(char const *archivo_nombre, Tablero tablero, char turno);

Personas obtener_jugadores(FILE *archivo_juego);

void liberar_jugadores(Personas jugador);

char cambiar_turno(char turno);

char obtener_turno(FILE *archivo_juego);

int convertir_columna(char letra);

int convertir_fila(char letra);

int fuera_del_tablero(Posicion jugada);

int posicion_ya_ocupada(Tablero tablero, Posicion posicion);

char obtener_ficha(Tablero tablero, Posicion posicion);

void colocar_ficha(Tablero tablero, Posicion posicion, char ficha);
//
int modificar_tablero(Tablero tablero, Posicion jugada, char turno, Direccion direccion);

int realizar_jugada(Tablero tablero, Posicion jugada, char turno);
//
void copiar_tablero(Tablero copia_tablero, Tablero tablero);

int chequear_paso(Tablero tablero, char turno);

void imprimir_tablero(Tablero tablero);

int fin_del_juego(Tablero tablero);

void evaluar_y_mostrar_resultado(Tablero tablero, Personas jugadores);

int jugadores_validos(Personas jugadores);

int turno_valido(char turno);

Codigos iniciar_codigos();

void liberar_codigos(Codigos codigos);

char jugar(FILE * archivo_juego, Tablero tablero, Codigos codigos, char turno);

int juego_terminado(Tablero tablero, Personas jugadores, Codigos codigos);

#endif