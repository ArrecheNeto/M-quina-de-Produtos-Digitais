---
name: pesquisa-problemas
description: Esta skill deve ser usada no Passo 1 da Máquina de Produtos Digitais — pesquisar dores reais do mercado a partir de uma habilidade ou tema, agrupar em problemas recorrentes e escolher o problema-alvo que vira produto. Acione quando o usuário disser "pesquisar problema", "achar dor", "que produto criar", "validar tema" ou rodar /problema ou /maquina.
---

# Passo 1 — Pesquisa de problemas

Objetivo: sair da suposição. O produto nasce de uma dor que o mercado JÁ tem e JÁ tenta resolver pagando — não de uma ideia bonita na cabeça do criador.

## Princípio

Não se inventa demanda. Procura-se onde as pessoas já reclamam, já buscam solução e já gastam dinheiro. A habilidade do usuário é a lente; a dor real do público é o alvo.

## Fluxo

1. **Ouça o mercado onde ele fala de verdade.** Com `WebSearch` e o Claude in Chrome (carregue via ToolSearch se preciso), varra:
   - Reddit e fóruns do nicho (buscas como "tema + problema/help/frustrated/como faço")
   - Comentários de vídeos do YouTube sobre o tema (onde aparecem os "eu não consigo...")
   - Grupos e comunidades (Facebook, Discord, comunidades pagas públicas)
   - Avaliações de produtos concorrentes (o que falta / o que irrita — 1 a 3 estrelas)
   - Perguntas repetidas (Quora, "people also ask", tópicos de suporte)
2. **Colete falas literais.** Copie 8–15 frases reais de pessoas descrevendo a dor, cada uma com a fonte. Falas > adjetivos.
3. **Agrupe em 3 a 5 dores recorrentes.** Para cada dor: quem sente, frequência, o que já tentaram (e por que não resolveu), intensidade (1–5), e sinal de que pagam pra resolver (existe concorrente cobrando? buscam "curso/serviço/ferramenta de X"?).
4. **Escolha UM problema-alvo** com o filtro: dói muito (≥4) + público que já gasta + resolvível com o que o usuário sabe + específico o bastante pra uma promessa clara. Guarde as 2 dores reservas.

## Critérios de um bom problema-alvo

- Específico ("editores de podcast perdem horas cortando silêncio" > "criadores querem produtividade").
- Urgente ou recorrente (dói agora, ou toda semana).
- Já tem dinheiro em volta (concorrentes, buscas comerciais, ferramentas pagas).
- Cabe na habilidade do usuário sem ele virar outra pessoa.

## Entregável

`produtos/[slug]/1-pesquisa-problemas.md` contendo: as falas coletadas com fonte, o mapa das 3–5 dores, e o problema-alvo escolhido com justificativa e as 2 reservas. Registre o resumo e o público no `maquina.db` (etapa `promessa`) e regenere o painel (skill `painel-produtos`).

## Evite

Confirmar a ideia que o usuário já queria (viés de confirmação). Se os dados não sustentarem a dor, diga isso — é mais barato descobrir agora.
