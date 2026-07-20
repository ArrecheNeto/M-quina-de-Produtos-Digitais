---
description: Passo 1 — pesquisa as dores reais do mercado e escolhe o problema que vira produto
argument-hint: "[habilidade ou tema] — ex.: edição de vídeo para infoprodutores"
---

Execute o **Passo 1 da esteira** seguindo a skill `pesquisa-problemas`.

## Preparação

1. Leia `maquina-config.json` na pasta conectada. Se não existir, oriente a rodar `/setup`.
2. Defina o tema: use `$ARGUMENTS` se informado; senão, pergunte qual das `habilidades` do config o usuário quer explorar (ou um tema novo).

## Execução

Siga a skill `pesquisa-problemas` para descobrir dores REAIS (não suposições):

- Pesquise onde o público reclama de verdade — use `WebSearch` e as ferramentas do Claude in Chrome (carregue via ToolSearch se necessário) para varrer Reddit, grupos, fóruns, comentários de YouTube, avaliações e redes. Colete falas literais.
- Agrupe em 3 a 5 dores recorrentes. Para cada uma: quem sente, com que frequência, o que já tentaram, quanto dói (1–5), e se pagariam pra resolver.
- Escolha **UM problema-alvo**: o que mais dói + público que já gasta dinheiro + você consegue resolver com o que sabe.

## Saída

1. Crie a pasta `produtos/[slug]/` (slug a partir do tema) e grave `1-pesquisa-problemas.md` com: as falas coletadas (com a fonte), o mapa das dores, e o problema-alvo escolhido com justificativa.
2. Registre/atualize o projeto no `maquina.db` (`etapa='promessa'`, `problema`=resumo do problema-alvo, `publico`) e regenere `painel.html` seguindo a skill `painel-produtos`.
3. Mostre ao usuário o problema-alvo e as 2 dores reservas, e sugira: **/promessa** para transformar isso na promessa vencedora.
