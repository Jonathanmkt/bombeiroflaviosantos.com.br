# -*- coding: utf-8 -*-
"""
Gera os artboards .dc.html das direções de design.

Existe porque as fontes da marca precisam viajar embutidas: o canvas roda num
quadro sem saída de rede (só Google Fonts passa), então Transducer e TT Runs vão
como @font-face em data: URI. Escrever isso à mão em seis arquivos seria seis
chances de errar; aqui o cabeçalho é um só.

Uso:
    python docs/design/gera-artboards.py
"""
import base64
import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))


def b64(caminho):
    return base64.b64encode(open(os.path.join(RAIZ, caminho), "rb").read()).decode()


T900 = b64("assets/fontes/transducer-900.woff2")
T700 = b64("assets/fontes/transducer-700.woff2")
TT900 = b64("assets/fontes/ttruns-900.woff2")

CABECA = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap">
  <style>
    @font-face{font-family:"Transducer";src:url(data:font/woff2;base64,%s) format("woff2");font-weight:900;font-style:normal;font-display:swap}
    @font-face{font-family:"Transducer";src:url(data:font/woff2;base64,%s) format("woff2");font-weight:700;font-style:normal;font-display:swap}
    @font-face{font-family:"TT Runs";src:url(data:font/woff2;base64,%s) format("woff2");font-weight:900;font-style:normal;font-display:swap}
    :root{
      --navy:#02174E; --verde:#009C3B; --amarelo:#FFC708; --verde-texto:#00822F;
      --branco:#FFFFFF; --claro:#F4F6FA; --texto-escuro:#12203F;
      --cinza:#5B6B86; --cinza-claro:#9FB0CE;
      --borda-escura:rgba(2,23,78,.12); --borda:rgba(255,255,255,.14);
      --titulo:"Transducer","Montserrat",sans-serif;
      --apoio:"TT Runs","Transducer","Montserrat",sans-serif;
      --texto:"Montserrat",system-ui,sans-serif;
    }
    *{box-sizing:border-box;margin:0;padding:0}
    body{font-family:var(--texto);line-height:1.65;color:var(--texto-escuro);
         -webkit-font-smoothing:antialiased}
    img{display:block;max-width:100%%}
    a{color:var(--verde-texto);text-decoration:none}
    a:hover{color:var(--verde)}
    .chapeu{display:block;font-family:var(--apoio);font-weight:900;font-size:12.5px;
            letter-spacing:.22em;text-transform:uppercase;color:var(--verde-texto);margin-bottom:12px}
    h2{font-family:var(--titulo);font-weight:900;font-size:44px;line-height:1.06;letter-spacing:-.015em}
