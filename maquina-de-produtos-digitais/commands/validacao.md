---
description: Passo 7 — analisa os sinais do lançamento e dá o veredito (validar, ajustar ou descartar)
argument-hint: "[slug do projeto] — opcional, usa o projeto na etapa validacao"
---

Execute o **Passo 7 da esteira** seguindo a skill `validacao`.

## Preparação

1. Identifique o projeto (slug em `$ARGUMENTS` ou o mais recente na etapa `validacao`).
2. Peça ao usuário os números reais do lançamento: quantas conversas/alcance, quantos cliques na página, quantas vendas, e o que as pessoas responderam (as objeções). Se ele ainda não lançou, explique que a validação precisa desses dados.

## Execução

Siga a skill `validacao` para ler os sinais e decidir:

- Calcule as taxas (interesse → clique → compra) e compare com a meta do passo 6.
- Classifique o veredito: **VALIDADO** (repetir e escalar), **AJUSTAR** (o quê mudar — promessa, preço, público ou canal) ou **DESCARTAR** (o problema não dói o suficiente / não pagam) — sempre com o porquê baseado nos números e nas falas.
- Se AJUSTAR: aponte exatamente qual passo refazer (ex.: volte pro /promessa com um novo ângulo).
- Se VALIDADO: liste os próximos passos pra escalar (produzir a fase 2, aumentar preço, abrir mais canais).

## Saída

1. Grave `produtos/[slug]/7-validacao.md` com as taxas, o veredito e a recomendação.
2. Atualize `maquina.db` (`etapa='validado'` ou mantenha em `validacao` se for ajustar; grave `validacao`=veredito) e regenere `painel.html`.
3. Dê o veredito com clareza e o próximo passo concreto.
