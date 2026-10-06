# Laboratório 6b — Respostas

## Exercício 1

**(a)** O código está em `tarifa/estacionamento.py`. Dois detalhes:

- `True` e `False` contam como número no Python, então eu rejeito eles com `TypeError`.
- Para "hora adicional ou fração" eu arredondo pra cima: `(minutos - 180 + 59) // 60`.

**(b) Classes de equivalência**

| Classe | Minutos | Cobra |
|--------|---------|-------|
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
| V4 | mais de 720 | R$ 60,00 |
| I1 | negativo | `ValueError` |
| I2 | não inteiro (float, str, None, bool) | `TypeError` |

**A faixa de 181 a 720 é uma classe só?** Não. Numa classe todo mundo tem que se comportar igual, e aqui o preço muda a cada 60 minutos (181 paga R$ 15,00, 720 paga R$ 39,00). Dá 9 subclasses, então tem fronteira *dentro* da faixa também (240/241, 300/301, ... 660/661).

**(c)** A suíte está em `tarifa/test_estacionamento.py`. É um teste parametrizado pras entradas válidas (representantes e limites de todas as fronteiras, com ids descritivos) e testes separados pra negativo (`ValueError`) e não inteiro (`TypeError`).

## Exercício 2

**(a) O que o estagiário errou**

| # | Menor entrada | Devolve | Deveria | Como arrumar |
|---|---------------|---------|---------|--------------|
| 1 | `0` | `ValueError` | `0.00` | trocar `minutos <= 0` por `minutos < 0` (zero é válido e grátis) |
| 2 | `15` | `12.00` | `0.00` | trocar `minutos < 15` por `minutos <= 15` |
| 3 | `181` | `12.00` | `15.00` | a divisão arredonda pra baixo, tem que ser pra cima: `(minutos - 180 + 59) // 60` |
| 4 | `720` | `60.00` | `39.00` | trocar `minutos < 720` por `minutos <= 720` |

O erro 3 pega todo minuto que não é múltiplo de 60 depois do 180. Exemplo: 241 devolve R$ 15,00 e devia ser R$ 18,00.

**(b)** Rodei a suíte do Exercício 1 na versão do estagiário (`tarifa/test_estagiario.py`) e ela **pega os 4 erros**. Deu 14 testes falhando e 62 passando.

- 13 falhas são de entradas válidas: `0` (erro 1), `15` (erro 2), `181`, `200`, `241`, `301`, `361`, `421`, `481`, `541`, `601`, `661` (erro 3) e `720` (erro 4).
- Os valores 240, 300, 360... passam porque são múltiplos de 60, aí arredondar pra cima ou pra baixo dá igual.
- A 14ª falha é o teste com `True`. A versão do estagiário aceita `True` como número. Isso não é um dos 4 erros da especificação, é uma exigência extra da minha suíte.

**(c)** Com um representante só por classe (8, 100, 300 e 1000), **nenhum erro aparece**. Os 4 testes passam (`tarifa/test_estagiario_representantes.py`). Por quê:

- 8, 100 e 1000 estão no meio das classes, longe das fronteiras onde os erros 1, 2 e 4 moram.
- O 300 deu certo na sorte: 300 − 180 = 120 é múltiplo de 60, então o erro de arredondamento do 3 some.
- Um representante só mostra que a classe funciona *naquele ponto*. Erro de `<` no lugar de `<=` e de arredondamento só aparece na fronteira.

## Exercício 3

**(a)** As quatro condições:

- **C**: tem credencial (PCD ou idoso)?
- **P**: compras ≥ R$ 150,00?
- **A**: cadastro no app?
- **T**: ficou até 240 minutos?

A regra em uma linha: `isento = C ou (T e (P ou A))`.

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
| T: até 240 min?       | X | N | S | S | S |
| Isento?               | S | N | S | S | N |

**Por que cada X pode ser X**

- **R1** (regras 1 a 8): com credencial é sempre isento. Compras, app e tempo não mudam nada.
- **R2** (regras 10, 12, 14, 16): sem credencial e com mais de 240 min, não tem isenção, ponto. Compras e app não adiantam, porque a isenção exige o tempo.
- **R3** (regras 9 e 11): sem credencial, até 240 min e compras ≥ 150. Isso já basta, então o app não importa.
- **R4 e R5** não têm X: sem credencial, até 240 min e compras baixas, quem decide é o app.

Conferindo: 8 + 4 + 2 + 1 + 1 = 16 regras. Nenhuma ficou de fora.

**(b)** A função está em `isencao/isencao.py`.

**(c)** O teste está em `isencao/test_isencao.py`, uma linha por regra (ids `R1` a `R5`). Usei valores-limite onde compras ou tempo decidem: 241 (R2), 150,00 e 240 (R3), 149,99 e 240 (R4 e R5).

## Exercício 4

**(a)** A versão errada está em `isencao/isento_errado.py`:

```python
def isento(pcd, valor_compra, cadastro_app, minutos):
    return bool(pcd or (minutos <= 240 and valor_compra >= 150.00) or cadastro_app)
```

O erro é que o app isenta mesmo passando de 240 minutos. O limite de tempo só vale pras compras.

Na tabela completa ela erra as **regras 10 (N,S,S,N) e 14 (N,N,S,N)**: devolve `True` e era pra ser `False`. Mesmo assim ela passa nos 5 casos do colega (`isencao/test_colega_vs_errado.py`).

**(b)** O que o colega deixou de verificar: ele assumiu que o X "não importa", então encheu os X com qualquer valor e nunca testou se isso era verdade. Nos casos dele, o app só aparece como `True` na R4, com 100 minutos. Nunca testou app + tempo estourado, que é exatamente onde a versão errada falha.

Casos corrigidos (`isencao/test_colega_corrigido.py`), ainda com 5 casos:

| Regra | pcd | compra | app | min | esperado |
|-------|-----|--------|-----|-----|----------|
| R1 | True  | 0.00   | False    | 1000 | True |
| R2 | False | 150.00 | **True** | 241  | False |
| R3 | False | 150.00 | False    | 240  | True |
| R4 | False | 149.99 | True     | 240  | True |
| R5 | False | 149.99 | False    | 240  | False |

Na versão errada, o caso R2 falha (devolve `True` quando devia ser `False`), então o erro é pego (`isencao/test_corrigido_vs_errado.py`). Na versão correta, os 5 passam.

**(c) Regra geral pra escolher o valor de um X:** escolha o valor que mais "tentaria" um erro. Ou seja, o valor que faria o programa dar um resultado **diferente do esperado** se a condição estivesse influenciando por engano. Na R2, por exemplo, usei `app=True` e `compra=150,00`, que puxam pra isenção, pra pegar quem isenta quando não devia. Na R1, usei tudo contra a isenção (0,00 de compra, sem app, 1000 min).

Se não der pra achar um valor "tentador" único, vale variar os valores dos X entre as regras, pra que cada valor apareça pelo menos uma vez. Mesmo assim, 5 casos não cobrem tudo. Pra garantir de verdade, só testando as 16 regras da tabela completa.
