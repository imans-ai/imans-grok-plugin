# Imans para Grok Bot

Plugin mantido pela Imans para usar **toda a superfície do MCP Imans** no Grok
Bot: dados de negócio, integrações e ações permitidas pela sua conexão.

## Conectar

Você precisa de uma conta no Grok Bot e acesso a um workspace Imans.
Em **Connect apps**, adicione Imans quando a listagem estiver disponível.
Antes da listagem, peça ao Bot para adicionar o MCP customizado:

```text
https://mcp.imans.ai/mcp
```

Conclua o login na tela OAuth do Imans e selecione workspaces, permissões e modo
da conexão. Uma conexão Imans já funcional pode continuar sendo usada. O pacote
acrescenta uma skill que orienta o Bot a descobrir as capacidades atuais.

## Usar

- “Resuma as vendas do mês passado por canal e explique os indicadores.”
- “Consulte este SKU, o estoque e a data de atualização.”
- “Descubra quais dados financeiros posso consultar.”
- “Crie uma tarefa para investigar essa divergência.”
- “Prepare um rascunho de processo e mostre os problemas de validação.”
- “Pré-visualize esta publicação de preços e mostre o link de aprovação.”
- “Exporte o resultado completo desta consulta.”

O plugin não aplica uma lista fixa de ferramentas. Tudo que o servidor expuser
à conexão fica disponível conforme consentimento, papel, módulos, integrações e
operações suportadas. Isso inclui as ações já existentes no MCP. Instalar o
plugin não amplia permissões nem converte uma conexão de leitura em escrita.

As aprovações exigidas pelo Imans continuam no Imans. Publicações de preços
dependem da aprovação do lote exato; “pendente”, “enviado” e “verificado” são
estados diferentes. Confira qual conta está conectada ao usar Bots compartilhados.

A instalação é gratuita. É necessário acesso ao serviço Imans; operações
aplicáveis podem consumir Usage Credits. O pacote não contém segredos, servidor
local ou telemetria própria. Os resultados solicitados são devolvidos ao Grok
Bot pelo MCP remoto. Consulte a [política de privacidade](https://imans.ai/privacy-policy)
e os termos da plataforma apresentados no Imans.

Para problemas na integração, use as
[issues](https://github.com/imans-ai/imans-grok-plugin/issues), sem dados de
clientes ou credenciais. Para ajuda com sua conta, use o suporte no
[Imans](https://app.imans.ai). Detalhes de empacotamento, desenvolvimento e
limitações de homologação estão no [README em inglês](README.md).
