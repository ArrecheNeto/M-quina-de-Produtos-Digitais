---
description: Passo 4 — gera a página de vendas pronta (HTML) a partir da oferta e do produto
argument-hint: "[slug do projeto] — opcional, usa o projeto na etapa pagina"
---

Execute o **Passo 4 da esteira** seguindo a skill `pagina-vendas`.

## Preparação

1. Identifique o projeto (slug em `$ARGUMENTS` ou o mais recente na etapa `pagina`).
2. Leia `1-pesquisa-problemas.md`, `2-promessa-oferta.md`, `3-produto-minimo.md` e o `maquina-config.json` (para o tom de voz e o nome/marca).

## Execução

Siga a skill `pagina-vendas` para escrever a copy E o HTML da página, num arquivo único, autossuficiente (CSS embutido, sem dependências externas). A página segue a estrutura de conversão: promessa acima da dobra → dor (com as falas reais) → virada → o que é o produto → o que está incluso + bônus → prova/autoridade → oferta e preço → garantia → FAQ (quebra de objeções) → CTA repetido. Use placeholders claros onde faltar dado do usuário (ex.: `[SEU DEPOIMENTO AQUI]`, `[LINK DE PAGAMENTO]`).

## Saída

1. Grave `produtos/[slug]/4-pagina-vendas.html` — pronta pra abrir no navegador e publicar em qualquer lugar.
2. Atualize `maquina.db` (`etapa='compradores'`, `paginaArq`=caminho do arquivo) e regenere `painel.html`.
3. Abra/ mostre a página ao usuário (via present_files) e sugira: **/compradores** para descobrir onde estão os 10 primeiros que compram.
