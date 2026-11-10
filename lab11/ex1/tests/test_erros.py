from unittest.mock import Mock

import pytest

from conversor import ConversorFrete, CotacaoIndisponivel
from test_conversao import CotacaoFixa


@pytest.mark.parametrize("taxa", [0, -1, -0.01])
def test_taxa_menor_ou_igual_a_zero_levanta_value_error(taxa):
    conversor = ConversorFrete(CotacaoFixa(taxa))

    with pytest.raises(ValueError):
        conversor.em_centavos_de_real(100)


def test_timeout_vira_cotacao_indisponivel():
    cotacao = Mock()
    cotacao.dolar.side_effect = TimeoutError("sem resposta")
    conversor = ConversorFrete(cotacao)

    with pytest.raises(CotacaoIndisponivel) as erro:
        conversor.em_centavos_de_real(100)

    cotacao.dolar.assert_called_once_with()
    assert isinstance(erro.value.__cause__, TimeoutError)
