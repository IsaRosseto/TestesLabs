import pytest

from isencao import isento


@pytest.mark.parametrize("pcd,compra,app,minutos,esperado", [
    (True, 0.00, False, 100, True),     # R1
    (False, 200.00, False, 300, False), # R2
    (False, 200.00, False, 100, True),  # R3
    (False, 50.00, True, 100, True),    # R4
    (False, 50.00, False, 100, False),  # R5
], ids=["R1", "R2", "R3", "R4", "R5"])
def test_isento(pcd, compra, app, minutos, esperado):
    assert isento(pcd, compra, app, minutos) is esperado
