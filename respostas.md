# Laboratório 6b — Respostas

## Exercício 1

**(a)** Implementação em `tarifa/estacionamento.py`. Observação: `bool` é subclasse de `int` em Python, então `True`/`False` são rejeitados explicitamente com `TypeError`. A hora adicional ou fração usa o teto da divisão: `(minutos - 180 + 59) // 60`.

**(b) Classes de equivalência**

| Classe | Entrada | Resultado |
|--------|---------|-----------|
| V1 | 0 a 15 | R$ 0,00 |
| V2 | 16 a 180 | R$ 12,00 |
| V3.1 | 181 a 240 | R$ 15,00 |
| V3.2 | 241 a 300 | R$ 18,00 |
| V3.3 | 301 a 360 | R$ 21,00 |
| V3.4 | 361 a 420 | R$ 24,00 |
| V3.5 | 421 a 480 | R$ 27,00 |
| V3.6 | 481 a 540 | R$ 30,00 |
| V3.7 | 541 a 600 | R$ 33,00 |
| V3.8 | 601 a 660 | R$ 36,00 |
| V3.9 | 661 a 720 | R$ 39,00 |
| V4 | acima de 720 | R$ 60,00 |
| I1 | negativo | `ValueError` |
| I2 | não inteiro (`float`, `str`, `None`, `bool`) | `TypeError` |

**A faixa de 181 a 720 não é uma classe só.** Numa classe, todos os elementos levam ao mesmo comportamento, e aqui o valor cobrado muda a cada 60 minutos: 181 paga R$ 15,00 e 720 paga R$ 39,00. São 9 subclasses (V3.1 a V3.9), com 8 fronteiras internas (240/241, 300/301, ..., 660/661), além das fronteiras externas 180/181 e 720/721.

**(c)** Suíte em `tarifa/test_estacionamento.py`: um teste parametrizado para as válidas (representantes e limites de todas as fronteiras, ids descritivos) e testes separados para `ValueError` (negativos) e `TypeError` (float, str, None, bool).

## Exercício 2

**(a) Divergências (sem executar)**

| # | Menor entrada | Devolvido | Esperado | Correção |
|---|---------------|-----------|----------|----------|
| 1 | `0` | `ValueError` | `0.00` | `minutos <= 0` → `minutos < 0` (zero é válido e grátis) |
| 2 | `15` | `12.00` | `0.00` | `minutos < 15` → `minutos <= 15` |
| 3 | `181` | `12.00` | `15.00` | divisão com piso (`// 60`) → teto: `(minutos - 180 + 59) // 60` |
| 4 | `720` | `60.00` | `39.00` | `minutos < 720` → `minutos <= 720` |

A divergência 3 afeta todo minuto que não seja múltiplo de 60 após o 180. Por exemplo, 241 devolve 15,00 e deveria devolver 18,00.

**(b)** A suíte do Exercício 1, importando da versão do estagiário (`tarifa/test_estagiario.py`), **detecta todas as quatro divergências**: 14 testes falham, 62 passam.

- Falham 13 casos válidos: `0` (div. 1); `15` (div. 2); `181`, `200`, `241`, `301`, `361`, `421`, `481`, `541`, `601`, `661` (div. 3); `720` (div. 4). Os valores 240, 300, 360, ... passam porque, sendo múltiplos de 60, o piso e o teto coincidem.
- O 14º é `test_tempo_booleano`: `True` não é rejeitado. Isso não é uma das quatro divergências da especificação, e sim um comportamento extra que a minha suíte exige.

**(c)** Com um representante por classe (8, 100, 300 e 1000), **nenhuma divergência é detectada**: os 4 testes passam (`tarifa/test_estagiario_representantes.py`).

- 8 → 0,00, 100 → 12,00 e 1000 → 60,00 estão no interior das classes, longe das fronteiras onde os defeitos 1, 2 e 4 estão.
- 300 → 18,00 está certo por acaso: 300 − 180 = 120 é múltiplo de 60, então piso e teto coincidem e escondem o defeito 3.
- Um representante só prova que a classe funciona no ponto escolhido. Erros de comparação (`<` no lugar de `<=`) e de arredondamento só aparecem nas fronteiras.

## Exercício 3

**(a)** Condições: **C** = credencial, **P** = compras ≥ R$ 150,00, **A** = cadastro no app, **T** = permanência ≤ 240 min.
Regra: `isento = C ou (T e (P ou A))`.

