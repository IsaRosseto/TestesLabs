import pytest

from imc_frete import tem_frete_gratis


@pytest.mark.parametrize("valor_compra, cliente_premium, peso, esperado", [
    (250, True, 20, True),    # R1: V V V
    (250, True, 40, False),   # R2: V V F
    (250, False, 20, False),  # R3: V F V
    (250, False, 40, False),  # R4: V F F
    (150, True, 20, False),   # R5: F V V
    (150, True, 40, False),   # R6: F V F
    (150, False, 20, False),  # R7: F F V
    (150, False, 40, False),  # R8: F F F
], ids=["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"])
def test_tabela_decisao_frete(valor_compra, cliente_premium, peso, esperado):
    assert tem_frete_gratis(valor_compra, cliente_premium, peso) == esperado


# tabela reduzida por don't care:
#
#   Regra | valor_compra | premium | peso   | resultado
#   ------|---------------|---------|--------|----------
#   RR1   |     >=200     |   sim   |  <=30  |  gratis
#   RR2   |     <200      |    -    |    -   |  cobrado
#   RR3   |     >=200     |   nao   |    -   |  cobrado
#   RR4   |     >=200     |   sim   |  >30   |  cobrado
#
# justificativa: o resultado é um "E" (and) das três condições, então
# assim que uma condição falha o resultado já é "cobrado" independente
# das condições seguintes:
#   - RR2: se valor_compra < 200, premium e peso não mudam o resultado
#   - RR3: com valor_compra ok mas sem premium, o peso não importa mais
#   - RR4: com valor_compra e premium ok, só falta checar o peso

@pytest.mark.parametrize("valor_compra, cliente_premium, peso, esperado", [
    (250, True, 20, True),     
    (150, True, 20, False),    
    (250, False, 20, False),   
    (250, True, 40, False),    
], ids=["RR1_gratis", "RR2_valor_baixo", "RR3_sem_premium", "RR4_peso_alto"])
def test_tabela_decisao_frete_reduzida(valor_compra, cliente_premium, peso, esperado):
    assert tem_frete_gratis(valor_compra, cliente_premium, peso) == esperado
