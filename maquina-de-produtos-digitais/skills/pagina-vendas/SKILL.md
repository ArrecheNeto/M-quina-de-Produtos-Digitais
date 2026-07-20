---
name: pagina-vendas
description: Esta skill deve ser usada no Passo 4 da Máquina de Produtos Digitais — escrever a copy e gerar a página de vendas em HTML único e autossuficiente a partir da oferta e do produto. Acione quando o usuário disser "página de vendas", "landing", "carta de vendas", "criar a página" ou rodar /pagina ou /maquina.
---

# Passo 4 — Página de vendas

Objetivo: transformar a oferta num arquivo HTML pronto pra abrir no navegador e publicar em qualquer lugar (sem build, sem dependências). Copy que converte + design limpo.

## Estrutura de conversão (nesta ordem)

1. **Acima da dobra** — a promessa (headline), subheadline que reforça o resultado, e um CTA visível.
2. **A dor** — espelhe o problema com as falas reais do passo 1. A pessoa precisa pensar "é exatamente isso".
3. **A virada** — existe outro caminho; apresente o método/produto como a ponte.
4. **O que é o produto** — o que a pessoa recebe, em partes concretas (do passo 3).
5. **O que está incluso + bônus** — lista com valor percebido; bônus quebrando objeções.
6. **Prova / autoridade** — depoimentos (placeholders se não houver), sua credencial, resultados. Use `[SEU DEPOIMENTO AQUI]` onde faltar.
7. **Oferta e preço** — ancoragem (valor total dos itens) → preço → parcelamento se fizer sentido.
8. **Garantia** — remova o risco.
9. **FAQ** — 5 a 8 perguntas que quebram as objeções reais do público.
10. **CTA final** — repita a oferta e o botão. Espalhe 2–3 CTAs ao longo da página.

## Copy

- Tom vem do `maquina-config.json` (`autor.tom`). Fale a língua do público, não a sua.
- Foco em resultado e transformação, não em recursos. "Você vai conseguir X" > "o módulo 3 tem 40 minutos".
- Frases curtas. Subtítulos escaneáveis. Sem jargão vazio.
- Honestidade: nada de promessa mentirosa, renda garantida ou escassez falsa.

## Técnico

- Um único arquivo `.html`, CSS embutido em `<style>`, sem CDN, sem JS obrigatório (pode ter um pouco de JS inline pra FAQ acordeão, opcional).
- Responsivo (mobile-first), fontes de sistema, bom contraste, botões grandes.
- Placeholders claros e fáceis de achar: `[LINK DE PAGAMENTO]`, `[SEU E-MAIL/WHATSAPP]`, `[SEU DEPOIMENTO AQUI]`, `[SUA FOTO]`.
- Pode partir de `references/pagina-modelo.html` como base e preencher com a oferta.

## Entregável

`produtos/[slug]/4-pagina-vendas.html`. Atualize `maquina.db` (etapa `compradores`, `paginaArq`) e regenere o painel. Mostre a página ao usuário com present_files.
