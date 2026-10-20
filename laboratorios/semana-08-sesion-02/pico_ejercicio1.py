"""Ejercicio 1: el pico de inicio de semestre contra un solo servidor.

Corre esto para ver el resultado:

    python3 pico_ejercicio1.py

Y las pruebas con:

    pytest test_pico_ejercicio1.py
"""

from servidor import Servidor


def simular_pico(servidor, cantidad, duracion):
    atendidas = 0
    rechazadas = 0

    for _ in range(cantidad):
        if servidor.atender(duracion):
            atendidas += 1
        else:
            rechazadas += 1

    return atendidas, rechazadas


if __name__ == "__main__":
    print("Escenario A, un servidor de capacidad 100:")
    print(simular_pico(Servidor("unico", 100), 250, 5))

    print("Escenario B, un servidor mas grande, capacidad 300:")
    print(simular_pico(Servidor("grande", 300), 250, 5))

    print("Escenario C, el mismo servidor grande, caido:")
    grande = Servidor("grande", 300)
    grande.caer()
    print(simular_pico(grande, 250, 5))
