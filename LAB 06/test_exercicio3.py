import pytest

from imc_frete import classificar_por_faixas, classificar_vento

def test_classificar_por_faixas_generica():
    faixas = [(10, "baixo"), (20, "medio"), (None, "alto")]
    assert classificar_por_faixas(5, faixas) == "baixo"
    assert classificar_por_faixas(15, faixas) == "medio"
    assert classificar_por_faixas(25, faixas) == "alto"


@pytest.mark.parametrize("velocidade, esperado", [
    (19, "calmo"),
    (20, "moderado"),
    (39, "moderado"),
    (40, "forte"),
    (59, "forte"),
    (60, "tempestade"),
], ids=[
    "abaixo_da_fronteira_20",
    "na_fronteira_20",
    "abaixo_da_fronteira_40",
    "na_fronteira_40",
    "abaixo_da_fronteira_60",
    "na_fronteira_60",
])
def test_fronteiras_vento(velocidade, esperado):
    assert classificar_vento(velocidade) == esperado
