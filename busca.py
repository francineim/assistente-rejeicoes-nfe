"""Motor de busca da base de conhecimento de rejeições de NF-e.

Lê o arquivo Markdown da base, divide em tópicos (um por título) e
responde consultas com ranking BM25, tolerância a erros de digitação
e prioridade para códigos de rejeição (ex.: "539", "rejeição 610").
"""

from __future__ import annotations

import difflib
import math
import re
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

STOPWORDS = set(
    """
    a o as os um uma uns umas de da do das dos dum duma em na no nas nos num numa
    por pela pelo pelas pelos para pra com sem sob sobre entre ate apos e ou mas
    que se nao sim ja ao aos à às eu tu ele ela nos voces eles elas meu minha
    seu sua seus suas esse essa este esta isso isto aquele aquela qual quais
    como quando onde porque por que qual o quê ser estar ter haver foi era sao
    esta estao tem ha vai fazer faco faz devo deve posso pode preciso precisa
    resolver resolvo resolve corrigir corrijo tratar trato problema problemas
    duvida ajuda erro erros mensagem rejeicao rejeicoes rejeitada rejeitado
    nota notas fiscal nfe nf apareceu aparece aparecendo deu dando estou
    meu minha gostaria saber quero queria tela sistema conexos o a me
    oi ola bom boa dia tarde noite obrigado obrigada valeu tudo bem
    """.split()
)

CODIGO_RE = re.compile(r"\b(\d{3,5})\b")


def normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto.lower())
    return "".join(c for c in texto if not unicodedata.combining(c))


def _radical(token: str) -> str:
    # Stemming leve: plurais e algumas terminações comuns em português.
    for suf in ("coes", "cao", "mente", "s"):
        if len(token) > len(suf) + 3 and token.endswith(suf):
            return token[: -len(suf)]
    return token


def tokenizar(texto: str, remover_stop: bool = True) -> list[str]:
    tokens = re.findall(r"[a-z0-9]+", normalizar(texto))
    if remover_stop:
        tokens = [t for t in tokens if t not in STOPWORDS]
    return [_radical(t) for t in tokens if len(t) > 1]


IMAGEM_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
IGNORAR_SECOES = {"índice", "indice"}
ROTULOS = r"Causa|Solução|Informações|Contexto|Mensagem apresentada"


@dataclass
class Topico:
    id: int
    titulo: str
    secao: str
    corpo: str
    fonte: str = ""
    codigos: set[str] = field(default_factory=set)
    imagens: dict[str, Path] = field(default_factory=dict)  # caminho no .md -> arquivo

    @property
    def causa(self) -> str | None:
        return _extrair_bloco(self.corpo, "Causa")

    @property
    def solucao(self) -> str | None:
        return _extrair_bloco(self.corpo, "Solução")

    @property
    def introducao(self) -> str:
        # Texto antes do primeiro bloco Causa/Solução (mensagem exibida, telas do erro).
        m = re.search(r"\*\*(Causa|Solução):?\*\*", self.corpo)
        return (self.corpo[: m.start()] if m else "").strip()

    @property
    def eh_erro(self) -> bool:
        return self.causa is not None or self.solucao is not None

    @property
    def titulo_limpo(self) -> str:
        t = re.sub(r"^\d+\.\s+", "", self.titulo)
        t = re.sub(r"^(Mensagem( de [Ee]rro)?|Erro referente|Erro|ERRO|Situação de erro|Mensagem apresentada \(ERRO\))\s*:\s*", "", t)
        return t.strip().strip('"')


def _extrair_bloco(corpo: str, rotulo: str) -> str | None:
    padrao = re.compile(
        rf"\*\*{rotulo}:?\*\*:?\s*(.*?)(?=\n\*\*({ROTULOS}):?\*\*|\Z)",
        re.S,
    )
    m = padrao.search(corpo)
    return m.group(1).strip() if m else None


def _resolver_imagem(ref: str, pasta_md: Path, raiz: Path) -> Path | None:
    caminho = pasta_md / ref
    if caminho.exists():
        return caminho
    # Upload pelo site do GitHub pode achatar pastas: procura pelo nome do arquivo.
    return next(raiz.rglob(Path(ref).name), None)


