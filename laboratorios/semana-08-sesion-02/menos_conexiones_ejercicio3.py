"""Ejercicio 3: balanceador de menos conexiones (least connections).

Corre las pruebas con:
    pytest test_menos_conexiones_ejercicio3.py


Las pruebas tambien usan tu BalanceadorRoundRobin del Ejercicio 2, para
comparar los dos algoritmos con el mismo trafico.
"""


class BalanceadorMenosConexiones:
    def __init__(self, servidores):
        self.servidores = servidores

    def enviar(self, duracion):
        servidor_seleccionado = None

        for servidor in self.servidores:
            if not servidor.health_check() or not servidor.puede_atender():
                continue

            if (
                servidor_seleccionado is None
                or servidor.conexiones_activas()
                < servidor_seleccionado.conexiones_activas()
            ):
                servidor_seleccionado = servidor

        if servidor_seleccionado is not None:
            servidor_seleccionado.atender(duracion)
            return servidor_seleccionado.nombre

        return None
