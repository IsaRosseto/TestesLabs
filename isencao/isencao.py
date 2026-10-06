"""Exercicio 3(b): regra de isencao da tarifa."""


def isento(pcd, valor_compra, cadastro_app, minutos):
    """True se o cliente esta isento da tarifa.

    Com credencial (PCD/idoso): sempre isento.
    Sem credencial: isento se minutos <= 240 E (compras >= 150,00 OU cadastro no app).
    """
    if pcd:
        return True
    return minutos <= 240 and (valor_compra >= 150.00 or cadastro_app)
