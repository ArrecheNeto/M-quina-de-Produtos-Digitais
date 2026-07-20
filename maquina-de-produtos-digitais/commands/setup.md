---
description: Configura o plugin (2 min, uma vez só) — seus dados, sua habilidade e instala o painel local
argument-hint: "sem argumentos — é uma conversa guiada"
---

Configure a Máquina de Produtos Digitais. Rode isto UMA vez, no começo.

## O que perguntar (uma pergunta por vez, curto)

1. **Seu nome / marca** — como assinar as páginas e materiais.
2. **O que você já sabe fazer** — a habilidade, profissão ou tema que vira produto (ex.: "edito vídeo", "sei tráfego pago", "sou nutricionista", "programo em Python"). Pode listar várias.
3. **Quem você quer ajudar** — o público que você imagina (opcional; a esteira também descobre isso sozinha).
4. **Tom de voz** — como você fala com seu público (ex.: direto e sem enrolação / acolhedor / técnico). Isso guia a copy das páginas e materiais.

Se o usuário não souber responder alguma, use um padrão razoável e siga — nunca trave o setup.

## Salvar a configuração

Grave `maquina-config.json` na RAIZ da pasta conectada:

```json
{
  "autor": { "nome": "", "marca": "", "tom": "direto e prático" },
  "habilidades": ["..."],
  "publicoImaginado": "",
  "moeda": "BRL"
}
```

## Instalar o painel local

Siga a skill `painel-produtos` para:

1. Copiar `references/painel-server.py`, `references/iniciar-painel.bat` e `references/iniciar-painel.command` desta skill para a raiz da pasta conectada.
2. Criar o banco `maquina.db` (schema na skill) se ainda não existir.
3. Gerar o `painel.html` inicial (vazio) a partir do template.
4. Explicar em UMA linha: "duplo clique em `iniciar-painel.bat` (Windows) ou `iniciar-painel.command` (Mac) abre seu painel em http://localhost:8767 — precisa de Python instalado; sem Python, dá pra abrir o `painel.html` direto (modo leitura)."

## Encerramento

Confirme que está pronto e mostre o próximo passo:

> Tudo configurado. Agora rode **/maquina** para montar seu primeiro produto do zero, ou chame um passo isolado: **/problema** para começar pela pesquisa de dores.
