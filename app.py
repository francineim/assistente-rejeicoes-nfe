"""Assistente de Faturamento — chat de consulta às bases de conhecimento (NF-e e ODF)."""

from __future__ import annotations

from html import escape
from pathlib import Path

import streamlit as st

from busca import IMAGEM_RE, MotorBusca, carregar_bases

PASTA = Path(__file__).parent
SCORE_MINIMO = 4.5      # abaixo disso consideramos que não há resposta na base
SCORE_CONFIANTE = 8.0   # acima disso a resposta principal é exibida como "encontrada"

EXEMPLOS = [
    "Rejeição 539 duplicidade de NF-e",
    "Nota travada em aguardando retorno",
    "Certificado digital vencido",
    "Total da NF difere do somatório dos itens",
    "Nenhum item com saldo para gerar a ODF",
    "Falta o tipo de operação no processo",
]

st.set_page_config(
    page_title="Assistente de Faturamento",
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
.vazio { text-align: center; color: #6B7280; margin: 1.2rem 0 .8rem 0; font-size: .95rem; }
[data-testid="stSidebar"] { background: #F5F7FB; }
@media (prefers-color-scheme: dark) { [data-testid="stSidebar"] { background: inherit; } }
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- estado
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []
if "pendente" not in st.session_state:
    st.session_state.pendente = None


def perguntar(texto: str):
    st.session_state.pendente = texto


# ---------------------------------------------------------------- sidebar
with st.sidebar:
    st.markdown("### 🧾 Assistente de Faturamento")
    st.caption("Rejeições de NF-e e erros na geração de Ordem de Faturamento (ODF) no ERP.")
    erros = sum(t.eh_erro for t in TOPICOS)
    c1, c2 = st.columns(2)
    c1.metric("Erros", erros)
    c2.metric("Tópicos", len(TOPICOS))
    st.divider()
    st.markdown("**Dicas de pesquisa**")
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
  <span class="tag">Faturamento · NF-e · Ordem de Faturamento</span>
  <h1>Assistente de Faturamento</h1>
  <p>Descreva a rejeição da SEFAZ ou o erro na geração da ODF e veja a causa e o passo a passo para resolver.</p>
</div>
""",
    unsafe_allow_html=True,
)

if not st.session_state.mensagens and not st.session_state.pendente:
    st.markdown('<div class="vazio">Comece com uma pergunta ou escolha um exemplo:</div>', unsafe_allow_html=True)
    cols = st.columns(2)
    for i, ex in enumerate(EXEMPLOS):
        cols[i % 2].button(ex, key=f"ex{i}", on_click=perguntar, args=(ex,), use_container_width=True)

for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"], avatar="🧑‍💼" if msg["role"] == "user" else "🧾"):
        if msg["role"] == "user":
            st.markdown(msg["content"])
        else:
            render_resposta(msg)

pergunta = st.chat_input("Ex.: Rejeição 610 ou \"falta o tipo de operação no processo\"")
if st.session_state.pendente:
    pergunta, st.session_state.pendente = st.session_state.pendente, None

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
