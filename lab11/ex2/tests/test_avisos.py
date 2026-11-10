from unittest.mock import Mock

import pytest

from confirmacao import confirmar


def test_aprovado_devolve_status_e_avisa():
    gateway, email = Mock(), Mock()
    gateway.cobrar.return_value = "aprovado"

    status = confirmar("P1", 500, gateway, email)

    assert status == "aprovado"
    email.enviar.assert_called_once_with("P1", "pedido confirmado")


def test_negado_devolve_status_sem_avisar():
    gateway, email = Mock(), Mock()
    gateway.cobrar.return_value = "negado"

    status = confirmar("P1", 500, gateway, email)

    assert status == "negado"
    gateway.cobrar.assert_called_once_with("P1", 500)
    email.enviar.assert_not_called()


def test_falha_na_ultima_tentativa_avisa_e_propaga():
    gateway, email = Mock(), Mock()
    gateway.cobrar.side_effect = ConnectionError("rede fora")

    with pytest.raises(ConnectionError, match="rede fora"):
        confirmar("P1", 500, gateway, email)

    assert gateway.cobrar.call_count == 3
    email.enviar.assert_called_once_with("P1", "falha na cobranca")


def test_sucesso_apos_falha_nao_avisa_falha():
    gateway, email = Mock(), Mock()
    gateway.cobrar.side_effect = [ConnectionError(), "aprovado"]

    confirmar("P1", 500, gateway, email)

    email.enviar.assert_called_once_with("P1", "pedido confirmado")
