CC = gcc
CFLAGS = -I./Headers

all: main tests

main: main.c funciones.c
	$(CC) $(CFLAGS) -o main main.c funciones.c

tests: tests.c funciones.c
	$(CC) $(CFLAGS) -o tests tests.c funciones.c

clean:
	rm -f main tests
