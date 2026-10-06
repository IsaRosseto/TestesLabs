"""Exercicio 2(c): um unico representante por classe valida (sem valores-limite)."""
import pytest

from estacionamento_estagiario import calcular_tarifa


@pytest.mark.parametrize(
    "minutos, esperado",
    [(8, 0.00), (100, 12.00), (300, 18.00), (1000, 60.00)],
    ids=["gratis_8", "fixo_100", "variavel_300", "diaria_1000"],
)
def test_representantes(minutos, esperado):
    assert calcular_tarifa(minutos) == esperado
