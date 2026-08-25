# -*- coding: utf-8 -*-
"""
Prepara para a web as fotos originais da campanha.

Entrada : docs/referencias/  (o que e leve o bastante para viver no git)
          o acervo de midia   (o que e pesado demais - foto de cliente em alta)
Saida   : assets/fotos/      (o que o site serve)

O retrato oficial tem 5,2 MB e e midia de cliente: pela regra da casa ele vive
no acervo, fora do git, e nao no repositorio. Este script sabe buscar nos dois
lugares - e avisa, em vez de falhar calado, se o acervo nao estiver na maquina.

O que faz, e por que:
  * recorta o PNG com fundo transparente ate o conteudo real - o original tem
    quase metade da tela em pixel vazio, e pixel vazio pesa igual;
  * gera tres larguras por foto, para o srcset escolher pela tela;
  * grava em AVIF e WebP sempre, e JPEG so onde nao ha transparencia -
    foto com alfa em PNG pesa ordens de grandeza mais e nao compensa;
  * imprime a tabela de tamanhos - a economia e o resultado, e ela se mede.

Uso:
    python scripts/prepara-fotos.py
"""
import io
import os
import sys

from PIL import Image

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEM = os.path.join(RAIZ, "docs", "referencias")
# o acervo de midia da empresa, fora do git - so existe nesta maquina
ACERVO = "C:/Projetos/MIDIA-VIRTUETECH/clientes/flavio-santos/landing-page/bruto"
DESTINO = os.path.join(RAIZ, "assets", "fotos")

# (pasta de origem, arquivo, nome de saida, recortar pelo alfa?, larguras, topo)
# "topo" corta a imagem na fração de altura indicada, contando do alto: o herói
# mostra cabeça e peito, e as mãos cruzadas ficam fora do quadro. None = inteira.
FOTOS = [
    (ORIGEM, "fotobombeirocorrendo.png", "flavio-correndo", True, [360, 520, 696], None),
    (ACERVO, "FOTO-EDITADA---BOMBEIRO-FLÁVIO.png", "flavio-retrato", False, [640, 960, 1440], None),
    # foto com alfa entregue pela campanha (25/08/2026), no lugar do recorte
    # automatico. 0.615 e o corte que devolve a MESMA proporcao (1,2155) do
    # heroi que ja estava no ar, e cai bem acima das maos cruzadas.
    (ACERVO, "bombeirofundotransparente.png", "flavio-heroi", True, [520, 780, 1040], 0.597),
    (ACERVO, "ponte-estaiada.png", "ponte", False, [520, 780, 1040], None),
    # ondas desenhadas pelo CEO (25/08/2026), 2400x600, cores exatas do manual
    (ACERVO, "ondas.png", "ondas", False, [1200, 1800, 2400], None),
    # ilustracao sintetica (Gemini) para a bandeira das criancas - nao e foto
    # de pessoa real, e a marcacao da pagina diz isso
    (ACERVO, "meninafundotransparente.png", "menina", True, [360, 520, 700], None),
]

MARGEM = 0.015  # folga em volta do recorte, para o contorno nao encostar na borda


def kb(caminho):
    return os.path.getsize(caminho) / 1024


def prepara(pasta, arquivo, nome, recortar, larguras, topo=None):
    im = Image.open(os.path.join(pasta, arquivo))
    tem_alfa = im.mode in ("RGBA", "LA")

    if topo:
        # corta ANTES do recorte pelo alfa, para a nova caixa acompanhar os
        # ombros: cortar depois deixaria margem lateral vazia dos dois lados
        antes = im.size
        im = im.crop((0, 0, im.width, round(im.height * topo)))
        print("  corte por altura (%.0f%% do alto): %dx%d -> %dx%d"
              % (100 * topo, antes[0], antes[1], im.width, im.height))

    if recortar and tem_alfa:
        caixa = im.getchannel("A").getbbox()
        folga = round(max(im.width, im.height) * MARGEM)
        caixa = (max(0, caixa[0] - folga), max(0, caixa[1] - folga),
                 min(im.width, caixa[2] + folga), min(im.height, caixa[3] + folga))
        antes = im.size
        im = im.crop(caixa)
        print("  recorte pelo alfa: %dx%d -> %dx%d" % (antes[0], antes[1], im.width, im.height))

    if not tem_alfa:
        im = im.convert("RGB")

    print("  proporcao %.4f (largura/altura)" % (im.width / im.height))
    for larg in larguras:
        if larg > im.width:
            print("  %dpx ignorado: maior que o original" % larg)
            continue
        alt = round(larg * im.height / im.width)
        peca = im.resize((larg, alt), Image.LANCZOS)
        base = os.path.join(DESTINO, "%s-%d" % (nome, larg))

        peca.save(base + ".avif", quality=58)
        peca.save(base + ".webp", quality=80, method=6)
        if tem_alfa:
            # Nao se grava PNG aqui de proposito: foto com alfa em PNG pesa ~11x
            # o mesmo WebP (872 KB contra 79 KB, medido em 25/08/2026). WebP com
            # alfa e suportado por todo navegador atual, e AVIF vem antes dele -
            # um fallback de 872 KB seria um tiro no pe de quem o servisse.
            print("  %4dpx  %4dx%-4d  avif %6.1f KB | webp %6.1f KB  (alfa: sem PNG)"
                  % (larg, larg, alt, kb(base + ".avif"), kb(base + ".webp")))
            continue
        else:
            peca.save(base + ".jpg", quality=82, optimize=True, progressive=True)
            legado = base + ".jpg"

        print("  %4dpx  %4dx%-4d  avif %6.1f KB | webp %6.1f KB | %s %6.1f KB"
              % (larg, larg, alt, kb(base + ".avif"), kb(base + ".webp"),
                 os.path.splitext(legado)[1][1:], kb(legado)))


os.makedirs(DESTINO, exist_ok=True)
for pasta, arquivo, nome, recortar, larguras, topo in FOTOS:
    caminho = os.path.join(pasta, arquivo)
    if not os.path.exists(caminho):
        print("\n%s  NAO ENCONTRADO em %s" % (arquivo, pasta))
        print("  se a pasta e o acervo, ele so existe na maquina da empresa - nada a fazer aqui")
        continue
    onde = "acervo" if pasta == ACERVO else "repositorio"
    print("\n%s  (%.1f MB, no %s)" % (arquivo, os.path.getsize(caminho) / 1048576, onde))
    prepara(pasta, arquivo, nome, recortar, larguras, topo)
