import pytest

from isento_errado import isento

CASOS = [
    (True, 0.00, False, 1000, True),
    (False, 150.00, True, 241, False),
    (False, 150.00, False, 240, True),
    (False, 149.99, True, 240, True),
    (False, 149.99, False, 240, False),
]


@pytest.mark.parametrize("pcd,compra,app,minutos,esperado", CASOS,
                         ids=["R1", "R2", "R3", "R4", "R5"])
def test_isento_errado_detectado(pcd, compra, app, minutos, esperado):
    assert isento(pcd, compra, app, minutos) is esperado
