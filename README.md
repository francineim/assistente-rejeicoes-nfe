# Assistente de Rejeições de NF-e

Chat em Streamlit que consulta a base de conhecimento **COM_319 — Geração Automática de NF-e**
e devolve a causa e a solução para rejeições da SEFAZ e erros de transmissão no ERP.

## Estrutura

```
app.py                  # interface (chat)
busca.py                # leitura da base + motor de busca (BM25, sem dependências externas)
data/COM_319_Geracao_Automatica_NFe.md   # base de conhecimento
requirements.txt
.streamlit/config.toml  # tema visual
```

Para atualizar a base, basta substituir/editar o arquivo `.md` em `data/` mantendo o padrão:
um título `####` por erro, com os blocos `**Causa:**` e `**Solução:**`.

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
