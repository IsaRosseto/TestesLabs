"""Exercicio 4(a): implementacao ERRADA de isento.

Defeito: o cadastro no app isenta independentemente do tempo
(o limite de 240 minutos so vale para o criterio das compras).

    errado:  pcd or (minutos <= 240 and compra >= 150) or app
    correto: pcd or (minutos <= 240 and (compra >= 150 or app))

Erra, na tabela completa (ordem das condicoes: credencial, compras>=150, app, perm<=240),
as regras 10 (N,S,S,N) e 14 (N,N,S,N): devolve True onde o esperado e False.
Passa nos cinco casos do colega, que so usam app=True com 100 minutos (R4).
"""


def isento(pcd, valor_compra, cadastro_app, minutos):
    return bool(pcd or (minutos <= 240 and valor_compra >= 150.00) or cadastro_app)
