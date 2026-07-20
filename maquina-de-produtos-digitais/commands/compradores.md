---
description: Passo 5 — mapeia 10 lugares/pessoas onde o comprador está, com abordagem personalizada (o elo que falta)
argument-hint: "[slug do projeto] — opcional, usa o projeto na etapa compradores"
---

Execute o **Passo 5 da esteira** seguindo a skill `mapa-compradores`.

Este é o passo que faz a validação ter alvo: sem saber PRA QUEM e ONDE oferecer, não há como validar.

## Preparação

1. Identifique o projeto (slug em `$ARGUMENTS` ou o mais recente na etapa `compradores`).
2. Leia `1-pesquisa-problemas.md` e `2-promessa-oferta.md` do projeto.

## Execução

Siga a skill `mapa-compradores`. Use `WebSearch` e o Claude in Chrome para achar lugares REAIS onde o público-alvo já se reúne:

- 10 canais concretos: comunidades, grupos, subreddits, perfis, hashtags, fóruns, listas, eventos — com o link/nome real e por que o comprador está ali.
- Para cada um: a **abordagem** certa (não é spam — é oferecer valor / convidar / conversar) e uma **mensagem-modelo** personalizada pra aquele contexto.
- Marque quais servem para os **10 primeiros beta-compradores** (oferta da v1 antes de produzir tudo).

Regra: nada de comprar lista, disparo em massa ou spam. O objetivo são 10 conversas certas, não 10 mil mensagens.

## Saída

1. Grave `produtos/[slug]/5-compradores.md` com os 10 canais, a abordagem e as mensagens-modelo.
2. Atualize `maquina.db` (`etapa='lancamento'`, `compradores`=JSON com os 10 canais) e regenere `painel.html`.
3. Mostre a lista e sugira: **/lancamento** para montar o plano de lançamento inicial.
