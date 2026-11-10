from unittest.mock import Mock, call

import pytest

from confirmacao import confirmar


def test_cobra_uma_vez_com_pedido_e_valor():
    gateway = Mock()
    gateway.cobrar.return_value = "aprovado"

    confirmar("P1", 9700, gateway, Mock())

    gateway.cobrar.assert_called_once_with("P1", 9700)


def test_repete_a_cobranca_apos_connection_error():
    gateway = Mock()
    gateway.cobrar.side_effect = [ConnectionError(), ConnectionError(), "aprovado"]

    status = confirmar("P1", 500, gateway, Mock())

    assert status == "aprovado"
    assert gateway.cobrar.call_args_list == [call("P1", 500)] * 3


def test_nao_passa_do_limite_de_tentativas():
    gateway = Mock()
    gateway.cobrar.side_effect = ConnectionError()

    with pytest.raises(ConnectionError):
        confirmar("P1", 500, gateway, Mock(), tentativas=4)

    assert gateway.cobrar.call_count == 4


def test_tentativas_igual_a_um_nao_repete():
    gateway = Mock()
    gateway.cobrar.side_effect = ConnectionError()

    with pytest.raises(ConnectionError):
        confirmar("P1", 500, gateway, Mock(), tentativas=1)

    gateway.cobrar.assert_called_once_with("P1", 500)


@pytest.mark.parametrize("tentativas", [0, -1])
def test_tentativas_invalidas_nao_cobram(tentativas):
    gateway = Mock()

    with pytest.raises(ValueError):
        confirmar("P1", 500, gateway, Mock(), tentativas=tentativas)

    gateway.cobrar.assert_not_called()
