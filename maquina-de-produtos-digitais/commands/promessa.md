---
description: Passo 2 — transforma o problema na promessa vencedora e na oferta
argument-hint: "[slug do projeto] — opcional, usa o projeto mais recente"
---

Execute o **Passo 2 da esteira** seguindo a skill `promessa-oferta`.

## Preparação

1. Identifique o projeto: use `$ARGUMENTS` (slug) ou o projeto mais recente do `maquina.db` que esteja na etapa `promessa`.
2. Leia `produtos/[slug]/1-pesquisa-problemas.md` para pegar o problema-alvo e as falas reais.

## Execução

Siga a skill `promessa-oferta`:

- Escreva 3 candidatas de **promessa** (resultado específico + prazo + sem a dor). Escolha a mais forte e justifique.
- Monte a **oferta** com a equação de valor: sonho realizado, alta probabilidade de sucesso, pouco tempo/esforço. Defina o que está incluso, bônus que quebram objeções, e a garantia.
- Sugira **formato** do produto (ebook, curso curto, template, mentoria, comunidade) e uma **faixa de preço** ancorada no valor, não no custo.
- Dê um **nome** provisório ao produto.

## Saída

1. Grave `produtos/[slug]/2-promessa-oferta.md` com a promessa vencedora, a oferta completa, o nome e a faixa de preço.
2. Atualize o `maquina.db` (`etapa='produto'`, `promessa`, `titulo`=nome, `formato`, `preco`) e regenere `painel.html` (skill `painel-produtos`).
3. Mostre a promessa e a oferta, e sugira: **/produto** para montar o produto mínimo que entrega essa promessa.
