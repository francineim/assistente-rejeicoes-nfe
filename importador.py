"""Converte documentos importados (PDF, JSON, CSV, Markdown, TXT) em bases .md.

Cada arquivo vira uma base no mesmo padrão das demais: um título `####` por
tópico. Registros de CSV/JSON com colunas de pergunta/causa/resposta viram
blocos **Causa:**/**Solução:**; textos corridos (ex.: Notas Técnicas em PDF)
são divididos pelos títulos numerados ou em trechos de tamanho fixo.
"""

from __future__ import annotations

import csv
import io
import json
import re
from pathlib import Path

from busca import normalizar

FORMATOS = ["pdf", "json", "csv", "md", "txt"]
PALAVRAS_POR_TOPICO = 300

CAMPOS_TITULO = ["pergunta", "duvida", "titulo", "title", "question", "erro", "mensagem",
                 "problema", "assunto", "rejeicao", "descricao"]
CAMPOS_SOLUCAO = ["resposta", "solucao", "tratativa", "orientacao", "procedimento",
                  "como resolver", "answer", "solution"]
CAMPOS_CAUSA = ["causa", "motivo", "cause"]
CAMPOS_CODIGO = ["codigo", "cod", "code", "cstat"]
# O app é usado por vários clientes: colunas que identificam o cliente nunca entram na base.
CAMPOS_OCULTOS = {"cliente", "clientes", "nome do cliente", "razao social", "empresa", "customer", "client"}

# Títulos numerados de Notas Técnicas: "2.1 Regras de validação", "539 Rejeição: ..."
CABECALHO_RE = re.compile(r"^\d+(\.\d+)*\.?\s+\S.{2,90}$")


def escapar_markdown(texto: str) -> str:
    # Linha começando com "#" viraria um novo tópico na base: escapa.
    return "\n".join("\\" + l.lstrip() if l.lstrip().startswith("#") else l for l in texto.strip().splitlines())