**Tabela completa (2⁴ = 16 regras)**

| Regra | C | P | A | T | Isento? |
|-------|---|---|---|---|---------|
| 1  | S | S | S | S | S |
| 2  | S | S | S | N | S |
| 3  | S | S | N | S | S |
| 4  | S | S | N | N | S |
| 5  | S | N | S | S | S |
| 6  | S | N | S | N | S |
| 7  | S | N | N | S | S |
| 8  | S | N | N | N | S |
| 9  | N | S | S | S | S |
| 10 | N | S | S | N | N |
| 11 | N | S | N | S | S |
| 12 | N | S | N | N | N |
| 13 | N | N | S | S | S |
| 14 | N | N | S | N | N |
| 15 | N | N | N | S | N |
| 16 | N | N | N | N | N |

**Tabela reduzida (5 regras)**

| Condição | R1 | R2 | R3 | R4 | R5 |
|----------|----|----|----|----|----|
| C: credencial?        | S | N | N | N | N |
| P: compras ≥ 150,00?  | X | X | S | N | N |
| A: cadastro no app?   | X | X | X | S | N |
| T: permanência ≤ 240? | X | N | S | S | S |
| Isento?               | S | N | S | S | N |

**Justificativa dos X**

- **R1** (regras 1 a 8): com credencial, o veículo é sempre isento. P, A e T não influenciam o resultado.
- **R2** (regras 10, 12, 14 e 16): sem credencial e com T = N, a permanência já impede a isenção. P e A não importam, pois a isenção exige T.
- **R3** (regras 9 e 11): sem credencial, com T = S e P = S, a regra "P ou A" já é verdadeira, então A não importa.
- **R4** e **R5** não têm X: com C = N, T = S e P = N, o resultado depende de A.

Conferência: 8 + 4 + 2 + 1 + 1 = 16 regras cobertas.

**(b)** Implementação em `isencao/isencao.py`.

**(c)** Teste em `isencao/test_isencao.py`, com ids `R1` a `R5`. Valores-limite onde compras ou permanência decidem: 241 (R2); 150,00 e 240 (R3); 149,99 e 240 (R4 e R5).

## Exercício 4

**(a)** `isencao/isento_errado.py`:

```python
def isento(pcd, valor_compra, cadastro_app, minutos):
    return bool(pcd or (minutos <= 240 and valor_compra >= 150.00) or cadastro_app)
```

O defeito é que o cadastro no app isenta sem respeitar o limite de 240 minutos. Na tabela completa (ordem C, P, A, T), ela **erra as regras 10 (N,S,S,N) e 14 (N,N,S,N)**: devolve `True`, mas o esperado é `False`. Ela passa nos cinco casos do colega (`isencao/test_colega_vs_errado.py`).

**(b)** O teste do colega supôs que o X vale qualquer coisa e pode ser preenchido com o valor que for mais cômodo. Ele fixou `app=False` nas regras R1 e R2 (e `app=True` só na R4, com 100 min). Assim, **nunca verificou** que, com T = N, o cadastro no app também não isenta, ou seja, que o X de A na R2 realmente não importa.

Casos corrigidos (`isencao/test_colega_corrigido.py`), mantendo cinco casos:

| Regra | pcd | compra | app | min | esperado |
|-------|-----|--------|-----|-----|----------|
| R1 | True  | 0.00   | False | 1000 | True |
| R2 | False | 150.00 | **True** | 241 | False |
| R3 | False | 150.00 | False | 240 | True |
| R4 | False | 149.99 | True  | 240 | True |
| R5 | False | 149.99 | False | 240 | False |

Contra `isento_errado`, o caso R2 falha (`True` no lugar de `False`) e o defeito é detectado (`isencao/test_corrigido_vs_errado.py`). Contra a implementação correta, os cinco passam.

**(c) Regra geral:** para uma condição marcada com X, escolha o valor que, se a condição passasse a influenciar o resultado indevidamente, faria o programa devolver algo **diferente do esperado**. Em outras palavras, o valor mais "tentador" para o defeito. Na R2 isso é `app=True` e `compra=150,00`, que "a favor" da isenção deveriam enganar uma implementação errada. Na R1 são os valores contra a isenção (0,00; sem app; 1000 min).

Complemento: se não houver um único valor adversário, **varie os valores dos X entre as regras** para que cada valor de cada X apareça ao menos uma vez. Para cobrir de fato todas as combinações escondidas, seriam necessários os 16 casos da tabela completa.
