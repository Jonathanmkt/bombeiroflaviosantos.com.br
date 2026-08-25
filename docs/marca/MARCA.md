# Marca — Bombeiro Flávio Santos (10193)

Material pronto para a landing page. **Nada aqui foi desenhado por semelhança: tudo saiu da fonte
oficial**: a `praguinha.pdf`, em `../referencias/`, e o `ID Visual Bombeiro Flávio Santos.pdf`, que
por ser mídia pesada de cliente vive no acervo, em
`C:\Projetos\MIDIA-VIRTUETECH\clientes\flavio-santos\landing-page\bruto\`.

**A descoberta que muda o método:** a `praguinha.pdf` **não tem nenhuma imagem embutida — é vetor
puro**. O capacete, o logotipo e o número saíram como curvas, não como redesenho de foto. Nas artes
em JPEG o capacete tem cerca de 40 px de largura e seria impossível reproduzi-lo com fidelidade; do
PDF ele sai em qualquer tamanho, nítido.

---

## 1. Tipografia

O manual (página 5) fixa **três famílias**:

| Fonte | Papel | Estado no site |
|---|---|---|
| **Transducer** | título | ✅ 400 · 500 · 700 · 900 em `assets/fontes/` |
| **TT Runs** | apoio e número | ✅ 400 · 900 em `assets/fontes/` |
| **Montserrat** | texto corrido | ✅ Google Fonts, é só chamar |

**Qual arquivo de cada uma, e por quê.** Nada foi escolhido no olho: comparei a largura de avanço
dos glifos das fontes **embutidas no manual** com cada candidata do pacote baixado. Todas as
escolhidas deram **erro zero**.

| Precisava ser | É este arquivo | O 2º colocado erra |
|---|---|---|
| Transducer Regular | `transducer-normalregular.otf` — largura **normal** | condensed, 36% |
| TT Runs Regular | `TT Runs Trial Regular.ttf` | itálica, 0,3% |
| TT Runs Black | `TT Runs Trial Black.ttf` | *Black Outline* empata em métrica, mas é vazada — descartada pelo desenho |

**Seis arquivos convertidos**, em WOFF2 e subconjuntados para pt-BR — **90,9 KB somados**:

| Família | Original | WOFF2 | Corte |
|---|---|---|---|
| Transducer (4 pesos) | 60 a 67 KB cada | **15,0 a 16,4 KB** | –75% |
| TT Runs (2 pesos) | 87 a 89 KB cada | **13,9 e 14,2 KB** | –84% |

O `assets/fontes/fontes.css` traz os seis `@font-face` prontos, com `font-display: swap`.

**Conferido em Chrome de verdade:** todos os pesos usados com estado `loaded`, sem requisição
quebrada, e os acentuados do português (ç ã õ é í ú) desenhados nas duas famílias — nada de caixa
vazia. *(Trial de fonte às vezes vem sem acento; estas não vêm — conferido glifo a glifo no `cmap`
antes de converter.)*

**Regerar:** `python scripts/prepara-fontes.py`

⚠️ **Os arquivos da TT Runs são os builds de *trial*** — é o que o nome deles diz, e é o mesmo que
o manual de ID visual usou. Funcionam e têm o conjunto completo de acentos. **Trocar pelos
definitivos, quando chegarem, é pôr o arquivo no acervo e rodar o script de novo.**

⚠️ **Os OTF originais não estão no git** — vivem no acervo, em
`...\clientes\flavio-santos\landing-page\bruto\fontes\`, junto com o arquivo de licença que veio
no pacote. **A licença é tratada diretamente pelo CEO.**

⚠️ **Montserrat entra por Google Fonts, não por arquivo local.** É a fonte de texto corrido; a
Transducer é a de título.

⚠️ **O logotipo não depende disso.** As letras de "FLÁVIO SANTOS", "BOMBEIRO", "DEPUTADO ESTADUAL"
e "10193" estão **vetorizadas** nos SVGs deste diretório — são curvas, não texto. A assinatura fica
idêntica mesmo que o resto da página use Montserrat.

---

## 2. Paleta

Os quatro valores oficiais, como impressos no manual:

| Cor | HEX | CMYK | Papel |
|---|---|---|---|
| **Azul-marinho** | `#02174E` | C99 M100 Y45 K22 | fundo, texto sobre claro, a cor da marca |
| **Verde** | `#009C3B` | C97 M3 Y100 K0 | número, capacete, destaque |
| **Amarelo** | `#FFC708` | C0 M31 Y94 K0 | acento, régua, onda |
| **Azul vivo** | `#0744F4` | C91 M78 Y0 K0 | apoio — o manual usa em títulos de página |

⚠️ **A `praguinha.pdf` traz esses mesmos tons já convertidos de CMYK, e por isso **ligeiramente
diferentes**: `#16244C`, `#19A54B`, `#FEC929`. **Os SVGs deste diretório usam os valores do
manual**, não os do PDF — o manual é quem manda. A conversão está registrada no
`extrai-da-fonte.py`, e é uma linha de troca caso a campanha decida o contrário.

### Contraste medido (WCAG)

| Combinação | Razão | Veredito |
|---|---|---|
| branco sobre navy | **17,00:1** | ✅ AA e AAA |
| amarelo sobre navy | **10,87:1** | ✅ AA e AAA |
| navy sobre branco | **17,00:1** | ✅ AA e AAA |
| branco sobre azul vivo | **6,68:1** | ✅ AA |
| verde sobre navy · navy sobre verde | **4,71:1** | ✅ AA em texto normal |
| branco sobre verde · verde sobre branco | **3,61:1** | ⚠️ **só em texto grande** (24px+, ou 19px+ negrito) |
| **verde de texto `#00822F`** sobre branco, e branco sobre ele | **4,96:1** | ✅ AA — é o verde que a landing usa em texto pequeno |
| **amarelo sobre branco** | **1,56:1** | 🔴 **não usar em texto** — só em faixa ou forma |
| **azul vivo sobre navy** | **2,54:1** | 🔴 **não usar em texto** |

