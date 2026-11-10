def confirmar(pedido, centavos, gateway, email, tentativas=3):
    if tentativas < 1:
        raise ValueError("tentativas deve ser pelo menos 1")

    restantes = tentativas
    while True:
        try:
            status = gateway.cobrar(pedido, centavos)
            break
        except ConnectionError:
            restantes -= 1
            if restantes == 0:
                email.enviar(pedido, "falha na cobranca")
                raise

    if status == "aprovado":
        email.enviar(pedido, "pedido confirmado")
    return status
