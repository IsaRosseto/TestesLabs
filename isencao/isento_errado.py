
def isento(pcd, valor_compra, cadastro_app, minutos):
    return bool(pcd or (minutos <= 240 and valor_compra >= 150.00) or cadastro_app)
