from imc_frete import classificar_pessoa


def test_abaixo_do_peso():
    assert classificar_pessoa(50, 1.80) == "abaixo do peso"


def test_peso_normal():
    assert classificar_pessoa(70, 1.80) == "peso normal"


def test_sobrepeso():
    assert classificar_pessoa(85, 1.80) == "sobrepeso"


def test_obesidade():
    assert classificar_pessoa(100, 1.80) == "obesidade"
