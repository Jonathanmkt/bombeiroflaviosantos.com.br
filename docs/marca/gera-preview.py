# -*- coding: utf-8 -*-
import os
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
D = "C:/Projetos/SITES/bombeiroflaviosantos.com.br/assets/marca"
DOCS = "C:/Projetos/SITES/bombeiroflaviosantos.com.br/docs/marca"

def svg(nome, larg):
    s = open(os.path.join(D, nome), encoding="utf-8").read()
    s = re.sub(r'\s(width|height)="[^"]*"', '', s, count=2)
    return s.replace('<svg ', '<svg style="width:%s;height:auto;display:block" ' % larg, 1)

PAL = [("Azul-marinho", "#02174E", "C99 M100 Y45 K22"), ("Verde", "#009C3B", "C97 M3 Y100 K0"),
       ("Amarelo", "#FFC708", "C0 M31 Y94 K0"), ("Azul vivo", "#0744F4", "C91 M78 Y0 K0")]
chips = "".join(
    '<div class="chip"><div class="swatch" style="background:%s"></div><b>%s</b><code>%s</code><small>%s</small></div>'
    % (h, n, h, c) for n, h, c in PAL)

CONTR = [("branco sobre navy","17,00:1","ok"),("amarelo sobre navy","10,87:1","ok"),
         ("navy sobre branco","17,00:1","ok"),("branco sobre azul vivo","6,68:1","ok"),
         ("verde sobre navy","4,71:1","ok"),("branco sobre verde","3,61:1","aviso"),
         ("amarelo sobre branco","1,56:1","erro"),("azul vivo sobre navy","2,54:1","erro")]
linhas = "".join('<tr class="%s"><td>%s</td><td><b>%s</b></td><td>%s</td></tr>' %
                 (k, a, b, {"ok":"passa em texto normal","aviso":"só em texto grande","erro":"não usar em texto"}[k])
                 for a, b, k in CONTR)

html = """<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Marca — Bombeiro Flávio Santos 10193</title>
<style>
@import url("../../assets/fontes/fontes.css");
.fonte.tr b{font-family:"Transducer",sans-serif}
.fonte.tt b{font-family:"TT Runs",sans-serif}
:root{--navy:#02174E;--verde:#009C3B;--amarelo:#FFC708;--azul:#0744F4}
*{box-sizing:border-box;margin:0;padding:0}
body{font:16px/1.6 "Montserrat",system-ui,sans-serif;color:#111;background:#F4F6F9;padding:clamp(16px,4vw,40px)}
h1{font-size:clamp(22px,5vw,32px);color:var(--navy);letter-spacing:-.02em}
h2{font-size:15px;text-transform:uppercase;letter-spacing:.14em;color:#5A6577;margin:40px 0 14px;font-weight:700}
.aviso{background:#fff;border-left:4px solid var(--amarelo);padding:14px 16px;margin-top:14px;font-size:14.5px}
.grade{display:grid;gap:14px;align-items:start;grid-template-columns:repeat(auto-fill,minmax(230px,1fr))}
.cartao{background:#fff;border:1px solid #E1E6EE;border-radius:12px;padding:20px;display:flex;flex-direction:column;gap:14px}
.cartao.escuro{background:var(--navy);border-color:var(--navy)}
.cartao.amarelo{background:var(--amarelo);border-color:var(--amarelo)}
.rot{font:600 11px/1.4 ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;color:#7A8699}
.cartao.escuro .rot{color:#9FB0CE}
.chip{background:#fff;border:1px solid #E1E6EE;border-radius:12px;padding:14px;display:flex;flex-direction:column;gap:6px}
.swatch{height:64px;border-radius:8px;margin-bottom:6px}
.chip code{font:600 13px ui-monospace,monospace;color:#111}
.chip small{color:#7A8699;font-size:12px}
table{width:100%;border-collapse:collapse;background:#fff;border:1px solid #E1E6EE;border-radius:12px;overflow:hidden;font-size:14.5px}
td{padding:10px 14px;border-bottom:1px solid #EEF1F6}
tr.erro td{background:#FFF1F0}tr.aviso td{background:#FFFBEB}
.fontes{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(260px,1fr))}
.fonte{background:#fff;border:1px solid #E1E6EE;border-radius:12px;padding:18px}
.fonte b{display:block;font-size:19px;color:var(--navy)}
.tag{display:inline-block;margin-top:8px;font-size:11.5px;font-weight:700;padding:3px 9px;border-radius:999px}
.livre{background:#E4F7EC;color:#0A6B35}.paga{background:#FFE9E7;color:#9B1C13}
</style></head><body>
<h1>Marca — Bombeiro Flávio Santos · 10193</h1>
<p style="max-width:62ch;margin-top:8px;color:#4A5468">Material extraído da fonte oficial. A praguinha é vetor puro,
então o capacete e o logotipo saíram como curvas — não são redesenho.</p>

<h2>Assinatura</h2>
<div class="grade">
  <div class="cartao"><span class="rot">assinatura-cor.svg</span>__COR__</div>
  <div class="cartao escuro"><span class="rot">assinatura-branco.svg</span>__BRANCO__</div>
  <div class="cartao amarelo"><span class="rot">assinatura-navy.svg</span>__NAVY__</div>
</div>

<h2>Capacete</h2>
<div class="grade">
  <div class="cartao"><span class="rot">capacete.svg</span>__CAP__</div>
  <div class="cartao escuro"><span class="rot">capacete-branco.svg</span>__CAPB__</div>
  <div class="cartao"><span class="rot">selo-propaganda.svg</span>__SELO__</div>
</div>

<h2>Paleta oficial</h2>
<div class="grade">__CHIPS__</div>

<h2>Contraste medido</h2>
<table>__LINHAS__</table>

<h2>Tipografia</h2>
<div class="fontes">
  <div class="fonte tr"><b>Transducer</b><span>título — 400 · 500 · 700 · 900</span><span class="tag livre">pronta em assets/fontes/</span></div>
  <div class="fonte tt"><b>TT Runs</b><span>apoio e número — 400 · 900</span><span class="tag livre">pronta em assets/fontes/</span></div>
  <div class="fonte"><b>Montserrat</b><span>texto corrido</span><span class="tag livre">Google Fonts</span></div>
</div>
<div class="aviso"><b>As três fontes do manual estão disponíveis.</b> Transducer e TT Runs foram convertidas para WOFF2 e
subconjuntadas para pt-BR — 90,9 KB somando os seis arquivos. Os originais ficam no acervo, fora do git.</div>
</body></html>"""

html = (html.replace("__COR__", svg("assinatura-cor.svg", "100%"))
            .replace("__BRANCO__", svg("assinatura-branco.svg", "100%"))
            .replace("__NAVY__", svg("assinatura-navy.svg", "100%"))
            .replace("__CAP__", svg("capacete.svg", "96px"))
            .replace("__CAPB__", svg("capacete-branco.svg", "96px"))
            .replace("__SELO__", svg("selo-propaganda.svg", "100%"))
            .replace("__CHIPS__", chips).replace("__LINHAS__", linhas))
open(os.path.join(DOCS, "PREVIEW.html"), "w", encoding="utf-8").write(html)
print("PREVIEW.html", len(html) // 1024, "KB")
