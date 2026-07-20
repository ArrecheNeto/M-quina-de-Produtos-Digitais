---
name: validacao
description: Esta skill deve ser usada no Passo 7 da Máquina de Produtos Digitais — ler os sinais do lançamento, calcular as taxas e dar o veredito (validar, ajustar ou descartar) com base em números e falas. Acione quando o usuário disser "validar", "analisar resultado", "deu certo?", "veredito", "e agora" ou rodar /validacao.
---

# Passo 7 — Validação

Objetivo: decidir com dado, não com esperança. O lançamento gerou sinais; aqui a gente lê e recomenda o próximo movimento.

## Entradas (peça ao usuário)

- Alcance/conversas iniciadas.
- Cliques na página de vendas.
- Vendas fechadas (e valor).
- As **objeções** que ouviu (o que as pessoas disseram ao não comprar).

Se ele ainda não lançou, explique que a validação precisa desses números — não dá pra validar no vácuo.

## Análise

1. Calcule o funil: interesse → clique → compra. Compare com a meta do passo 6.
2. Leia as objeções: elas dizem ONDE está o furo (promessa fraca, preço, público errado, canal errado, prova insuficiente).
3. Dê o **veredito**:
   - **VALIDADO** — bateu ou passou a meta. Recomende escalar: produzir a fase 2, subir preço, abrir mais canais, pedir depoimentos.
   - **AJUSTAR** — houve interesse mas pouca compra. Aponte o passo exato pra refazer e a hipótese (ex.: "interesse alto, conversão baixa → preço ou garantia: volte ao /promessa"; "ninguém clica → promessa/canal: /problema ou /compradores").
   - **DESCARTAR** — sem interesse real nem após ajuste de canal. O problema não dói o suficiente ou o público não paga. Melhor liberar energia pra outro tema — e isso é uma vitória barata, não um fracasso.
4. Seja honesto com os números. Não maquie sinal fraco de "quase".

## Entregável

`produtos/[slug]/7-validacao.md` com as taxas, o veredito e a recomendação concreta. Atualize `maquina.db` (`etapa='validado'` se validado, ou mantenha em `validacao` com nota de ajuste; grave `validacao`=veredito) e regenere o painel.

## Princípio

O objetivo da esteira não é ter razão — é descobrir rápido e barato o que o mercado quer pagar. Ajustar e descartar fazem parte do método.
