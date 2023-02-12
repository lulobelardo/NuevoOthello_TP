#ifndef __TESTS_H__
#define __TESTS_H__

#include <assert.h>
#include <string.h>
#include <unistd.h>
#include "funciones.h"

void test_crear_tablero();

void test_guardar_tablero();

void test_obtener_jugadores();

void test_cambiar_turno();

void test_convertir_columna();

void test_convertir_fila();

void test_fuera_del_tablero();

void test_posicion_ya_ocupada();

void test_obtener_ficha();

void test_colocar_ficha();

void test_realizar_jugada();

void test_chequear_paso();

void test_fin_del_juego();

void test_jugadores_validos();

void test_turno_valido();

void test_jugar();

#endif