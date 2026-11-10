## Exercício 1 – Frete em dólar

**Por que não usar um serviço real de cotação?**
Porque a taxa muda o tempo todo, então não existe valor esperado fixo para conferir no assert. O teste ainda ficaria lento, dependeria de rede e de um terceiro, e falharia por motivos alheios ao nosso código. E não dá para forçar um timeout num serviço real quando a gente quer, que é justamente o cenário do item (c). O stub devolve a taxa que escolhermos e o Mock simula a falha na hora.


## Exercício 2 – Cobrar de novo sem avisar duas vezes

**Por que conferir as chamadas não é excesso?**
Confirmar quase não tem o que comparar no retorno: o que importa é quantas vezes cobrou, com quais argumentos e quantos e-mails mandou. Cobrar duas vezes um pedido já aprovado ou avisar o cliente duas vezes são exatamente os bugs que esse código pode ter, e só dá para pegar olhando as chamadas. Conferir como o código faz por dentro seria excesso; conferir o que ele pede ao mundo externo, não.