def carregar_topicos(caminho: Path, raiz: Path | None = None, inicio: int = 0) -> tuple[str, list[Topico]]:
    raiz = raiz or caminho.parent
    linhas = caminho.read_text(encoding="utf-8").splitlines()
    titulo_doc = "Base de conhecimento"
    topicos: list[Topico] = []
    secao_atual = ""
    titulo_atual: str | None = None
    buffer: list[str] = []

    def fechar():
        if titulo_atual is None or normalizar(titulo_atual) in IGNORAR_SECOES:
            return
        corpo = "\n".join(l for l in buffer if l.strip() != "---").strip()
        if not corpo:
            return
        imagens = {}
        for _, ref in IMAGEM_RE.findall(corpo):
            arquivo = _resolver_imagem(ref, caminho.parent, raiz)
            if arquivo:
                imagens[ref] = arquivo
        codigos = set(CODIGO_RE.findall(titulo_atual))
        topicos.append(
            Topico(inicio + len(topicos), titulo_atual, secao_atual, corpo, titulo_doc, codigos, imagens)
        )

    for linha in linhas:
        m = re.match(r"^(#{1,6})\s+(.*)$", linha)
        if m:
            nivel, texto = len(m.group(1)), m.group(2).strip()
            if nivel == 1:
                titulo_doc = texto
                continue
            fechar()
            buffer = []
            if nivel == 2:
                secao_atual = texto
            titulo_atual = texto
        elif titulo_atual is not None:
            buffer.append(linha)
    fechar()
    return titulo_doc, topicos


def carregar_bases(caminhos: list[Path], raiz: Path) -> tuple[list[str], list[Topico]]:
    titulos, topicos = [], []
    for caminho in caminhos:
        titulo, novos = carregar_topicos(caminho, raiz, inicio=len(topicos))
        titulos.append(titulo)
        topicos.extend(novos)
    return titulos, topicos


class MotorBusca:
    """BM25 sobre título (peso maior) + corpo, com correção de digitação."""

    K1, B, PESO_TITULO = 1.5, 0.75, 3

    def __init__(self, topicos: list[Topico]):
        self.topicos = topicos
        self.docs: list[Counter] = []
        for t in topicos:
            tokens = tokenizar(t.titulo) * self.PESO_TITULO + tokenizar(IMAGEM_RE.sub(r"\1", t.corpo))
            self.docs.append(Counter(tokens))
        self.tam_medio = sum(sum(d.values()) for d in self.docs) / max(len(self.docs), 1)
        df = Counter()
        for d in self.docs:
            df.update(d.keys())
        n = len(self.docs)
        self.idf = {t: math.log(1 + (n - f + 0.5) / (f + 0.5)) for t, f in df.items()}
        self.vocabulario = list(self.idf)

    def _expandir(self, tokens: list[str]) -> list[str]:
        saida = []
        for t in tokens:
            if t in self.idf or t.isdigit():
                saida.append(t)
            else:
                saida.extend(difflib.get_close_matches(t, self.vocabulario, n=2, cutoff=0.8))
        return saida

    def buscar(self, consulta: str, limite: int = 4) -> list[tuple[Topico, float]]:
        termos = self._expandir(tokenizar(consulta))
        codigos = set(CODIGO_RE.findall(consulta))
        pontuacoes = []
        for topico, doc in zip(self.topicos, self.docs):
            tam = sum(doc.values())
            score = 0.0
            for termo in termos:
                f = doc.get(termo, 0)
                if f:
                    idf = self.idf[termo]
                    score += idf * f * (self.K1 + 1) / (f + self.K1 * (1 - self.B + self.B * tam / self.tam_medio))
            if codigos & topico.codigos:
                score += 50  # código de rejeição exato vence qualquer outro critério
            if score > 0:
                pontuacoes.append((topico, score))
        pontuacoes.sort(key=lambda x: x[1], reverse=True)
        return pontuacoes[:limite]
