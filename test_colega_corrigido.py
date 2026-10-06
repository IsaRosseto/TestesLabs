"""Exercicio 4(b): teste do colega com os valores dos X corrigidos (5 casos).

Contra a implementacao correta (isencao.py) todos passam.
"""
import pytest

from isencao import isento

CASOS = [
    (True, 0.00, False, 1000, True),    # R1: X = valores "contra" a isencao
    (False, 150.00, True, 241, False),  # R2: X = valores "a favor" da isencao
    (False, 150.00, False, 240, True),  # R3: app X = False
    (False, 149.99, True, 240, True),   # R4
    (False, 149.99, False, 240, False), # R5
]


@pytest.mark.parametrize("pcd,compra,app,minutos,esperado", CASOS,
                         ids=["R1", "R2", "R3", "R4", "R5"])
def test_isento_corrigido(pcd, compra, app, minutos, esperado):
    assert isento(pcd, compra, app, minutos) is esperado
