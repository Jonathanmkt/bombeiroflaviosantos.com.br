# Histórico do projeto — bombeiroflaviosantos.com.br

Diário append-only. Entrada mais recente no topo.

## 2026-08-26 — Proteção das crianças ganha dois números

**O quê:** o bloco "Proteção das crianças" passou a exibir dois números em vez de um. O
**5.015** (registros de desaparecimento por ano em SP) ocupa agora o lugar do número grande; o
**257** (crianças que não voltaram mais para casa) desceu para um segundo dado, menor, separado
por um filete amarelo, com uma única linha de fonte valendo para os dois. Corrigidos também dois
defeitos de CSS no mesmo bloco: o número 257 saía com 15px em vez de 58px porque a regra do texto
ao lado (`.criancas__segundo span`) também casava o `<span>` de dentro do número por
especificidade — resolvido com seletor de filho direto (`> span`); e número e texto ficavam em
alturas diferentes por estarem em `align-items:baseline` (que alinha pela primeira linha de um
texto de duas linhas) — trocado para `center`.

**Por quê:** sugestão do próprio candidato, trazida pelo CEO. O 257 sozinho é só o estoque de
crianças que não voltaram; o 5.015 dá a escala do problema (fluxo anual de registros, a maioria
resolvida). Substituir um pelo outro deixaria a peça factualmente errada — a legenda antiga dizia
"crianças desaparecidas", o que não vale para um registro que se resolve. Manter os dois preserva
a precisão e explica por que o aplicativo de alerta importa: ele atua na distância entre um número
e o outro. ⚠️ A fonte do 5.015 ainda não foi confirmada — o CEO forneceu o número, não a fonte; a
linha "Ministério da Justiça — Relatório 2025" foi mantida por suposição e pode estar errada se o
5.015 vier de outra fonte (ex. SSP-SP).

**Também nesta rodada:** `.gitignore` passou a excluir os artefatos pesados de `docs/design/` — a
exploração de direções visuais feita com a skill `/design` do Claude Code. O canvas montado (com o
editor embutido) e os `.dc.html` com fontes da marca em base64 não são servidos pelo site; ficam
versionados só `gera-artboards.py` e `canvas.json`, que reconstroem tudo.

**Conferido:** Chrome de verdade em 360, 414, 768, 1280 e 1440 px — sem rolagem horizontal,
console limpo, nenhuma requisição quebrada, zero reprovações de contraste, 24 de 24 blocos
revelando ao rolar e os números voltando ao valor original ao fim da contagem.

**Arquivos-chave:** `index.html` (bloco "Proteção das crianças"), `.gitignore`, `docs/design/`.

## 2026-08-25 — O "em breve" vira a landing page completa do candidato

**O quê:** `index.html` deixou de ser a tela única "em breve" e passou a ser uma landing page de
sete blocos: herói (reproduzindo o carrossel de 3 posts da campanha, com a linha de propaganda
eleitoral na vertical, por pedido do CEO) · "Quem sou eu" · frase de transição · as 5 bandeiras
("Pelo que eu luto") · o Pacote de Valorização Policial/Bombeiro (10 propostas em 6 frentes) ·
fecho com contato e Instagram · rodapé legal. Entraram junto: vetores da marca extraídos de
`docs/referencias/praguinha.pdf` (vetor puro, não redesenho) em `assets/marca/`; as fontes
Transducer e TT Runs convertidas para WOFF2 e subconjuntadas para pt-BR (90,9 KB no total,
escolhidas comparando largura de avanço de glifo contra as fontes embutidas no manual de marca);
fotos em AVIF/WebP em três larguras em `assets/fotos/`; e `assets/js/site.js` (4 KB, sem
dependência) com sprite de ícones Lucide, revela por `IntersectionObserver`, barra de progresso de
leitura e contagem animada dos números 257 e 7,5 milhões.

**Por quê:** o conteúdo e as artes da campanha já existiam; faltava a página que os organizasse.
A paleta do manual de marca (`#009C3B`) reprova em contraste AA para texto pequeno (3,61:1), por
isso a página usa um segundo verde (`#00822F`, 4,96:1) só para texto — o verde do manual continua
mandando em superfície, régua e marcador. A imagem de fundo da ponte não tem arquivo original: foi
recortada do próprio carrossel da campanha e desbotada de propósito, para servir de textura. As
ondas foram desenhadas pelo CEO e não encostam na base entre 42% e 50% da largura (193 colunas de
pixel) — hoje isso fica atrás da foto, mas é sorte de enquadramento. A ilustração da criança é
sintética (Gemini), com `alt` de propósito dizendo "Ilustração" para não sugerir pessoa real.

**Conferido:** Chrome de verdade (`playwright-core`, canal `chrome`) em 360, 414, 768, 1280, 1440
e 1920 px — sem rolagem horizontal, console limpo, nenhuma requisição quebrada. Contraste: zero
reprovações, bloco por bloco contra o fundo real, aplicando a regra de texto grande da WCAG. Sem
JavaScript: 0 blocos invisíveis (via `<noscript>`); com `prefers-reduced-motion`: 0 invisíveis e
número já no valor final. Peso da primeira carga: 268 KB (131 imagem, 82 fonte, 45 documento, 7
CSS, 4 JS). Revela: 24 de 24 blocos revelam ao rolar.

⚠️ **README ficou desatualizado até esta rodada** — descrevia a tela "em breve" de uma coluna; foi
reescrito nesta mesma entrada.

