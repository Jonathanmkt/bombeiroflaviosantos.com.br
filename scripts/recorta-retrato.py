# -*- coding: utf-8 -*-
"""
Recorta o retrato oficial do fundo de estudio, gerando PNG com transparencia.

Por que existe: o heroi da landing precisa do candidato SOBRE o azul da marca,
como nas pecas do carrossel. A campanha entregou o retrato com fundo cinza-claro
uniforme (~246), e nao a versao recortada.

Como faz, e por que assim:
  * o fundo e reconhecido por LUMINANCIA, e depois restrito ao que esta ligado
    a borda da imagem. Sem isso o dente, o olho e o brilho da pele - todos
    claros - virariam buraco no meio do rosto;
  * a borda ganha meio-tom (alpha entre 0 e 255) numa faixa estreita, senao o
    contorno fica serrilhado como recorte de tesoura;
  * o halo claro que sobra na borda e removido encolhendo a mascara em 1 px:
    fundo claro deixa franja branca quando a foto vai para cima de azul-escuro,
    e essa franja e o que denuncia recorte automatico.

Uso:
    python scripts/recorta-retrato.py
"""
import io
import os
import sys

import numpy as np
from PIL import Image
from scipy import ndimage

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ACERVO = "C:/Projetos/MIDIA-VIRTUETECH/clientes/flavio-santos/landing-page/bruto"
ORIGEM = os.path.join(ACERVO, "FOTO-EDITADA---BOMBEIRO-FLÁVIO.png")
SAIDA = os.path.join(ACERVO, "flavio-retrato-recortado.png")

# faixa de transicao: acima de CLARO e fundo puro, abaixo de ESCURO e sujeito
CLARO, ESCURO = 244.0, 224.0


def main():
    if not os.path.exists(ORIGEM):
        print("original nao encontrado no acervo - nada a fazer")
        return

    im = Image.open(ORIGEM).convert("RGB")
    px = np.asarray(im).astype(np.float32)
    lum = px @ np.array([0.2126, 0.7152, 0.0722], dtype=np.float32)

    # 1) candidato a fundo: tudo que e claro o bastante
    claro = lum >= ESCURO

    # 2) so vale como fundo o que esta LIGADO a borda da imagem
    rotulos, _ = ndimage.label(claro)
    borda = set(rotulos[0, :]) | set(rotulos[-1, :]) | set(rotulos[:, 0]) | set(rotulos[:, -1])
    borda.discard(0)
    fundo = np.isin(rotulos, list(borda))

    # 3) alpha: 0 no fundo puro, 255 no sujeito, meio-tom na faixa de transicao
    rampa = np.clip((CLARO - lum) / (CLARO - ESCURO), 0.0, 1.0)
    alpha = np.where(fundo, rampa, 1.0)

    # 4) encolhe 1 px para matar a franja clara da borda
    alpha = np.clip(alpha * 1.18 - 0.18, 0.0, 1.0)

    # 5) tira o derrame de claro na borda: onde o pixel e translucido, escurece
    #    na medida do fundo que ele carrega (des-composicao simples)
    a = alpha[..., None]
    seguro = np.maximum(a, 0.35)
    limpo = np.clip((px - 246.0 * (1.0 - a)) / seguro, 0, 255)
    px = np.where(a < 0.98, limpo, px)

    # arredondar, e nao truncar: 1.0*255 em float32 vira 254,99 e o uint8
    # devolveria 254 - um "quase opaco" que nao existe de proposito nenhum
    saida = np.rint(np.dstack([px, alpha * 255.0])).astype(np.uint8)
    recorte = Image.fromarray(saida, "RGBA")
    caixa = recorte.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    recorte = recorte.crop(caixa)
    recorte.save(SAIDA)

    total = recorte.width * recorte.height
    a2 = np.asarray(recorte.getchannel("A"))
    print("recorte: %dx%d" % (recorte.width, recorte.height))
    print("  transparente: %.1f%% | meio-tom: %.2f%% | opaco: %.1f%%"
          % (100 * (a2 == 0).sum() / total,
             100 * ((a2 > 0) & (a2 < 255)).sum() / total,
             100 * (a2 == 255).sum() / total))
    print("  gravado em %s (%.1f MB)" % (SAIDA, os.path.getsize(SAIDA) / 1048576))


main()
