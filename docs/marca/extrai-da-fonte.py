# -*- coding: utf-8 -*-
"""
Extrai as pecas vetoriais da praguinha.pdf para SVG, sem rasterizar.
O PDF e 100% vetorial (nenhuma imagem embutida), entao o capacete e o
logotipo saem exatos - nao sao redesenho.
"""
import fitz, io, sys
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PDF = r"C:\Users\Jonathan Figueiredo\Desktop\bombeiro flavio santos\praguinha.pdf"
SAIDA = "C:/Projetos/SITES/bombeiroflaviosantos.com.br/assets/marca"

# cor do PDF (CMYK convertido) -> cor oficial do manual de ID visual
OFICIAL = {
    "#16244C": "#02174E",   # azul-marinho
    "#19A54B": "#009C3B",   # verde
    "#FEC929": "#FFC708",   # amarelo
    "#F0F1F3": "#FFFFFF",   # branco
    "#FFFFFF": "#FFFFFF",
}

def hexcor(f):
    return "#%02X%02X%02X" % tuple(round(v * 255) for v in f) if f else None

def num(v):
    return ("%.3f" % v).rstrip("0").rstrip(".")

def path_d(g):
    """Serializa os itens de um desenho do PyMuPDF em 'd' de SVG."""
    partes, atual = [], None
    for it in g["items"]:
        t = it[0]
        if t == "l":
            p1, p2 = it[1], it[2]
            if atual != (p1.x, p1.y):
                partes.append("M%s %s" % (num(p1.x), num(p1.y)))
            partes.append("L%s %s" % (num(p2.x), num(p2.y)))
            atual = (p2.x, p2.y)
        elif t == "c":
            p1, p2, p3, p4 = it[1], it[2], it[3], it[4]
            if atual != (p1.x, p1.y):
                partes.append("M%s %s" % (num(p1.x), num(p1.y)))
            partes.append("C%s %s %s %s %s %s" % (num(p2.x), num(p2.y), num(p3.x), num(p3.y), num(p4.x), num(p4.y)))
            atual = (p4.x, p4.y)
        elif t == "re":
            r = it[1]
            partes.append("M%s %sH%sV%sH%sZ" % (num(r.x0), num(r.y0), num(r.x1), num(r.y1), num(r.x0)))
            atual = None
        elif t == "qu":
            q = it[1]
            pts = [q.ul, q.ur, q.lr, q.ll]
            partes.append("M%s %s" % (num(pts[0].x), num(pts[0].y)))
            partes += ["L%s %s" % (num(p.x), num(p.y)) for p in pts[1:]]
            partes.append("Z")
            atual = None
    if g.get("closePath"):
        partes.append("Z")
    return "".join(partes)

