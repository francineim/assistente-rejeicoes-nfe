"""Assistente de Faturamento — chat de consulta às bases de conhecimento (NF-e e ODF)."""

from __future__ import annotations

import base64
import json
import urllib.error
import urllib.request
from html import escape
from pathlib import Path

import streamlit as st

from busca import IMAGEM_RE, MotorBusca, carregar_bases

PASTA = Path(__file__).parent
SCORE_MINIMO = 4.5      # abaixo disso consideramos que não há resposta na base
SCORE_CONFIANTE = 8.0   # acima disso a resposta principal é exibida como "encontrada"
TITULO_APP = "Assistente Dúvidas Faturamento"

# Validações criadas pelo app ficam numa base própria, ao lado das demais.
ARQUIVO_VALIDACOES = (PASTA / "data" if (PASTA / "data").is_dir() else PASTA) / "Validacoes_Cadastradas.md"
CABECALHO_VALIDACOES = "# Validações cadastradas\n\n## Validações cadastradas pela equipe\n"

st.set_page_config(
    page_title=TITULO_APP,
    page_icon="🧾",
    layout="centered",
    initial_sidebar_state="expanded",
)


def localizar_bases() -> list[Path]:
    # Todas as bases .md em data/ e, se houver, na raiz do repositório (comum quando
    # o upload pelo site do GitHub não preserva a pasta). Cada arquivo entra uma vez.
    vistos, bases = set(), []
    for caminho in sorted(PASTA.glob("data/*.md")) + sorted(PASTA.glob("*.md")):
        if caminho.name.lower() != "readme.md" and caminho.name not in vistos:
            vistos.add(caminho.name)
            bases.append(caminho)
    return bases


@st.cache_resource
def carregar_motor(caminhos: tuple[Path, ...]):
    titulos, topicos = carregar_bases(list(caminhos), PASTA)
    return titulos, topicos, MotorBusca(topicos)


BASES = localizar_bases()
if not BASES:
    st.error("Nenhuma base de conhecimento encontrada. Envie os arquivos `.md` para a pasta `data/` do repositório.")
    st.stop()

TITULOS_BASES, TOPICOS, MOTOR = carregar_motor(tuple(BASES))


# ---------------------------------------------------------------- novas validações
def segredo(nome: str, padrao=None):
    try:
        return st.secrets.get(nome, padrao)
    except Exception:  # sem secrets.toml (execução local)
        return padrao


def montar_validacao(duvida: str, causa: str, tratativa: str) -> str:
    def limpar(texto: str) -> str:
        # Linha começando com "#" viraria um novo tópico na base: escapa.
        return "\n".join("\\" + l.lstrip() if l.lstrip().startswith("#") else l for l in texto.strip().splitlines())

    bloco = f"\n#### {' '.join(duvida.split())}\n\n"
    if causa.strip():
        bloco += f"**Causa:** {limpar(causa)}\n\n"
    return bloco + f"**Solução:** {limpar(tratativa)}\n"


