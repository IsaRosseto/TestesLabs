
def calcular_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        raise ValueError("peso e altura devem ser positivos")
    return peso / (altura ** 2)


def categorizar_imc(imc):
    return classificar_por_faixas(imc, FAIXAS_IMC)


def classificar_pessoa(peso, altura):
    imc = calcular_imc(peso, altura)
    return categorizar_imc(imc)


def classificar_por_faixas(valor, faixas):
    for limite_superior, rotulo in faixas:
        if limite_superior is None or valor < limite_superior:
            return rotulo
    raise ValueError("tabela de faixas incompleta")


FAIXAS_IMC = [
    (18.5, "abaixo do peso"),
    (25, "peso normal"),
    (30, "sobrepeso"),
    (None, "obesidade"),
]

FAIXAS_VENTO = [
    (20, "calmo"),
    (40, "moderado"),
    (60, "forte"),
    (None, "tempestade"),
]


def classificar_vento(velocidade):
    return classificar_por_faixas(velocidade, FAIXAS_VENTO)



def tem_frete_gratis(valor_compra, cliente_premium, peso):
    return valor_compra >= 200 and cliente_premium and peso <= 30
