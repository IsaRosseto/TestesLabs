"""Exercicio 1(c): suite de classes de equivalencia e valores-limite."""
import pytest

from estacionamento import calcular_tarifa


@pytest.mark.parametrize(
    "minutos, esperado",
    [
        # Classe 0-15: gratis
        (0, 0.00),
        (8, 0.00),
        (14, 0.00),
        (15, 0.00),
        # Classe 16-180: R$ 12,00
        (16, 12.00),
        (100, 12.00),
        (179, 12.00),
        (180, 12.00),
        # Classe 181-720: degraus de 60 min (fronteiras internas)
        (181, 15.00),
        (200, 15.00),
        (240, 15.00),
        (241, 18.00),
        (300, 18.00),
        (301, 21.00),
        (360, 21.00),
        (361, 24.00),
        (420, 24.00),
        (421, 27.00),
        (480, 27.00),
        (481, 30.00),
        (540, 30.00),
        (541, 33.00),
        (600, 33.00),
        (601, 36.00),
        (660, 36.00),
        (661, 39.00),
        (720, 39.00),
        # Classe > 720: diaria
        (721, 60.00),
        (1000, 60.00),
        (100000, 60.00),
    ],
    ids=[
        "gratis_min_0",
        "gratis_representante_8",
        "gratis_abaixo_limite_14",
        "gratis_limite_15",
        "fixo_limite_16",
        "fixo_representante_100",
        "fixo_abaixo_limite_179",
        "fixo_limite_180",
        "hora1_limite_181",
        "hora1_representante_200",
        "hora1_limite_240",
        "hora2_limite_241",
        "hora2_limite_300",
        "hora3_limite_301",
        "hora3_limite_360",
        "hora4_limite_361",
        "hora4_limite_420",
        "hora5_limite_421",
        "hora5_limite_480",
        "hora6_limite_481",
        "hora6_limite_540",
        "hora7_limite_541",
        "hora7_limite_600",
        "hora8_limite_601",
        "hora8_limite_660",
        "hora9_limite_661",
        "hora9_limite_720",
        "diaria_limite_721",
        "diaria_representante_1000",
        "diaria_valor_alto",
    ],
)
def test_tarifa_valida(minutos, esperado):
    assert calcular_tarifa(minutos) == esperado


def test_tempo_negativo_limite():
    with pytest.raises(ValueError):
        calcular_tarifa(-1)


def test_tempo_negativo_representante():
    with pytest.raises(ValueError):
        calcular_tarifa(-100)


def test_tempo_float():
    with pytest.raises(TypeError):
        calcular_tarifa(15.5)


def test_tempo_string():
    with pytest.raises(TypeError):
        calcular_tarifa("30")


def test_tempo_none():
    with pytest.raises(TypeError):
        calcular_tarifa(None)


def test_tempo_booleano():
    with pytest.raises(TypeError):
        calcular_tarifa(True)