**A dupla de trabalho da página é navy + branco.** Verde e amarelo entram como destaque, não como
cor de leitura.

⚠️ **O verde da marca não serve para texto pequeno, e essa é a armadilha desta paleta.** `#009C3B`
dá 3,61:1 — reprova em AA abaixo de 24px, nos dois sentidos. A landing por isso tem **dois
verdes**: `#009C3B` manda em superfície, régua e marcador; **`#00822F` manda em texto**, e a
diferença entre os dois não se percebe a olho. Está em `tokens.css` como `--verde-texto`.

---

## 3. Os arquivos

📁 **Todos vivem em `assets/marca/`** — sob `assets/` porque o site os serve. Este diretório
(`docs/marca/`) guarda só a documentação e os dois scripts que os geram.

### Vetor — use estes por padrão

| Arquivo | O que é | Quando usar |
|---|---|---|
| `assinatura-cor.svg` | assinatura completa, tricolor | sobre fundo branco ou claro |
| `assinatura-branco.svg` | a mesma, toda branca | sobre navy, verde ou foto escura |
| `assinatura-navy.svg` | a mesma, toda navy | sobre amarelo, branco ou fundo claro |
| `capacete.svg` | só o capacete, verde | ícone, favicon, marca d'água, marcador de lista |
| `capacete-branco.svg` | só o capacete, branco | o mesmo, sobre fundo escuro |
| `selo-propaganda.svg` | a praguinha redonda inteira, **com a linha legal e o CNPJ** | peça de apoio |
| `onda.svg` | a onda amarela e verde | base do herói — a landing usa embutida, com `preserveAspectRatio="none"`, porque `<img>` de SVG não estica |
| `republicanos.svg` · `republicanos-branco.svg` | o selo do partido | assinatura do partido no herói |

**A assinatura tem 202,76 × 155,29 unidades no viewBox** — proporção ≈ 1,306:1. Escale pela
largura; nunca distorça.

### Raster — só onde SVG não serve

| Arquivo | Tamanho | Observação |
|---|---|---|
| `assinatura-cor.png` | 1200×919, fundo transparente | Open Graph, e-mail, WhatsApp |
| `assinatura-branco.png` | 1200×919, fundo transparente | idem, sobre escuro |
| `capacete.png` | 600×391, fundo transparente | fallback de ícone |
| `assinatura-horizontal.png` | 1077×279, fundo transparente | **versão horizontal — nome \| número.** Só existe em raster: veio de dentro do PDF de ID visual já rasterizada. Serve para topo estreito e cabeçalho fixo |

⚠️ **A versão horizontal é a única peça sem vetor.** Se a landing depender dela em tamanho grande,
peça o arquivo editável à campanha.

### Apoio

| Arquivo | O que é |
|---|---|
| `tokens.css` | as cores e as pilhas de fonte como variáveis CSS, já com o papel de cada cor |
| `PREVIEW.html` | folha de marca: todas as peças, a paleta, o contraste medido e a situação das fontes, numa página só. Abra no navegador |
| `gera-preview.py` | regenera o `PREVIEW.html` a partir dos SVGs |

### Como as peças foram extraídas

`extrai-da-fonte.py` — roda sobre a `praguinha.pdf` e regenera **todos** os SVGs. Ele existe para
que a extração não seja um passe de mágica de uma tarde: mudou a cor oficial, mudou a fonte,
apareceu uma praguinha nova? Ajusta e roda de novo.

```bash
python docs/marca/extrai-da-fonte.py
```

**Conferência feita:** o `selo-propaganda.svg` renderizado em Chrome, a 851 px, foi comparado pixel
a pixel com a mesma página do PDF renderizada no mesmo tamanho. **2,97% dos pixels diferem acima do
limiar de 40/255, distribuídos por igual em todas as faixas da imagem** — o padrão de antisserrilha
de borda, e não de peça deslocada ou faltando. A diferença de cor entre os dois (manual × PDF) fica
abaixo desse limiar em todos os três tons.

---

## 4. Regras de uso

1. **Área de respiro:** o menor espaço livre em volta da assinatura é a altura do capacete.
2. **Tamanho mínimo:** abaixo de ~120 px de largura o "DEPUTADO ESTADUAL" fecha. Nesse caso, use a
   versão horizontal ou só o capacete.
3. **Não recomponha a assinatura** — não troque a ordem, não mude a entrelinha, não substitua o
   capacete por outro ícone, não aplique sombra ou contorno.
4. **Sobre foto**, use a versão branca, e só onde o fundo for escuro o bastante para dar 4,5:1.
5. **O verde do número é parte da marca**, não é uma cor livre: na versão colorida ele é sempre
   verde; nas monocromáticas, a mesma cor de tudo.

---

## 5. Ponta solta

✅ **A foto deixou de ser buraco em 25/08/2026.** Chegaram o retrato oficial (2333×3500) e o
corredor **com fundo transparente** (1414×2000). As duas já estão preparadas para a web em
`../../assets/fotos/`, e o que fazer com cada uma está no `../BRIEFING-LANDING-PAGE.md`, seção 3.

**A ponta solta que sobrou é a licença das fontes** — item 1 acima. É decisão da campanha, e é a
única coisa que muda a tipografia da landing.
