# -*- coding: utf-8 -*-
"""
Converte para a web as fontes da campanha.

Entrada : o acervo de midia (OTF/TTF originais, fora do git)
Saida   : assets/fontes/    (WOFF2 subconjunto + o fontes.css pronto)

O que faz, e por que:
  * subconjunto: o site e em pt-BR e nao precisa de grego, cirilico nem de
    centenas de glifos que ninguem vai ver - cortar isso e o que faz a fonte
    caber no primeiro carregamento;
  * WOFF2, o unico formato que importa hoje: todo navegador atual le, e ele ja
    vem comprimido (Brotli), entao nao adianta gzip por cima;
  * escreve o proprio fontes.css - peso errado no @font-face faz o navegador
    sintetizar negrito e borrar o desenho, e isso nao pode depender de memoria;
  * imprime a tabela antes/depois, porque economia se mede, nao se afirma.

Uso:
    python scripts/prepara-fontes.py
"""
import io
import os
import sys

from fontTools import subset
from fontTools.ttLib import TTFont

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# o acervo de midia da empresa, fora do git - so existe nesta maquina
ACERVO = "C:/Projetos/MIDIA-VIRTUETECH/clientes/flavio-santos/landing-page/bruto/fontes"
DESTINO = os.path.join(RAIZ, "assets", "fontes")

# (familia CSS, arquivo de origem, nome de saida, peso CSS)
# Quais arquivos: nao foram escolhidos no olho. A largura da Transducer e o peso
# de cada TT Runs sairam da comparacao das larguras de avanco com as fontes
# embutidas no manual de ID visual - erro zero em todos.
FONTES = [
    ("Transducer", "transducer-normalregular.otf", "transducer-400", 400),
    ("Transducer", "transducer-normalmedium.otf", "transducer-500", 500),
    ("Transducer", "transducer-normalbold.otf", "transducer-700", 700),
    ("Transducer", "transducer-normalblack.otf", "transducer-900", 900),
    ("TT Runs", "TT Runs Trial Regular.ttf", "ttruns-400", 400),
    ("TT Runs", "TT Runs Trial Black.ttf", "ttruns-900", 900),
]

# o que uma pagina em pt-BR realmente usa: latino basico, os acentuados do
# portugues, pontuacao e os simbolos de moeda e numero que aparecem em texto.
FAIXAS = "U+0020-007E,U+00A0-00FF,U+0131,U+0152-0153,U+02C6,U+2000-206F,U+2074,U+20AC,U+2122,U+2212"


def kb(caminho):
    return os.path.getsize(caminho) / 1024


def converte(arquivo, nome):
    origem = os.path.join(ACERVO, arquivo)
    destino = os.path.join(DESTINO, nome + ".woff2")

    fonte = TTFont(origem)
    total_glifos = len(fonte.getGlyphOrder())

    opcoes = subset.Options()
    opcoes.flavor = "woff2"
    opcoes.layout_features = ["*"]        # mantem kerning e ligaduras
    opcoes.desubroutinize = True          # exigido para CFF -> woff2 confiavel
    opcoes.notdef_outline = True
    opcoes.recalc_bounds = True
    recorte = subset.Subsetter(options=opcoes)
    recorte.populate(unicodes=subset.parse_unicodes(FAIXAS))
    recorte.subset(fonte)
    fonte.flavor = "woff2"
    fonte.save(destino)
    restantes = len(fonte.getGlyphOrder())
    fonte.close()

    print("  %-28s %6.1f KB -> %6.1f KB  (%d de %d glifos, -%.0f%%)"
          % (arquivo, kb(origem), kb(destino), restantes, total_glifos,
             100 * (1 - kb(destino) / kb(origem))))
    return True


os.makedirs(DESTINO, exist_ok=True)
if not os.path.isdir(ACERVO):
    print("acervo nao encontrado: %s" % ACERVO)
    print("as fontes originais so existem na maquina da empresa - nada a fazer aqui")
    sys.exit(0)

feitas = []
familia_atual = None
for familia, arquivo, nome, peso in FONTES:
    if familia != familia_atual:
        print("\n%s" % familia)
        familia_atual = familia
    if not os.path.exists(os.path.join(ACERVO, arquivo)):
        print("  %-28s NAO ENCONTRADO no acervo" % arquivo)
        continue
    converte(arquivo, nome)
    feitas.append((familia, nome, peso))

# O caminho no url() e relativo a este CSS, entao vale tanto importado da raiz
# quanto aberto de dentro da propria pasta.
css = ["/* Gerado por scripts/prepara-fontes.py - nao edite a mao. */", ""]
for familia, nome, peso in feitas:
    css += ["@font-face {",
            '  font-family: "%s";' % familia,
            '  src: url("%s.woff2") format("woff2");' % nome,
            "  font-weight: %d;" % peso,
            "  font-style: normal;",
            "  font-display: swap;",
            "}", ""]
open(os.path.join(DESTINO, "fontes.css"), "w", encoding="utf-8").write("\n".join(css))
print("\nfontes.css: %d declaracoes @font-face, %.1f KB no total de WOFF2"
      % (len(feitas), sum(kb(os.path.join(DESTINO, n + ".woff2")) for _f, n, _p in feitas)))
