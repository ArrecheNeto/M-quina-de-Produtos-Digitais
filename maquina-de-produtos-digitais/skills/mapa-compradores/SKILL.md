---
name: mapa-compradores
description: Esta skill deve ser usada no Passo 5 da Máquina de Produtos Digitais — mapear 10 lugares reais onde o comprador está, com a abordagem certa e mensagens-modelo, e marcar os 10 primeiros beta-compradores. Acione quando o usuário disser "onde vender", "achar comprador", "pra quem oferecer", "primeiros clientes" ou rodar /compradores ou /maquina.
---

# Passo 5 — Mapa de compradores (o elo que falta)

Objetivo: responder "pra QUEM e ONDE eu ofereço isso amanhã?". Sem alvo, o lançamento e a validação não têm em quem bater. Aqui não se compra audiência — se encontra onde ela já está.

## Fluxo

1. A partir do público do passo 1, use `WebSearch` e o Claude in Chrome para achar **10 canais reais** onde esse público já se reúne:
   - Comunidades e grupos (Discord, Facebook, Telegram, Circle, Skool)
   - Subreddits e fóruns específicos
   - Perfis/creators que esse público segue (parcerias, comentários)
   - Hashtags e buscas onde eles pedem ajuda
   - Eventos, newsletters, listas, marketplaces do nicho
2. Para cada canal registre: nome + link real, por que o comprador está ali, tamanho/atividade (se der pra ver), e as regras (alguns proíbem divulgação — respeite).
3. Defina a **abordagem** de cada um. Nunca spam. Padrões que funcionam:
   - **Dar valor primeiro** — responder dúvidas, postar um mini-conteúdo útil, e a oferta vem como consequência.
   - **Conversa 1:1** — puxar papo com quem demonstrou a dor, entender, e oferecer.
   - **Parceria** — creator/admin que já tem a audiência.
   - **Convite** — chamar pra um grupo/lista onde a oferta acontece.
4. Escreva uma **mensagem-modelo personalizada** por contexto (não a mesma pra todos): abertura que mostra que entende a dor, valor, e um convite leve — sem link jogado.
5. Marque quais canais são os melhores para os **10 primeiros beta-compradores** (a oferta de fundador da v1).

## Regra

10 conversas certas > 10 mil mensagens. Nada de comprar lista, disparo em massa ou fingir. O objetivo é validar com gente real, e reputação vale mais que velocidade.

## Entregável

`produtos/[slug]/5-compradores.md` com os 10 canais, abordagem e mensagens-modelo, e os marcados como beta. Atualize `maquina.db` (etapa `lancamento`, `compradores` em JSON) e regenere o painel.
