---
description: Passo 6 — cria o plano de lançamento inicial (sem ads, sem audiência gigante)
argument-hint: "[slug do projeto] — opcional, usa o projeto na etapa lancamento"
---

Execute o **Passo 6 da esteira** seguindo a skill `lancamento-inicial`.

## Preparação

1. Identifique o projeto (slug em `$ARGUMENTS` ou o mais recente na etapa `lancamento`).
2. Leia `2-promessa-oferta.md`, `4-pagina-vendas.html` e `5-compradores.md` do projeto.

## Execução

Siga a skill `lancamento-inicial` para montar um lançamento simples de 7 dias, focado nos 10 primeiros compradores — sem tráfego pago, sem depender de audiência grande:

- Um cronograma dia a dia: o que postar/enviar/oferecer em cada dia, e em qual dos canais do passo 5.
- Os textos prontos: 3 a 5 mensagens/posts de aquecimento, a mensagem de abertura da oferta e a de fechamento (escassez honesta).
- A meta de validação (ex.: 10 conversas → 3 vendas) e a oferta de fundador (desconto/bônus pra quem entra na v1).
- O que medir a cada dia (respostas, cliques, vendas).

## Saída

1. Grave `produtos/[slug]/6-lancamento.md` com o cronograma de 7 dias, todos os textos e as metas.
2. Atualize `maquina.db` (`etapa='validacao'`, `lancamento`=resumo do plano) e regenere `painel.html`.
3. Mostre o cronograma e sugira: rodar o lançamento e depois **/validacao** para ler os resultados e decidir go/no-go.
