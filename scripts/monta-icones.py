# -*- coding: utf-8 -*-
"""
Monta o sprite de ícones do site a partir do acervo Lucide.

Por que um sprite, e não um <svg> inline por ícone: o mesmo desenho aparece em
mais de um lugar, e repetir o traçado inflaria o HTML. O sprite entra uma vez,
escondido, e cada uso vira um <use href="#ic-nome"> de uma linha.

Por que copiar em vez de apontar para o acervo: o acervo vive fora do git e só
existe nesta máquina - apontar o site para lá o quebraria em qualquer outra.

Uso:
    python scripts/monta-icones.py
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ACERVO = "C:/Projetos/MIDIA-VIRTUETECH/empresa/insumos/lucide/icons"
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(RAIZ, "assets", "marca", "icones.svg")

# (arquivo no acervo, id no sprite) — o id é o papel na página, não o nome do
# desenho: se um dia trocarmos o ícone, o HTML não muda.
ICONES = [
    ("bell-ring", "criancas"),
    ("graduation-cap", "mirim"),
    ("footprints", "esporte"),
    ("waves", "litoral"),
    ("map-pin", "itinerante"),
    ("heart-pulse", "saude"),
    ("smartphone", "digital"),
    ("shield-check", "regional"),
    ("bus", "mobilidade"),
    ("scale", "juridica"),
    ("clock-4", "jornada"),
    ("arrow-down", "desce"),
]


def miolo(caminho):
    """Devolve só o conteúdo de dentro do <svg>, sem a casca."""
    bruto = open(caminho, encoding="utf-8").read()
    dentro = re.search(r"<svg[^>]*>(.*)</svg>", bruto, re.S).group(1)
    return re.sub(r"\s+", " ", dentro).strip()


if not os.path.isdir(ACERVO):
    print("acervo Lucide não encontrado: %s" % ACERVO)
    print("os ícones só existem na máquina da empresa — nada a fazer aqui")
    sys.exit(0)

partes = ['<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">']
for arquivo, nome in ICONES:
    caminho = os.path.join(ACERVO, arquivo + ".svg")
    if not os.path.exists(caminho):
        print("  %-16s NÃO ENCONTRADO" % arquivo)
        continue
    partes.append('<symbol id="ic-%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                  'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</symbol>'
                  % (nome, miolo(caminho)))
    print("  %-16s -> #ic-%s" % (arquivo, nome))
partes.append("</svg>")

texto = "\n".join(partes)
os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
open(SAIDA, "w", encoding="utf-8").write(texto)
print("\n%s  (%d ícones, %.1f KB)" % (SAIDA, len(ICONES), len(texto) / 1024))
print("Licença Lucide: ISC — cópia em %s/../LICENSE" % ACERVO)
