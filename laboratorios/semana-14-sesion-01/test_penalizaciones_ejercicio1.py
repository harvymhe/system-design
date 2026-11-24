"""Pruebas del Ejercicio 1. Empieza vacio: cada prueba se escribe antes
del codigo que la hace pasar, una a la vez, en el orden de la lista de
penalizaciones_ejercicio1.py.
"""

from penalizaciones_ejercicio1 import HistorialDePenalizaciones, puntos_por_cancelar

def test_cancelar_con_mas_de_un_dia_no_penaliza():
    assert puntos_por_cancelar(2000) == 0

def test_cancelar_el_mismo_dia_penalizar():
    assert puntos_por_cancelar(600) == 1

def test_cancelar_a_ultima_hora_penalizar():
    assert puntos_por_cancelar(30) == 2

def test_cancelacion_casos_frontera():
    assert puntos_por_cancelar(1440) == 0
    assert puntos_por_cancelar(120) == 1

def test_estudiante_con_tres_puntos_esta_bloqueado():
    historial = HistorialDePenalizaciones()

    historial.cancelar("ana", 600)  # 1 punto
    assert historial.esta_bloqueado("ana") is False

    historial.cancelar("ana", 30)   # 2 puntos
    assert historial.esta_bloqueado("ana") is True


def test_no_presentarse_suma_tres_puntos():
    historial = HistorialDePenalizaciones()

    historial.no_presentarse("ana")

    assert historial.puntos_de("ana") == 3
    assert historial.esta_bloqueado("ana") is True


def test_las_penalizaciones_son_independientes_por_estudiante():
    historial = HistorialDePenalizaciones()

    historial.cancelar("ana", 30)

    assert historial.puntos_de("ana") == 2
    assert historial.puntos_de("beto") == 0
    assert historial.esta_bloqueado("beto") is False


def test_estudiante_sin_puntos_no_esta_bloqueado():
    historial = HistorialDePenalizaciones()

    assert historial.esta_bloqueado("ana") is False
