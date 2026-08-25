# -*- coding: utf-8 -*-
"""
Extrai as ondas amarela e verde da propria peca do carrossel.

Por que existe: redesenhar a curva de olho nao converge - foram varias
tentativas e nenhuma bateu. Aqui a forma sai da imagem, por cor, e nao da
minha leitura dela.

Como faz:
  1. classifica cada pixel do carrossel em AMARELO, VERDE ou nada, por matiz;
  2. para cada coluna, acha o topo de cada cor e preenche dali ate a base -
     isso fecha os buracos que o corpo do candidato abre na frente da onda;
  3. suaviza a linha de topo (mediana movel), porque a borda de JPEG serrilha;
  4. grava PNG com alfa: so as formas, sem azul, sem foto.

Uso:
    python scripts/extrai-ondas.py
"""
import io
import os
import sys

import numpy as np
from PIL import Image

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEM = os.path.join(RAIZ, "docs", "referencias",
                      "Como deve ficar l Carrossel 3 posts - Bombeiro Flávio Santos.jpg")
ACERVO = "C:/Projetos/MIDIA-VIRTUETECH/clientes/flavio-santos/landing-page/bruto"
SAIDA = os.path.join(ACERVO, "ondas-do-carrossel.png")

AMARELO = (255, 199, 8)
VERDE = (0, 156, 59)


def mediana_movel(v, janela=9):
    fora = np.copy(v)
    meio = janela // 2
    for i in range(len(v)):
        a, b = max(0, i - meio), min(len(v), i + meio + 1)
        fora[i] = int(np.median(v[a:b]))
    return fora


im = Image.open(ORIGEM).convert("RGB")
px = np.asarray(im).astype(np.int16)
alt, larg = px.shape[:2]
r, g, b = px[..., 0], px[..., 1], px[..., 2]

# amarelo: alem de vermelho e verde altos com azul baixo, exige g-b grande -
# sem isso a PELE do candidato entra como amarelo (ela tem r-b alto, mas g-b
# baixo). verde: o verde domina os outros dois canais.
eh_amarelo = (r > 170) & (g > 140) & (b < 100) & (r - b > 110) & (g - b > 90)
eh_verde = (g > 90) & (g - b > 35) & (g - r > 35)

# as ondas vivem na metade de baixo da peca: fora dali e rosto, ceu ou logo
eh_amarelo[: int(alt * 0.45)] = False
eh_verde[: int(alt * 0.45)] = False

topo_am = np.full(larg, alt, dtype=np.int32)
topo_vd = np.full(larg, alt, dtype=np.int32)
for x in range(larg):
    ys = np.flatnonzero(eh_amarelo[:, x])
    if ys.size > 12:
        topo_am[x] = ys[0]
    ys = np.flatnonzero(eh_verde[:, x])
    if ys.size > 12:
        topo_vd[x] = ys[0]

# So se interpolam as LACUNAS INTERNAS - as colunas onde o corpo do candidato
# tapa a onda. Fora do intervalo em que a cor existe a forma acabou mesmo, e
# herdar da vizinha ali espalharia o amarelo pela tela inteira.
for v in (topo_am, topo_vd):
    achou = np.flatnonzero(v < alt)
    if achou.size:
        v[achou[0]:achou[-1] + 1] = np.interp(
            np.arange(achou[0], achou[-1] + 1), achou, v[achou]).astype(np.int32)

for nome, v in (("amarelo", topo_am), ("verde", topo_vd)):
    achou = np.flatnonzero(v < alt)
    if achou.size:
        v[achou[0]:achou[-1] + 1] = mediana_movel(v[achou[0]:achou[-1] + 1], 15)
    print("  %-8s de x=%d a x=%d" % (nome, achou[0], achou[-1]))

saida = np.zeros((alt, larg, 4), dtype=np.uint8)
linhas = np.arange(alt)[:, None]
mascara_vd = linhas >= topo_vd[None, :]
mascara_am = linhas >= topo_am[None, :]
for canal, valor in enumerate(VERDE):
    saida[..., canal] = np.where(mascara_vd, valor, 0)
for canal, valor in enumerate(AMARELO):
    saida[..., canal] = np.where(mascara_am, valor, saida[..., canal])
saida[..., 3] = np.where(mascara_vd | mascara_am, 255, 0)

# corta a faixa util: da primeira linha com cor ate a base
primeira = int(min(topo_am.min(), topo_vd.min()))
recorte = Image.fromarray(saida[primeira:], "RGBA")
recorte.save(SAIDA)
print("ondas: %dx%d  (topo amarelo %d, topo verde %d, base %d)"
      % (recorte.width, recorte.height, topo_am.min(), topo_vd.min(), alt))
print("proporcao %.3f  ->  %s" % (recorte.width / recorte.height, SAIDA))