""" % (T900, T700, TT900)

FIM_CABECA = """  </style>
</helmet>
"""

RODAPE = """</x-dc>
</body>
</html>
"""

# ---------------------------------------------------------------- conteúdo real
DEPOIMENTO = [
    "Há 23 anos, aos 19, decidi dedicar minha vida a proteger a vida do próximo. Entrei para a "
    "corporação, virei bombeiro, e essa passou a ser minha missão todo dia: arriscar minha vida "
    "pra salvar a de outras pessoas.",
    "Quem acompanha nossa caminhada sabe que esse compromisso nunca ficou só na farda. Sempre "
    "esteve em tudo que fizemos, cuidando das pessoas e servindo nossa sociedade na corrida de "
    "pais e filhos, nos desafios de corrida 24 horas, sempre com arrecadação de alimentos.",
    "E hoje, depois de tantos pedidos ao longo dos anos, não dava pra dar esse passo novo sem ter "
    "do meu lado as pessoas mais importantes da minha vida: minha esposa e minha filha, que "
    "sempre acreditaram em mim e caminham comigo em cada desafio.",
    "É com gratidão e responsabilidade que dou esse passo.",
]
ASSINA = ("Vou seguir fazendo o que sempre fiz: servir, trabalhar e dar meu melhor pela vida "
          "das pessoas.")
FATOS = [
    ("23 anos", "de corporação — entrou aos 19"),
    ("Guarda-vidas", "em Praia Grande, Baixada Santista"),
    ("Empresário", "e idealizador de projetos sociais"),
    ("Corrida de pais e filhos", "e desafios de 24 horas, com arrecadação de alimentos"),
    ("Esposa e filha", "caminham com ele em cada desafio"),
]
MARCAS = ["Recordista mundial de corrida", "168 km em 24 h na rua",
          "201 km em 24 h na esteira", "Ironman Full"]

CAPACETE = ('<svg viewBox="0 0 32 21" width="34" height="22" aria-hidden="true">'
            '<path fill="currentColor" d="M16 1.6c-5.2 0-9.1 3-10.3 7.6H3.2C2 9.2 1 10 1 11.1'
            'c0 1.2 1 2 2.2 2h25.6c1.2 0 2.2-.8 2.2-2 0-1.1-1-1.9-2.2-1.9h-2.5C25.1 4.6 21.2 1.6 16 1.6z'
            'm0 3.1c3.5 0 6.2 1.9 7.1 4.5H8.9C9.8 6.6 12.5 4.7 16 4.7z"/>'
            '<rect x="1" y="15.4" width="30" height="3.4" rx="1.7" fill="currentColor"/></svg>')


def escreve(nome, corpo, css_extra=""):
    caminho = os.path.join(AQUI, nome)
    open(caminho, "w", encoding="utf-8").write(CABECA + css_extra + FIM_CABECA + corpo + RODAPE)
    print("  %-22s %6.1f KB" % (nome, os.path.getsize(caminho) / 1024))


# ================================================================ QUEM SOU EU
# Direção A — Editorial: o depoimento manda, o retrato ancora, os fatos viram
# um friso horizontal no fim. É a que menos muda o que já está no ar.
escreve("Main.dc.html", """
<div style="background:var(--claro);padding:72px 64px">
  <div style="max-width:1000px;margin:0 auto">
    <span class="chapeu">Quem sou eu</span>
    <h2 style="max-width:16ch">Esse compromisso nunca ficou só na farda.</h2>
    <div style="display:grid;grid-template-columns:1.25fr .75fr;gap:48px;margin-top:40px;align-items:start">
      <div style="display:flex;flex-direction:column;gap:18px">
        %s
        <p style="margin-top:8px;padding-left:20px;border-left:4px solid var(--verde);
                  font-weight:600;color:var(--navy);font-size:19px;line-height:1.5">%s</p>
      </div>
      <div style="position:relative">
        <div style="position:absolute;inset:auto 0 0 0;height:62%%;background:var(--navy);border-radius:18px"></div>
        <img src="retrato.webp" alt="" style="position:relative;width:100%%;border-radius:18px">
      </div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:20px;margin-top:44px;
                padding-top:28px;border-top:1px solid var(--borda-escura)">
      %s
    </div>
  </div>
</div>
""" % (
    "".join('<p style="font-size:17px">%s</p>' % p for p in DEPOIMENTO),
    ASSINA,
    "".join('<div><b style="display:block;font-family:var(--titulo);font-weight:700;color:var(--navy);'
            'font-size:15px;line-height:1.25">%s</b>'
            '<span style="display:block;margin-top:6px;font-size:13.5px;color:var(--cinza)">%s</span></div>'
            % (t, s) for t, s in FATOS),
))

# Direção B — Linha do tempo: a biografia vira percurso, com o capacete
# marcando cada marco. Muda a leitura de "texto" para "trajetória".
escreve("QuemSouEuB.dc.html", """
<div style="background:var(--navy);color:var(--branco);padding:72px 64px">
  <div style="max-width:1000px;margin:0 auto">
    <span class="chapeu" style="color:var(--amarelo)">Quem sou eu</span>
    <h2 style="max-width:18ch">23 anos protegendo vidas — e nunca só na farda.</h2>
    <div style="display:grid;grid-template-columns:.9fr 1.1fr;gap:56px;margin-top:44px;align-items:start">
      <div style="display:flex;flex-direction:column;gap:0">
        %s
      </div>
      <div style="display:flex;flex-direction:column;gap:20px">
        %s
        <p style="padding:22px 24px;background:var(--verde-texto);border-radius:16px;
                  font-family:var(--titulo);font-weight:700;font-size:19px;line-height:1.4">%s</p>
      </div>
    </div>
  </div>
