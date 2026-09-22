import pytest

from imc_frete import calcular_imc, categorizar_imc


# fronteiras: 18.5, 25 e 30
# para cada uma, testamos o valor logo abaixo e o valor exato,
# o que já cobre as 6 posições-limite sem precisar de 9 casos

@pytest.mark.parametrize("imc, esperado", [
    (18.4, "abaixo do peso"),
    (18.5, "peso normal"),
    (24.9, "peso normal"),
    (25.0, "sobrepeso"),
    (29.9, "sobrepeso"),
    (30.0, "obesidade"),
], ids=[
    "abaixo_da_fronteira_18.5",
    "na_fronteira_18.5",
    "abaixo_da_fronteira_25",
    "na_fronteira_25",
    "abaixo_da_fronteira_30",
    "na_fronteira_30",
])
def test_fronteiras_imc(imc, esperado):
    assert categorizar_imc(imc) == esperado


def test_peso_invalido_levanta_erro():
    with pytest.raises(ValueError):
        calcular_imc(0, 1.80)


def test_altura_invalida_levanta_erro():
    with pytest.raises(ValueError):
        calcular_imc(70, -1.80)
