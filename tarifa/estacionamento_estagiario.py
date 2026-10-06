def calcular_tarifa(minutos):
    if not isinstance(minutos, int):
        raise TypeError("minutos deve ser inteiro")
    if minutos <= 0:
        raise ValueError("minutos nao pode ser negativo")
    if minutos < 15:
        return 0.00
    if minutos <= 180:
        return 12.00
    if minutos < 720:
        return 12.00 + 3.00 * ((minutos - 180) // 60)
    return 60.00