</div>
""" % (
    "".join(
        '<div style="display:flex;gap:18px;padding-bottom:26px;%s">'
        '<div style="flex:none;width:38px;color:var(--amarelo)">%s</div>'
        '<div><b style="display:block;font-family:var(--titulo);font-weight:700;font-size:17px">%s</b>'
        '<span style="display:block;margin-top:4px;font-size:14.5px;color:var(--cinza-claro)">%s</span></div>'
        '</div>' % ("border-left:2px solid rgba(255,255,255,.18);margin-left:19px;padding-left:26px"
                    if i else "", CAPACETE if not i else
                    '<div style="width:11px;height:11px;border-radius:50%;background:var(--amarelo);margin:7px 0 0 13px"></div>',
                    t, s)
        for i, (t, s) in enumerate(FATOS)),
    "".join('<p style="font-size:16.5px;color:#DCE5F4">%s</p>' % p for p in DEPOIMENTO[:3]),
    ASSINA,
))

# Direção C — Citação: a frase dele ocupa a dobra, o resto vira apoio.
# É a mais arriscada: aposta tudo na voz, e o depoimento encolhe.
escreve("QuemSouEuC.dc.html", """
<div style="background:var(--claro);padding:72px 64px">
  <div style="max-width:1000px;margin:0 auto">
    <span class="chapeu">Quem sou eu</span>
    <div style="display:flex;gap:28px;align-items:flex-start;margin-top:8px">
      <span style="font-family:var(--apoio);font-weight:900;font-size:112px;line-height:.7;
                   color:var(--amarelo);flex:none">&ldquo;</span>
      <p style="font-family:var(--titulo);font-weight:900;font-size:38px;line-height:1.14;
                letter-spacing:-.015em;color:var(--navy);max-width:20ch">
        Arriscar minha vida pra salvar a de outras pessoas.</p>
    </div>
    <div style="display:grid;grid-template-columns:.85fr 1.15fr;gap:44px;margin-top:44px;align-items:start">
      <img src="retrato.webp" alt="" style="width:100%%;border-radius:18px">
      <div style="display:flex;flex-direction:column;gap:16px">
        %s
        <p style="padding-left:20px;border-left:4px solid var(--verde);font-weight:600;
                  color:var(--navy);font-size:18px;line-height:1.5">%s</p>
        <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:6px">%s</div>
      </div>
    </div>
  </div>
</div>
""" % (
    "".join('<p style="font-size:16.5px">%s</p>' % p for p in DEPOIMENTO[1:3]),
    ASSINA,
    "".join('<span style="border:1px solid var(--borda-escura);border-radius:999px;padding:7px 14px;'
            'font-size:13px;color:var(--cinza)">%s</span>' % m for m in MARCAS),
))

# ================================================================ FECHO
# Direção A — Cédula: o gesto que o eleitor vai repetir na urna.
escreve("FechoA.dc.html", """
<div style="background:var(--navy);color:var(--branco);padding:76px 64px;text-align:center">
  <div style="max-width:1000px;margin:0 auto">
    <h2 style="font-size:48px">Juntos por São Paulo.</h2>
    <p style="margin-top:12px;color:var(--cinza-claro);font-size:17px">Coragem para proteger, preparado para cuidar.</p>
    <div style="margin:40px auto 0;width:fit-content;background:var(--branco);color:var(--navy);
                border-radius:10px;padding:22px 30px 26px;box-shadow:0 26px 60px rgba(0,0,0,.45);text-align:left">
      <span style="display:block;font-family:var(--apoio);font-weight:900;font-size:11px;
                   letter-spacing:.22em;text-transform:uppercase;color:var(--cinza)">Deputado Estadual</span>
      <div style="display:flex;gap:9px;margin-top:12px">
        %s
      </div>
      <span style="display:block;margin-top:14px;font-size:13px;color:var(--cinza)">
        Bombeiro Flávio Santos &middot; Republicanos 10</span>
    </div>
    <a href="#" style="display:inline-flex;align-items:center;gap:11px;margin-top:34px;padding:15px 28px;
              border-radius:999px;background:var(--branco);color:var(--navy);font-weight:700;font-size:15.5px">
      @bombeiroflaviosantos</a>
  </div>
