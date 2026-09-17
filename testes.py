import os
import pytest

from carteira import (
    CarteiraDigital,
    SaldoInsuficienteError,
    classificar_transacao,
    transferir,
)


def test_saldoInicial():
    carteira = CarteiraDigital()
    saldo = carteira.saldo
    assert saldo == 0


def test_saldo_inicial_customizado():
    carteira = CarteiraDigital(saldo_inicial=50)
    saldo = carteira.saldo
    assert saldo == 50


def test_depositar():
    carteira = CarteiraDigital(saldo_inicial=100)
    carteira.depositar(30)
    assert carteira.saldo == 130


def test_sacar_saldo_disponivel():
    carteira = CarteiraDigital(saldo_inicial=100)
    carteira.sacar(40)
    assert carteira.saldo == 60


# saldo insuficiente 

def test_sacar_saldoInsuficiente():
    carteira = CarteiraDigital(saldo_inicial=100)
    with pytest.raises(SaldoInsuficienteError) as exc_info:
        carteira.sacar(150)
    assert str(exc_info.value) == "saldo insuficiente"


def test_sacar_saldoInsuficiente_semAlterar():
    carteira = CarteiraDigital(saldo_inicial=100)
    with pytest.raises(SaldoInsuficienteError):
        carteira.sacar(150)
    assert carteira.saldo == 100


# fixture 

@pytest.fixture
def carteira_com_log():
    log_path = "carteira_teste.log"

    if os.path.exists(log_path):
        os.remove(log_path)

    carteira = CarteiraDigital(saldo_inicial=0, log_path=log_path)

    yield carteira

    if os.path.exists(log_path):
        os.remove(log_path)


def test_deposito_grava_linha_correta_no_log(carteira_com_log):
    carteira = carteira_com_log
    carteira.depositar(75)
    with open(carteira.log_path) as f:
        conteudo = f.read()
    assert conteudo == "deposito:75\n"


# faixa de valor

@pytest.mark.parametrize(
    "valor, esperado",
    [
        (0, "pequena"),
        (99, "pequena"),
        (100, "media"),
        (999, "media"),
        (1000, "grande"),
        (5000, "grande"),
    ],
    ids=[
        "zero_e_pequena",
        "limite_99_ainda_pequena",
        "limite_100_ja_e_media",
        "limite_999_ainda_media",
        "limite_1000_ja_e_grande",
        "valor_bem_acima_e_grande",
    ],
)
def test_classificar_transacao(valor, esperado):
    resultado = classificar_transacao(valor)
    assert resultado == esperado


# transferência entre carteiras

@pytest.fixture
def par_de_carteiras():
    origem = CarteiraDigital(saldo_inicial=200, log_path="origem_teste.log")
    destino = CarteiraDigital(saldo_inicial=0, log_path="destino_teste.log")

    yield origem, destino

    for path in (origem.log_path, destino.log_path):
        if os.path.exists(path):
            os.remove(path)


@pytest.mark.parametrize(
    "valor",
    [10, 50, 200],
    ids=["valor_pequeno", "valor_medio", "valor_igual_ao_saldo_total"],
)
def test_transferencia_bemSucedida(par_de_carteiras, valor):
    origem, destino = par_de_carteiras
    saldo_origem_antes = origem.saldo
    saldo_destino_antes = destino.saldo
    transferir(origem, destino, valor)
    assert origem.saldo == saldo_origem_antes - valor
    assert destino.saldo == saldo_destino_antes + valor


def test_transferencia_semAlterar(par_de_carteiras):
    origem, destino = par_de_carteiras
    saldo_origem_antes = origem.saldo
    saldo_destino_antes = destino.saldo
    with pytest.raises(SaldoInsuficienteError):
        transferir(origem, destino, 300)
    assert origem.saldo == saldo_origem_antes
    assert destino.saldo == saldo_destino_antes
