---
name: painel-produtos
description: Esta skill deve ser usada para criar e ATUALIZAR o painel local da Máquina de Produtos Digitais — o dashboard (SQLite + página web) que mostra cada produto na esteira dos 7 passos com link para os entregáveis. Acione sempre que um comando mudar dados de um projeto (/problema, /promessa, /produto, /pagina, /compradores, /lancamento, /validacao, /maquina) ou quando o usuário disser "painel", "dashboard", "meus produtos", "esteira" ou rodar /painel ou /setup.
---

# Painel de produtos (SQLite + página local)

Arquitetura na RAIZ da pasta conectada:

- **`maquina.db`** — banco SQLite, a FONTE DA VERDADE dos projetos.
- **`painel-server.py` + `iniciar-painel.bat` (Windows) / `iniciar-painel.command` (Mac)** — mini-servidor local (Python padrão, sem dependências). Duplo clique → abre `http://localhost:8767`: editar e arrastar cards entre etapas salva direto no banco.
- **`painel.html`** — a página do painel (gerada do template). Servida pelo servidor (modo banco) ou aberta por duplo clique (modo arquivo: leitura). O badge no topo indica o modo.
- **`produtos/[slug]/`** — pasta de cada projeto com os 7 entregáveis (`1-...md` … `7-...md`/`4-pagina-vendas.html`).

## Setup (uma vez, no /setup ou primeiro uso)

1. Copie `references/painel-server.py`, `references/iniciar-painel.bat` e `references/iniciar-painel.command` desta skill para a raiz da pasta conectada.
2. Crie o `maquina.db` com o schema abaixo (via python3/sqlite3 no bash).
3. Gere o `painel.html` de `references/painel-template.html` trocando `__DADOS__` pelo snapshot JSON.
4. Diga em uma linha: "duplo clique em `iniciar-painel.bat` (ou `.command` no Mac) abre o painel vivo — precisa de Python; sem Python, abra `painel.html` (modo leitura)."

## Schema do banco

```sql
CREATE TABLE IF NOT EXISTS projetos(
  slug TEXT PRIMARY KEY, titulo TEXT, habilidade TEXT, publico TEXT,
  etapa TEXT DEFAULT 'problema',
  problema TEXT, promessa TEXT, produto TEXT,
  paginaArq TEXT, compradores TEXT, lancamento TEXT, validacao TEXT,
  formato TEXT, preco REAL,
  criadoEm TEXT DEFAULT (datetime('now','localtime')),
  atualizado TEXT DEFAULT (datetime('now','localtime')));
```

Etapas (ordem da esteira): `problema → promessa → produto → pagina → compradores → lancamento → validacao → validado`. `slug` é a chave.

## Como os comandos atualizam (SEMPRE os 2 passos)

1. **Upsert no banco** via bash:
```bash
python3 - <<'EOF'
import sqlite3
c = sqlite3.connect('CAMINHO/maquina.db')
c.execute("""INSERT INTO projetos (slug,titulo,etapa) VALUES (?,?,?)
             ON CONFLICT(slug) DO UPDATE SET etapa=excluded.etapa, atualizado=datetime('now','localtime')""",
          ('meu-produto','Nome do produto','promessa'))
c.commit()
EOF
```
   - `/problema` → cria o projeto (`etapa='promessa'`, `problema`, `publico`, `habilidade`). NUNCA rebaixe a etapa de um projeto que já avançou.
   - `/promessa` → `etapa='produto'`, `promessa`, `titulo`, `formato`, `preco`.
   - `/produto` → `etapa='pagina'`, `produto`.
   - `/pagina` → `etapa='compradores'`, `paginaArq`.
   - `/compradores` → `etapa='lancamento'`, `compradores`.
   - `/lancamento` → `etapa='validacao'`, `lancamento`.
   - `/validacao` → `etapa='validado'` (ou mantém), `validacao`.
2. **Regenerar o snapshot**: leia todos os projetos e regrave `painel.html` do template com o JSON embutido (`{"atualizado":"...","projetos":[...]}`) — é o fallback pra quem abre sem servidor. Antes de regravar um projeto, leia o registro atual pra respeitar edições do usuário.

Se o banco não existir (usuário antigo), crie-o e importe o snapshot embutido no `painel.html` atual antes do upsert.

## O que o painel faz sozinho (não reimplementar)

Esteira kanban com as 7 colunas + coluna "validado", drag & drop entre etapas, card por produto com título/formato/preço/público e links pra cada entregável em `produtos/[slug]/`, badge do veredito de validação, busca e contadores. O plugin só mantém o BANCO correto e o snapshot em dia.
