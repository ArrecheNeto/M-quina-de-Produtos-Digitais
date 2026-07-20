---
description: Abre e atualiza o painel local com todos os seus produtos e o estágio de cada um
argument-hint: "sem argumentos"
---

Abra o painel de produtos seguindo a skill `painel-produtos`.

## Ação

1. Se o `maquina.db` ou os arquivos do painel não existirem na pasta conectada, instale-os agora (copie de `references/` e crie o banco — ver skill `painel-produtos`).
2. Leia todos os projetos do `maquina.db` e regenere o `painel.html` do template com o snapshot JSON atualizado.
3. Abra o `painel.html` para o usuário (via present_files) e explique em uma linha: "duplo clique em `iniciar-painel.bat`/`iniciar-painel.command` abre a versão viva (edita e arrasta os cards); o `painel.html` sozinho é a versão leitura."

O painel mostra cada produto como um card na esteira (Problema → Promessa → Produto → Página → Compradores → Lançamento → Validação), com link para cada entregável e o veredito final quando houver.