def _github(metodo: str, url: str, token: str, dados: dict | None = None) -> dict:
    req = urllib.request.Request(
        url,
        method=metodo,
        data=json.dumps(dados).encode() if dados else None,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.load(resp)


def salvar_validacao(duvida: str, causa: str, tratativa: str) -> bool:
    """Acrescenta a validação na base. Retorna True se também foi gravada no GitHub."""
    bloco = montar_validacao(duvida, causa, tratativa)
    token = segredo("GITHUB_TOKEN")
    if token:
        # O GitHub é a fonte da verdade: o disco do Streamlit Cloud é apagado a cada reinício.
        repo = segredo("GITHUB_REPO", "francineim/assistente-rejeicoes-nfe")
        ramo = segredo("GITHUB_BRANCH", "main")
        url = f"https://api.github.com/repos/{repo}/contents/{ARQUIVO_VALIDACOES.relative_to(PASTA).as_posix()}"
        try:
            atual = _github("GET", f"{url}?ref={ramo}", token)
            conteudo, sha = base64.b64decode(atual["content"]).decode("utf-8"), atual["sha"]
        except urllib.error.HTTPError as e:
            if e.code != 404:
                raise
            conteudo, sha = CABECALHO_VALIDACOES, None
        novo = conteudo.rstrip("\n") + "\n" + bloco
        dados = {
            "message": f"Nova validação: {duvida.strip()[:60]}",
            "content": base64.b64encode(novo.encode("utf-8")).decode(),
            "branch": ramo,
        }
        if sha:
            dados["sha"] = sha
        _github("PUT", url, token, dados)
    else:
        conteudo = ARQUIVO_VALIDACOES.read_text(encoding="utf-8") if ARQUIVO_VALIDACOES.exists() else CABECALHO_VALIDACOES
        novo = conteudo.rstrip("\n") + "\n" + bloco
    ARQUIVO_VALIDACOES.write_text(novo, encoding="utf-8")
    return bool(token)


@st.dialog("Criar nova validação", width="large")
def dialogo_nova_validacao():
    with st.form("form_validacao", border=False):
        duvida = st.text_input("Dúvida / mensagem de erro *", placeholder="Ex.: Rejeição 999 — Campo X inválido")
        causa = st.text_area("Causa (opcional)", placeholder="Por que o problema acontece")
        tratativa = st.text_area("Tratativa *", height=200, placeholder="Passo a passo para resolver")
        enviar = st.form_submit_button("Salvar validação", type="primary", use_container_width=True)
    if not enviar:
        return
    if not duvida.strip() or not tratativa.strip():
        st.error("Preencha a dúvida e a tratativa.")
        return
    try:
        no_github = salvar_validacao(duvida, causa, tratativa)
    except Exception as e:
        st.error(f"Não foi possível salvar a validação: {e}")
        return
    carregar_motor.clear()
    st.session_state.aviso = (
        "Validação salva e já disponível na pesquisa."
        if no_github
        else "Validação salva neste servidor. Configure o GITHUB_TOKEN para mantê-la após reinícios."
    )
    st.rerun()

# ---------------------------------------------------------------- estilo
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"], .stMarkdown, .stChatInput textarea { font-family: 'Inter', sans-serif; }
#MainMenu, footer { visibility: hidden; }
.block-container { padding-top: 3.5rem; max-width: 820px; }

.hero {
  background: linear-gradient(135deg, #0B2545 0%, #13315C 55%, #1F6FEB 100%);
  border-radius: 16px; padding: 28px 30px; color: #fff; margin-bottom: 1.4rem;
  box-shadow: 0 8px 24px rgba(11, 37, 69, .18);
}
.hero h1 { font-size: 1.65rem; font-weight: 700; margin: 0 0 .35rem 0; color: #fff; }
.hero p  { margin: 0; opacity: .85; font-size: .98rem; }
.hero .tag {
  display: inline-block; background: rgba(255,255,255,.14); border: 1px solid rgba(255,255,255,.25);
  border-radius: 999px; padding: 3px 12px; font-size: .75rem; letter-spacing: .04em;
  text-transform: uppercase; margin-bottom: .8rem;
}
.titulo-resp { font-size: 1.08rem; font-weight: 600; margin: .1rem 0 .6rem 0; }
.rotulo { font-size: .78rem; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; margin-bottom: .2rem; }
.rotulo.causa   { color: #B45309; }
.rotulo.solucao { color: #047857; }
.rotulo.info    { color: #1F6FEB; }
.fonte { font-size: .78rem; color: #6B7280; margin-top: .4rem; }
.vazio { text-align: center; color: #0B2545; margin: 2rem 0 1rem 0; font-size: 1.25rem; font-weight: 600; }
[data-testid="stSidebar"] { background: #F5F7FB; }
@media (prefers-color-scheme: dark) { [data-testid="stSidebar"] { background: inherit; } }
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- estado
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []
if aviso := st.session_state.pop("aviso", None):
    st.toast(aviso, icon="✅")

# ---------------------------------------------------------------- sidebar
with st.sidebar:
    st.markdown(f"### 🧾 {TITULO_APP}")
    st.divider()
    if st.button("➕  Criar Nova Validação", type="primary", use_container_width=True):
        dialogo_nova_validacao()
    st.divider()
    st.markdown("**💡 Dicas de pesquisa**")
    st.markdown(
        "- Informe o **código da rejeição** (ex.: `610`)\n"
        "- Ou cole a **mensagem de erro** exibida\n"
        "- Ou descreva o problema com suas palavras"
    )
    st.divider()
    if st.button("🗑️  Limpar conversa", use_container_width=True):
        st.session_state.mensagens = []
        st.rerun()
    st.caption("Bases: " + " · ".join(TITULOS_BASES))

# ---------------------------------------------------------------- render
def render_texto(texto: str, topico):
    """Exibe o markdown do tópico, trocando as referências de imagem pelas telas."""
    pos = 0
    for m in IMAGEM_RE.finditer(texto):
        if texto[pos : m.start()].strip():
            st.markdown(texto[pos : m.start()])
        arquivo = topico.imagens.get(m.group(2))
        if arquivo:
            st.image(str(arquivo), caption=m.group(1) or None)
        pos = m.end()
    if texto[pos:].strip():
        st.markdown(texto[pos:])


def render_topico(topico, destaque: bool):
    if destaque:
        st.markdown(f'<div class="titulo-resp">{escape(topico.titulo_limpo)}</div>', unsafe_allow_html=True)
    causa, solucao = topico.causa, topico.solucao
    if causa or solucao:
        if topico.introducao:
            render_texto(topico.introducao, topico)
        if causa:
            st.markdown('<div class="rotulo causa">⚠ Causa</div>', unsafe_allow_html=True)
            render_texto(causa, topico)
        if solucao:
            st.markdown('<div class="rotulo solucao">✔ Como resolver</div>', unsafe_allow_html=True)
            render_texto(solucao, topico)
    else:
        st.markdown('<div class="rotulo info">ℹ Orientação</div>', unsafe_allow_html=True)
        render_texto(topico.corpo, topico)
    secao = "" if topico.secao == topico.titulo else f" › {escape(topico.secao)}"
    st.markdown(f'<div class="fonte">Fonte: {escape(topico.fonte)}{secao}</div>', unsafe_allow_html=True)


def render_resposta(msg):
    resultados = [(TOPICOS[i], s) for i, s in msg["resultados"]]
    if not resultados or resultados[0][1] < SCORE_MINIMO:
        st.markdown(
            "Não encontrei esse problema na base de conhecimento. 🤔\n\n"
            "Tente informar o **código da rejeição** retornado pela SEFAZ ou "
            "copiar o **texto exato da mensagem de erro**."
        )
        return
    principal, score = resultados[0]
    if score >= SCORE_CONFIANTE:
        st.markdown("Encontrei a orientação para esse problema:")
    else:
        st.markdown("Este é o tópico mais próximo do que você descreveu:")
    with st.container(border=True):
        render_topico(principal, destaque=True)
    relacionados = [(t, s) for t, s in resultados[1:] if s >= SCORE_MINIMO]
    if relacionados:
        st.markdown("**Tópicos relacionados**")
        for t, _ in relacionados:
            with st.expander(t.titulo_limpo):
                render_topico(t, destaque=False)


# ---------------------------------------------------------------- layout
st.markdown(
    """
<div class="hero">
  <h1>Assistente Dúvidas Faturamento</h1>
  <p>Descreva a sua dúvida ou rejeição.</p>
</div>
""",
    unsafe_allow_html=True,
)

pergunta = st.chat_input("Digite sua dúvida...")  # fica fixo no rodapé, onde quer que seja chamado

if not st.session_state.mensagens and not pergunta:
    st.markdown('<div class="vazio">Olá, faça a sua pergunta!</div>', unsafe_allow_html=True)

for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"], avatar="🧑‍💼" if msg["role"] == "user" else "🧾"):
        if msg["role"] == "user":
            st.markdown(msg["content"])
        else:
            render_resposta(msg)


if pergunta:
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    with st.chat_message("user", avatar="🧑‍💼"):
        st.markdown(pergunta)
    with st.chat_message("assistant", avatar="🧾"):
        with st.spinner("Pesquisando na base de conhecimento..."):
            resultados = [(t.id, s) for t, s in MOTOR.buscar(pergunta)]
        resposta = {"role": "assistant", "resultados": resultados}
        render_resposta(resposta)
    st.session_state.mensagens.append(resposta)
