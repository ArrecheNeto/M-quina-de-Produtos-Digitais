# Máquina de Produtos Digitais

Uma esteira que transforma **o que você já sabe** num produto digital pronto pra vender — sem API, sem custo extra, rodando na sua própria assinatura do Claude.

São **7 passos, 7 entregáveis**:

1. **/problema** — pesquisa as dores reais do mercado e escolhe o problema-alvo
2. **/promessa** — vira o problema numa promessa vencedora + oferta irresistível
3. **/produto** — monta o produto mínimo (o que basta pra vender, não o curso inteiro)
4. **/pagina** — gera a página de vendas pronta (HTML)
5. **/compradores** — mapeia 10 lugares onde o comprador está, com abordagem
6. **/lancamento** — cria o plano de lançamento inicial (sem ads, sem audiência grande)
7. **/validacao** — analisa os resultados e dá o veredito (validar, ajustar ou descartar)

Tudo é administrado num **painel local** (esteira kanban) que mostra cada produto e o estágio dele, com link para cada entregável.

## Começando

1. **/setup** — 2 minutos, uma vez só. Configura seu nome, sua habilidade e instala o painel.
2. **/maquina [tema]** — roda a esteira inteira, parando pra confirmar com você nos pontos de decisão.

Prefere passo a passo? Rode um comando por vez: `/problema` → `/promessa` → … → `/validacao`.

## Como funciona por dentro

- **Sem API e sem chave.** A pesquisa usa a busca web e o navegador do próprio Claude; o resto é geração. Nada de configurar serviços externos.
- **Seus arquivos ficam com você.** Cada produto vira uma pasta `produtos/[slug]/` na sua pasta conectada, com os 7 entregáveis em Markdown e HTML.
- **Painel local.** `maquina.db` (SQLite) é a fonte da verdade; `iniciar-painel.bat` (Windows) / `iniciar-painel.command` (Mac) abre a versão viva em http://localhost:8767. Sem Python, abra `painel.html` no modo leitura.

## Comandos

| Comando | O que faz |
|---|---|
| `/setup` | Configura tudo e instala o painel (uma vez) |
| `/maquina` | Roda a esteira completa dos 7 passos |
| `/problema` | Passo 1 — pesquisa de dores |
| `/promessa` | Passo 2 — promessa e oferta |
| `/produto` | Passo 3 — produto mínimo |
| `/pagina` | Passo 4 — página de vendas |
| `/compradores` | Passo 5 — onde/pra quem vender |
| `/lancamento` | Passo 6 — lançamento inicial |
| `/validacao` | Passo 7 — veredito de validação |
| `/painel` | Abre e atualiza o painel |

---

Feito por **Helio Arreche**. Plugin gratuito.
