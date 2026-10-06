"""Exercicio 4(a): o teste ORIGINAL do colega aplicado a isento_errado.

Todos passam: o defeito nao e detectado.
"""
import pytest

from isento_errado import isento


@pytest.mark.parametrize("pcd,compra,app,minutos,esperado", [
    (True, 0.00, False, 100, True),     # R1
    (False, 200.00, False, 300, False), # R2
    (False, 200.00, False, 100, True),  # R3
    (False, 50.00, True, 100, True),    # R4
    (False, 50.00, False, 100, False),  # R5
], ids=["R1", "R2", "R3", "R4", "R5"])
def test_isento_errado_passa_no_colega(pcd, compra, app, minutos, esperado):
    assert isento(pcd, compra, app, minutos) is esperado
