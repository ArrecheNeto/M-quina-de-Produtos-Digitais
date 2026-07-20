---
description: Passo 3 — monta o produto mínimo que entrega a promessa (o mínimo pra vender, não o curso inteiro)
argument-hint: "[slug do projeto] — opcional, usa o projeto na etapa produto"
---

Execute o **Passo 3 da esteira** seguindo a skill `produto-minimo`.

## Preparação

1. Identifique o projeto (slug em `$ARGUMENTS` ou o mais recente na etapa `produto`).
2. Leia `1-pesquisa-problemas.md` e `2-promessa-oferta.md` do projeto.

## Execução

Siga a skill `produto-minimo`. A regra de ouro: **o mínimo que entrega a promessa e já pode ser vendido** — nada de produzir tudo antes de validar.

- Defina a estrutura no formato escolhido (módulos/aulas, capítulos, ou blocos do template/mentoria).
- Para cada parte: o que entrega, o resultado intermediário, e o esforço de produção (baixo/médio/alto).
- Marque o **MVP vendável**: as partes mínimas necessárias pra cumprir a promessa e cobrar por isso. O resto vira "fase 2" (produz só depois que vender).
- Liste os entregáveis de apoio (checklist, template, bônus) que aumentam o valor percebido com pouco esforço.

## Saída

1. Grave `produtos/[slug]/3-produto-minimo.md` com a estrutura completa, o MVP vendável destacado e o plano de produção.
2. Atualize `maquina.db` (`etapa='pagina'`, `produto`=resumo da estrutura) e regenere `painel.html`.
3. Mostre a estrutura e o MVP, e sugira: **/pagina** para gerar a página de vendas.