**Arquivos-chave:** `index.html`, `assets/marca/`, `assets/fontes/`, `assets/fotos/`,
`assets/js/site.js`, `docs/ACERVO-DE-CONTEUDO.md`, `docs/BRIEFING-LANDING-PAGE.md`,
`docs/marca/MARCA.md`, `README.md`.

## 2026-08-25 — Volta a ser site distinto: o conteúdo original de campanha volta ao ar

**O quê:** `index.html` foi restaurado para a versão anterior ao commit `93a2f1c` — a página
única e original deste domínio volta ao ar: nome de campanha "Bombeiro Flávio Santos", selo
"site em construção", o lema "Sou Brasil. Sou São Paulo. Sou Republicanos.", a lista de recordes
esportivos e o link do Instagram. O rodapé com o nome civil completo e o CNPJ da campanha
(68.461.977/0001-40) permanece — aquela é exigência de plataforma de anúncio e não mudou.

**Por quê:** ordem do CEO em 25/08/2026, em sessão direta — os dois domínios do candidato voltam
a ser sites distintos. Em 23/08 este domínio tinha passado a servir a mesma página do
`flaviosantos10193.com.br`, por causa da segunda reprovação do rótulo de anúncio. O
`flaviosantos10193.com.br` fica exatamente como está, com o conteúdo sem o termo "bombeiro" —
nada muda naquele repositório, e os dois deixam de ser gêmeos.

⚠️ **Consequência aceita conscientemente:** trazendo o nome de campanha de volta, este domínio
volta a estar sujeito à mesma reprovação de rótulo de anúncio de 20 e 23/08. O CEO foi avisado e
decidiu assim.

**Infra conferida pelo devops-infra na mesma rodada, sem alteração:** os dois domínios já estão
em zonas Cloudflare separadas, em DNS only, cada um apontando para o GitHub Pages do seu próprio
repositório, com certificado Let's Encrypt próprio e HTTPS forçado, sem page rules ou
redirecionamento cruzado. O que unia os dois era só o conteúdo.

**Conferido:** Chrome de verdade (`playwright-core`, canal `chrome`, servindo o diretório na
porta 8099) em 360, 414, 768 e 1280 px — transbordo 0, sem rolagem horizontal, console sem erro
nem aviso, nenhuma requisição quebrada (só `index.html` e `assets/flavio.jpg`, ambos 200),
`<title>` de volta a "Bombeiro Flávio Santos — em breve".

**Arquivos-chave:** `index.html`, `README.md`.

## 2026-08-23 — Segunda reprovação: a página virou a mesma do domínio novo, sem o nome de campanha

**O quê:** A página inteira foi substituída pela do `flaviosantos10193.com.br`. Saíram o nome de
campanha "Bombeiro Flávio Santos", a menção a bombeiro e guarda-vidas, o lema, a lista de
recordes esportivos e o link do Instagram — este último porque a URL do perfil
(`@bombeiroflaviosantos`) traria de volta o termo. Ficaram cargo, **nome civil completo como
título**, número de urna **10193**, partido/estado, e a linha de responsabilidade com o CNPJ da
campanha, que a correção de 20/08 tinha trazido e continua sendo exigência.

**Por quê:** o rótulo de anúncio foi reprovado **de novo**, mesmo com o nome civil e o CNPJ já no
rodapé desde 20/08. Decisão do CEO em 23/08/2026: publicar em domínio novo uma versão sem o termo
"bombeiro" e **apontar os dois domínios para a mesma página**, até a aprovação sair. O título
passou a ser o nome civil para que o revisor case o nome impresso com o do documento cadastrado
na conta de anúncios, sem interpretar.

⚠️ **Não é um site novo substituindo o antigo: são dois domínios servindo o mesmo arquivo.** Como
o GitHub Pages aceita um domínio personalizado por repositório, a página está duplicada aqui e em
`Jonathanmkt/flaviosantos10193.com.br`. A única diferença é o `CNAME` e as três URLs de
auto-referência. Alterar uma sem a outra faz os domínios divergirem em silêncio.

**Conferido:** Chrome de verdade (`playwright-core`, canal `chrome`) em 360, 414, 768 e 1280 px —
transbordo 0. Nenhuma ocorrência de "bombeir" em conteúdo renderizado: as três que restam no
arquivo são o próprio domínio, em `canonical`, `og:url` e `og:image`.

**Arquivos-chave:** `index.html`, `README.md`, `scripts/confere-visual.js` (novo).

## 2026-08-20 — Identificação de quem financia o anúncio (rótulo Meta/Google reprovado)

**O quê:** O rótulo de anúncio ("Pago por...") foi reprovado pela plataforma porque a página não
trazia nenhum nome civil — o rodapé só tinha o domínio, e o título só o nome de campanha. Entrou
no rodapé a linha de responsabilidade com "Flávio Henrique Pinto dos Santos" e o CNPJ da campanha
(68.461.977/0001-40), conferido no comprovante da Receita e validado pelos dígitos verificadores.
A linha usa `--texto-suave` em vez do cinza que já existia no rodapé, que ficava abaixo de AA.
**Por quê:** rótulo de anúncio de assunto social/eleição/política, na Meta e no Google, exige que
o revisor encontre o financiador em conteúdo renderizado da própria página. Conferido em Chrome
360 e 1280px: transbordo 0, sem rolagem horizontal, console limpo, contraste da linha 8,26:1.
**Arquivos-chave:** `index.html`, `README.md`.
