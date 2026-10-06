"""Exercicio 1(a): tarifa do estacionamento do shopping."""


def calcular_tarifa(minutos):
    """Devolve a tarifa (em reais) para `minutos` inteiros de permanencia.

    0 a 15      -> 0.00 (tolerancia)
    16 a 180    -> 12.00
    181 a 720   -> 12.00 + 3.00 por hora adicional ou fracao
    > 720       -> 60.00 (diaria)
    negativo    -> ValueError
    nao inteiro -> TypeError
    """
    # bool e subclasse de int em Python; True/False nao sao tempos validos.
    if isinstance(minutos, bool) or not isinstance(minutos, int):
        raise TypeError("minutos deve ser inteiro")
    if minutos < 0:
        raise ValueError("minutos nao pode ser negativo")
    if minutos <= 15:
        return 0.00
    if minutos <= 180:
        return 12.00
    if minutos <= 720:
        horas_adicionais = (minutos - 180 + 59) // 60  # teto da divisao por 60
        return 12.00 + 3.00 * horas_adicionais
    return 60.00