</div>
""" % "".join(
    '<span style="width:56px;height:74px;display:grid;place-items:center;border:2px solid var(--borda-escura);'
    'border-radius:8px;font-family:var(--apoio);font-weight:900;font-size:44px;color:var(--navy)">%s</span>' % d
    for d in "10193"))

# Direção B — Faixa: o lema em escala de rua, o número como assinatura.
escreve("FechoB.dc.html", """
<div style="background:var(--verde-texto);color:var(--branco);padding:0;overflow:hidden">
  <div style="padding:72px 64px;max-width:1000px;margin:0 auto;display:grid;
              grid-template-columns:1.15fr .85fr;gap:48px;align-items:center">
    <div>
      <p style="font-family:var(--titulo);font-weight:900;font-size:58px;line-height:.98;
                letter-spacing:-.03em;text-transform:uppercase">Juntos<br>por São Paulo.</p>
      <div style="height:6px;width:190px;margin-top:22px;border-radius:3px;
                  background:linear-gradient(90deg,var(--amarelo) 0 48%%,var(--branco) 48%% 100%%)"></div>
      <p style="margin-top:22px;font-size:17px;max-width:34ch;color:rgba(255,255,255,.92)">
        Coragem para proteger, preparado para cuidar.</p>
      <a href="#" style="display:inline-flex;align-items:center;gap:10px;margin-top:28px;padding:14px 24px;
                background:var(--branco);color:var(--verde-texto);font-family:var(--titulo);
                font-weight:900;font-size:15px;text-transform:uppercase;letter-spacing:.04em">
        @bombeiroflaviosantos</a>
    </div>
    <div style="text-align:right">
      <span style="display:block;font-family:var(--apoio);font-weight:900;font-size:12px;
                   letter-spacing:.24em;text-transform:uppercase;color:rgba(255,255,255,.82)">Deputado Estadual</span>
      <p style="font-family:var(--apoio);font-weight:900;font-size:132px;line-height:.9;
                letter-spacing:.01em">10193</p>
    </div>
  </div>
</div>
""")

# Direção C — Compromissos: o fecho recapitula as cinco bandeiras antes do número.
escreve("FechoC.dc.html", """
<div style="background:var(--navy);color:var(--branco);padding:72px 64px">
  <div style="max-width:1000px;margin:0 auto">
    <div style="display:grid;grid-template-columns:1fr .8fr;gap:52px;align-items:center">
      <div>
        <span class="chapeu" style="color:var(--amarelo)">O compromisso</span>
        <h2 style="font-size:38px;max-width:16ch">Cinco frentes, uma missão.</h2>
        <div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin-top:26px">
          %s
        </div>
      </div>
      <div style="text-align:center">
        <div style="background:linear-gradient(150deg,var(--verde-texto),#006B27);border-radius:20px;
                    padding:26px 30px;box-shadow:0 22px 50px rgba(0,0,0,.42)">
          <span style="display:block;font-family:var(--apoio);font-weight:900;font-size:11.5px;
                       letter-spacing:.24em;text-transform:uppercase">Deputado Estadual</span>
          <p style="font-family:var(--apoio);font-weight:900;font-size:78px;line-height:1;margin-top:4px">10193</p>
        </div>
        <p style="margin-top:20px;font-family:var(--titulo);font-weight:900;font-size:22px">Juntos por São Paulo.</p>
        <a href="#" style="display:inline-flex;align-items:center;gap:10px;margin-top:18px;padding:13px 22px;
                  border-radius:999px;background:var(--branco);color:var(--navy);font-weight:700;font-size:14.5px">
          @bombeiroflaviosantos</a>
      </div>
    </div>
  </div>
</div>
""" % "".join(
    '<div style="display:flex;align-items:center;gap:10px;padding:12px 14px;'
    'background:rgba(255,255,255,.06);border:1px solid var(--borda);border-radius:12px;'
    'font-size:14px">'
    '<span style="width:7px;height:7px;border-radius:2px;background:var(--amarelo);flex:none"></span>%s</div>' % b
    for b in ["Proteção das crianças", "Bombeiro Mirim", "Incentivo ao esporte",
              "Litoral com estrutura", "Escritório itinerante", "Valorização de quem protege"]))

print("\nartboards gerados em docs/design/")
