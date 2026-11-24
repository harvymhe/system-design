"""Pruebas de reservas recurrentes."""

import pytest

from recurrentes_ejercicio3 import AgendaDeCancha


def test_calendario_se_crea_una_vez_por_fecha():
    agenda = AgendaDeCancha("cancha-1")

    assert agenda.calendario("2026-11-16") is agenda.calendario("2026-11-16")
    assert agenda.calendario("2026-11-16") is not agenda.calendario("2026-11-23")


def test_reservar_cada_semana_crea_ids_y_fechas_en_orden():
    agenda = AgendaDeCancha("cancha-1")

    resultado = agenda.reservar_cada_semana(
        "entreno", "futbol", "2026-11-16", 9, 10, 3
    )

    assert resultado == [
        ("2026-11-16", "reservada"),
        ("2026-11-23", "reservada"),
        ("2026-11-30", "reservada"),
    ]
    assert agenda.calendario("2026-11-16").franja_de("entreno-1").inicio == 9
    assert agenda.calendario("2026-11-23").franja_de("entreno-2").inicio == 9
    assert agenda.calendario("2026-11-30").franja_de("entreno-3").inicio == 9


def test_una_fecha_ocupada_se_omite_y_las_siguientes_se_reservan():
    agenda = AgendaDeCancha("cancha-1")
    agenda.calendario("2026-11-23").reservar("otra", "otro", 9, 10)

    resultado = agenda.reservar_cada_semana(
        "entreno", "futbol", "2026-11-16", 9, 10, 3
    )

    assert resultado == [
        ("2026-11-16", "reservada"),
        ("2026-11-23", "ocupada"),
        ("2026-11-30", "reservada"),
    ]


def test_limite_de_horas_se_omite_y_las_siguientes_se_reservan():
    agenda = AgendaDeCancha("cancha-1")
    agenda.calendario("2026-11-16").reservar("previa", "futbol", 7, 8)

    resultado = agenda.reservar_cada_semana(
        "entreno", "futbol", "2026-11-16", 9, 11, 2
    )

    assert resultado == [
        ("2026-11-16", "limite"),
        ("2026-11-23", "reservada"),
    ]


@pytest.mark.parametrize("semanas", [0, 13, -1, 1.5, True])
def test_numero_de_semanas_invalido_no_crea_reservas(semanas):
    agenda = AgendaDeCancha("cancha-1")

    with pytest.raises(ValueError):
        agenda.reservar_cada_semana(
            "entreno", "futbol", "2026-11-16", 9, 10, semanas
        )

    assert agenda.calendario("2026-11-16").reservas() == []


@pytest.mark.parametrize("semanas", [1, 12])
def test_acepta_los_limites_validos_de_semanas(semanas):
    agenda = AgendaDeCancha("cancha-1")

    resultado = agenda.reservar_cada_semana(
        "entreno", "futbol", "2026-11-16", 9, 10, semanas
    )

    assert len(resultado) == semanas
    assert all(estado == "reservada" for _, estado in resultado)
