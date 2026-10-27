# Assistente de Faturamento

Chat em Streamlit que consulta as bases de conhecimento do ERP e devolve a causa e a solução para:

- rejeições da SEFAZ e erros de transmissão (**COM_319 — Geração Automática de NF-e**);
- erros na **geração de Ordem de Faturamento (ODF)**, com as telas de cada erro.

## Estrutura

```
app.py                  # interface (chat)
busca.py                # leitura da base + motor de busca (BM25, sem dependências externas)
data/*.md              # bases de conhecimento (todas são carregadas)
data/imagens/          # telas referenciadas nas bases
requirements.txt
.streamlit/config.toml  # tema visual
```

Para incluir uma nova base, basta colocar outro arquivo `.md` em `data/` seguindo o padrão:
um título (`##` a `####`) por erro, com os blocos `**Causa:**` e `**Solução:**`.
Imagens entram com `![legenda](imagens/arquivo.png)` e o arquivo vai em `data/imagens/`.

## Rodar localmente

```bash
pip install -r requirements.txt
```

```bash
streamlit run app.py
```

## Publicar na nuvem (Streamlit Community Cloud — gratuito)

1. Crie um repositório no GitHub e envie estes arquivos (incluindo a pasta `data/` e `.streamlit/`).
2. Acesse https://share.streamlit.io e entre com sua conta GitHub.
3. Clique em **Create app** → **Deploy a public app from GitHub**.
4. Selecione o repositório, a branch `main` e o arquivo principal `app.py`.
5. Clique em **Deploy**. Em ~1 minuto o app estará em `https://<nome>.streamlit.app`.

Para restringir o acesso a pessoas da empresa, em **Settings → Sharing** do app,
marque o app como privado e convide os e-mails autorizados.

## Cadastro de novas validações

O botão **➕ Criar Nova Validação** (barra lateral) abre um formulário com dúvida, causa e
tratativa. As validações são gravadas em `Validacoes_Cadastradas.md` e entram na pesquisa na hora.

## Importação de documentos

O botão **📥 Importar Documentos** aceita PDF (ex.: Notas Técnicas), CSV, JSON, Markdown e TXT.
Cada arquivo vira uma base `Base_<nome>.md` (conversão em `importador.py`):

- **CSV/JSON**: uma linha/registro por tópico; colunas `pergunta`, `causa` e `resposta`
  (também `dúvida`, `erro`, `código`, `solução`, `tratativa`). Demais colunas aparecem como informação adicional.
- **PDF/TXT**: dividido pelos títulos numerados (`1.`, `2.1`...) ou em trechos de ~300 palavras.
  PDFs digitalizados (imagem) não têm texto e não podem ser importados.

## Persistência

Como o disco do Streamlit Cloud é apagado a cada reinício, configure em
**Manage app → Settings → Secrets** para que o app grave o arquivo direto no GitHub:

```toml
GITHUB_TOKEN = "github_pat_..."   # token com permissão Contents: Read and write neste repositório
```
