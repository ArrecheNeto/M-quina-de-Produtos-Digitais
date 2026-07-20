---
description: Roda a esteira COMPLETA — do tema ao produto validável — os 7 passos em sequência
argument-hint: "[habilidade ou tema] — ex.: sei fazer tráfego pago para dentistas"
---

Rode a **esteira completa** da Máquina de Produtos Digitais: os 7 passos, um após o outro, parando pra confirmar com o usuário nos pontos que exigem decisão dele.

## Preparação

1. Leia `maquina-config.json`. Se não existir, rode o fluxo do `/maquina-setup` primeiro (rápido).
2. Defina o tema com `$ARGUMENTS` ou perguntando qual habilidade explorar.

## Execução — encadeada, com checkpoints

Execute na ordem, cada um seguindo sua skill e gravando seu entregável em `produtos/[slug]/`, atualizando o `maquina.db` e regenerando o `painel.html` a cada passo:

1. **Pesquisa de problemas** (skill `pesquisa-problemas`) → mostra o problema-alvo. **Checkpoint:** confirme com o usuário antes de seguir.
2. **Promessa e oferta** (skill `promessa-oferta`) → mostra a promessa. **Checkpoint.**
3. **Produto mínimo** (skill `produto-minimo`).
4. **Página de vendas** (skill `pagina-vendas`).
5. **Mapa de compradores** (skill `mapa-compradores`).
6. **Lançamento inicial** (skill `lancamento-inicial`).
7. **Validação** (skill `validacao`) → só pode rodar de verdade depois que o usuário lançar e tiver números; nos passos 1–6 a esteira PARA aqui e explica que a validação vem após o lançamento.

Nos checkpoints, se o usuário quiser mudar algo, ajuste antes de avançar. Não pule passos sem avisar.

## Saída

Ao fim dos passos 1–6, mostre um resumo do projeto (com os caminhos dos 6 entregáveis e o link do `painel.html`) e o roteiro de lançamento. Deixe claro que o **/validacao** fecha a esteira depois que ele rodar o lançamento.
