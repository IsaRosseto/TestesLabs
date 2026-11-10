class CotacaoIndisponivel(Exception):
    """A cotação não respondeu a tempo."""


class ConversorFrete:
    def __init__(self, cotacao):
        self.cotacao = cotacao

    def em_centavos_de_real(self, centavos_de_dolar):
        try:
            taxa = self.cotacao.dolar()
        except TimeoutError as erro:
            raise CotacaoIndisponivel("cotacao do dolar indisponivel") from erro

        if taxa <= 0:
            raise ValueError(f"taxa invalida: {taxa}")

        return round(centavos_de_dolar * taxa)