def monta(desenhos, indices, arquivo, titulo, margem=0.0, forcar_cor=None, fundo=None):
    sel = [desenhos[i] for i in indices]
    x0 = min(d["rect"].x0 for d in sel) - margem
    y0 = min(d["rect"].y0 for d in sel) - margem
    x1 = max(d["rect"].x1 for d in sel) + margem
    y1 = max(d["rect"].y1 for d in sel) + margem
    w, h = x1 - x0, y1 - y0
    linhas = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s %s %s %s" width="%s" height="%s" role="img" aria-label="%s">'
        % (num(x0), num(y0), num(w), num(h), num(w), num(h), titulo),
        "<title>%s</title>" % titulo,
    ]
    if fundo:
        linhas.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s"/>' % (num(x0), num(y0), num(w), num(h), fundo))
    for d in sel:
        cor = forcar_cor or OFICIAL.get(hexcor(d["fill"]), hexcor(d["fill"]) or "#000000")
        regra = ' fill-rule="evenodd"' if d.get("even_odd") else ""
        linhas.append('<path fill="%s"%s d="%s"/>' % (cor, regra, path_d(d)))
    linhas.append("</svg>")
    txt = "\n".join(linhas)
    open(os.path.join(SAIDA, arquivo), "w", encoding="utf-8").write(txt)
    print("%-38s %sx%s  %d paths  %d KB" % (arquivo, num(w), num(h), len(sel), len(txt) // 1024))

doc = fitz.open(PDF)
des = doc[0].get_drawings()

CAPACETE = list(range(39, 45))
ASSINATURA = list(range(2, 52))          # BOMBEIRO + FLAVIO SANTOS + capacete + regua + 10193
SELO = list(range(0, len(des)))          # a praguinha inteira

monta(des, CAPACETE, "capacete.svg", "Capacete do Bombeiro Flavio Santos")
monta(des, CAPACETE, "capacete-branco.svg", "Capacete do Bombeiro Flavio Santos", forcar_cor="#FFFFFF")
monta(des, ASSINATURA, "assinatura-cor.svg", "Bombeiro Flavio Santos - Deputado Estadual 10193")
monta(des, ASSINATURA, "assinatura-branco.svg", "Bombeiro Flavio Santos - Deputado Estadual 10193", forcar_cor="#FFFFFF")
monta(des, ASSINATURA, "assinatura-navy.svg", "Bombeiro Flavio Santos - Deputado Estadual 10193", forcar_cor="#02174E")
monta(des, SELO, "selo-propaganda.svg", "Selo de propaganda eleitoral - CNPJ 68.461.977/0001-40")

# --- o selo inteiro precisa ser recortado pelo circulo: a onda transborda a pagina ---
def monta_selo():
    pag = doc[0].rect
    circ = des[1]["rect"]
    cx, cy = (circ.x0 + circ.x1) / 2, (circ.y0 + circ.y1) / 2
    r = (circ.x1 - circ.x0) / 2
    L = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" width="%s" height="%s" role="img" aria-label="Selo de propaganda eleitoral">'
         % (num(pag.x1), num(pag.y1), num(pag.x1), num(pag.y1)),
         "<title>Selo de propaganda eleitoral - CNPJ 68.461.977/0001-40</title>",
         '<defs><clipPath id="recorte"><circle cx="%s" cy="%s" r="%s"/></clipPath></defs>' % (num(cx), num(cy), num(r)),
         '<rect width="%s" height="%s" fill="#02174E"/>' % (num(pag.x1), num(pag.y1)),
         '<g clip-path="url(#recorte)">']
    for d in des[1:]:
        cor = OFICIAL.get(hexcor(d["fill"]), hexcor(d["fill"]) or "#000000")
        regra = ' fill-rule="evenodd"' if d.get("even_odd") else ""
        L.append('<path fill="%s"%s d="%s"/>' % (cor, regra, path_d(d)))
    L += ["</g>", "</svg>"]
    txt = "\n".join(L)
    open(os.path.join(SAIDA, "selo-propaganda.svg"), "w", encoding="utf-8").write(txt)
    print("selo-propaganda.svg (recortado)  %sx%s  %d KB" % (num(pag.x1), num(pag.y1), len(txt) // 1024))

monta_selo()

# --- a linha legal do selo e texto real (Arial Bold), curvada caractere a caractere ---
import math, html
def texto_curvo():
    L = []
    for b in doc[0].get_text("rawdict")["blocks"]:
        for lin in b.get("lines", []):
            dx, dy = lin["dir"]
            ang = math.degrees(math.atan2(dy, dx))
            for s in lin["spans"]:
                for c in s["chars"]:
                    ch = c["c"]
                    if not ch.strip():
                        continue
                    ox, oy = c["origin"]
                    L.append('<text x="%s" y="%s" transform="rotate(%s %s %s)" font-family="Arial, Helvetica, sans-serif" font-weight="700" font-size="%s" fill="#02174E">%s</text>'
                             % (num(ox), num(oy), num(ang), num(ox), num(oy), num(s["size"]), html.escape(ch)))
    return L

alvo = os.path.join(SAIDA, "selo-propaganda.svg")
svg = open(alvo, encoding="utf-8").read()
svg = svg.replace("</svg>", "\n".join(texto_curvo()) + "\n</svg>")
open(alvo, "w", encoding="utf-8").write(svg)
print("selo-propaganda.svg: linha legal acrescentada (%d caracteres)" % svg.count("<text"))

# --- pecas soltas que o site usa fora da assinatura ---
ONDA = [52, 53]                      # a onda amarela e verde do rodape da peca
REPUBLICANOS = list(range(54, len(des)))

monta(des, ONDA, "onda.svg", "Onda amarela e verde da campanha")
monta(des, REPUBLICANOS, "republicanos.svg", "Republicanos 10")
monta(des, REPUBLICANOS, "republicanos-branco.svg", "Republicanos 10", forcar_cor="#FFFFFF")
