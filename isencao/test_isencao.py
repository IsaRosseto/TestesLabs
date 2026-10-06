import pytest

from isencao import isento


@pytest.mark.parametrize(
    "pcd, compra, app, minutos, esperado",
    [
        # R1: credencial = S; demais X (todos "contra": sem compras, sem app, muito tempo)
        (True, 0.00, False, 1000, True),
        # R2: sem credencial, minutos 241 (limite); compras e app X (ambos "a favor" da isencao)
        (False, 150.00, True, 241, False),
        # R3: sem credencial, 240 min (limite), compras 150,00 (limite); app X = False
        (False, 150.00, False, 240, True),
        # R4: sem credencial, 240 min, compras 149,99 (limite), app = S
        (False, 149.99, True, 240, True),
        # R5: sem credencial, 240 min, compras 149,99, sem app
        (False, 149.99, False, 240, False),
    ],
    ids=["R1", "R2", "R3", "R4", "R5"],
)
def test_isento(pcd, compra, app, minutos, esperado):
    assert isento(pcd, compra, app, minutos) is esperado
