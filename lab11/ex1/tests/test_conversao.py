import pytest

from conversor import ConversorFrete


class CotacaoFixa:
    """Stub escrito à mão: devolve sempre a taxa recebida."""

    def __init__(self, taxa):
        self.taxa = taxa

    def dolar(self):
        return self.taxa


@pytest.mark.parametrize(
    "centavos, taxa, esperado",
    [
        (100, 5.0, 500),
        (0, 5.0, 0),
        (200, 5.25, 1050),
        (1, 5.5, 6),      # 5,5 -> 6
        (5, 0.5, 2),      # 2,5 vai para o par (2)
        (7, 0.5, 4),      # 3,5 vai para o par (4)
        (3, 0.5, 2),      # 1,5 vai para o par (2)
    ],
)
def test_converte_e_arredonda(centavos, taxa, esperado):
    conversor = ConversorFrete(CotacaoFixa(taxa))

    assert conversor.em_centavos_de_real(centavos) == esperado