def nome_base(titulo: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", normalizar(titulo)).strip("_")
    slug = re.sub(r"^base_", "", slug) or "documento"
    return f"Base_{slug}.md"


def _decodificar(dados: bytes) -> str:
    try:
        return dados.decode("utf-8-sig")
    except UnicodeDecodeError:
        return dados.decode("cp1252", errors="replace")  # padrão do Excel em português


def _linha(texto: str, limite: int = 150) -> str:
    return " ".join(texto.split())[:limite]


# ---------------------------------------------------------------- texto corrido
def _fatiar(linhas: list[str], limite: int) -> list[list[str]]:
    """Agrupa linhas em blocos de ~limite palavras, cortando preferencialmente no fim de frase."""
    blocos, atual, palavras = [], [], 0
    for linha in linhas:
        atual.append(linha)
        palavras += len(linha.split())
        fim_frase = not linha.strip() or linha.rstrip().endswith((".", ":", ";"))
        if (palavras >= limite and fim_frase) or palavras >= limite * 2:
            blocos.append(atual)
            atual, palavras = [], 0
    if any(l.strip() for l in atual):
        blocos.append(atual)
    return blocos


def texto_para_topicos(texto: str) -> list[tuple[str, str]]:
    linhas = [l.rstrip() for l in texto.splitlines()]
    cabecalhos = [
        i for i, l in enumerate(linhas)
        if CABECALHO_RE.match(l.strip()) and not l.rstrip().endswith((",", ";"))
    ]
    if len(cabecalhos) < 3:
        # Sem estrutura reconhecível: trechos de tamanho fixo, titulados pela primeira linha.
        return [
            (_linha(next(l for l in bloco if l.strip()), 90), "\n".join(bloco))
            for bloco in _fatiar(linhas, PALAVRAS_POR_TOPICO)
        ]
    secoes = [("Introdução", linhas[: cabecalhos[0]])]
    secoes += [(linhas[a].strip(), linhas[a + 1 : b]) for a, b in zip(cabecalhos, cabecalhos[1:] + [len(linhas)])]
    topicos = []
    for titulo, corpo in secoes:
        blocos = _fatiar(corpo, PALAVRAS_POR_TOPICO * 2)
        for n, bloco in enumerate(blocos, 1):
            topicos.append((titulo if len(blocos) == 1 else f"{titulo} (parte {n})", "\n".join(bloco)))
    return topicos


# ---------------------------------------------------------------- registros (CSV/JSON)
def _chave(nome: str) -> str:
    return normalizar(nome).strip().replace("_", " ")


def _campo(registro: dict, nomes: list[str]) -> str | None:
    # Nome exato primeiro; depois prefixo ("Solução proposta pela Conexos" -> solução).
    chaves = {_chave(k): k for k in registro}
    exato = next((chaves[n] for n in nomes if n in chaves), None)
    return exato or next((k for n in nomes for c, k in chaves.items() if c.startswith(n + " ")), None)


def _valor(v) -> str:
    return json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else str(v).strip()


def registros_para_topicos(registros: list) -> list[tuple[str, str]]:
    topicos = []
    for r in registros:
        if not isinstance(r, dict):
            r = {"descricao": r}
        r = {
            str(k): v for k, v in r.items()
            if k is not None and _chave(str(k)) not in CAMPOS_OCULTOS and _valor(v or "")
        }
        if not r:
            continue
        k_titulo = _campo(r, CAMPOS_TITULO) or next(iter(r))
        k_solucao, k_causa, k_codigo = _campo(r, CAMPOS_SOLUCAO), _campo(r, CAMPOS_CAUSA), _campo(r, CAMPOS_CODIGO)
        titulo = _valor(r[k_titulo])
        if k_codigo and k_codigo != k_titulo:
            titulo = f"{_valor(r[k_codigo])} - {titulo}"
        usados = {k_titulo, k_solucao, k_causa, k_codigo}
        partes = ["\n".join(f"- **{k}:** {_valor(v)}" for k, v in r.items() if k not in usados)]
        if k_causa:
            partes.append(f"**Causa:** {_valor(r[k_causa])}")
        if k_solucao:
            partes.append(f"**Solução:** {_valor(r[k_solucao])}")
        topicos.append((_linha(titulo), "\n\n".join(p for p in partes if p)))
    return topicos


def _registros_json(dados) -> list:
    if isinstance(dados, list):
        return dados
    if isinstance(dados, dict):
        listas = [v for v in dados.values() if isinstance(v, list) and v and all(isinstance(x, dict) for x in v)]
        if listas:
            return [item for lista in listas for item in lista]
        return [{"pergunta": k, "resposta": v} for k, v in dados.items()]
    return [dados]


def _registros_csv(texto: str) -> list[dict]:
    try:
        dialeto = csv.Sniffer().sniff(texto[:5000], delimiters=";,\t|")
    except csv.Error:
        dialeto = csv.excel
    return list(csv.DictReader(io.StringIO(texto), dialect=dialeto))


def _texto_pdf(dados: bytes) -> str:
    from pypdf import PdfReader

    return "\n".join(pagina.extract_text() or "" for pagina in PdfReader(io.BytesIO(dados)).pages)


# ---------------------------------------------------------------- entrada
def converter(nome_arquivo: str, dados: bytes) -> tuple[str, str]:
    """Retorna (nome do arquivo .md da base, conteúdo em markdown)."""
    caminho = Path(nome_arquivo)
    extensao = caminho.suffix.lower().lstrip(".")
    titulo = _linha(caminho.stem.replace("_", " "), 90) or "Documento"
    if extensao == "pdf":
        topicos = texto_para_topicos(_texto_pdf(dados))
    elif extensao == "json":
        topicos = registros_para_topicos(_registros_json(json.loads(_decodificar(dados))))
    elif extensao == "csv":
        topicos = registros_para_topicos(_registros_csv(_decodificar(dados)))
    elif extensao in ("md", "txt"):
        texto = _decodificar(dados)
        if extensao == "md" and re.search(r"^#{2,6}\s+\S", texto, re.M):
            # Já está no padrão da base: só garante o título do documento.
            return nome_base(titulo), texto if re.search(r"^#\s+\S", texto, re.M) else f"# {titulo}\n\n{texto}"
        topicos = texto_para_topicos(texto)
    else:
        raise ValueError(f"formato .{extensao} não suportado")
    partes = [f"# {titulo}", f"## {titulo}"]
    partes += [f"#### {t}\n\n{escapar_markdown(corpo)}" for t, corpo in topicos if corpo.strip()]
    return nome_base(titulo), "\n\n".join(partes) + "\n"
