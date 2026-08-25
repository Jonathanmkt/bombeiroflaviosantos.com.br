# bombeiroflaviosantos.com.br

Site de **Flávio Henrique Pinto dos Santos, 10193** — candidato a Deputado Estadual por São Paulo
(Republicanos). Cliente da Idealis.

Desde 25/08/2026 este domínio é a **landing page completa** do candidato, substituindo a antiga
tela "em breve" de uma coluna só. A página tem sete blocos: herói (reproduzindo o carrossel de 3
posts da campanha) · "Quem sou eu" · frase de transição · as 5 bandeiras ("Pelo que eu luto") · o
Pacote de Valorização Policial/Bombeiro (10 propostas em 6 frentes) · fecho com contato e
Instagram · rodapé legal.

⚠️ **Risco de rótulo de anúncio ainda em pé.** O nome de campanha "Bombeiro Flávio Santos" e o
termo "bombeiro" aparecem na página. Esse mesmo termo já causou duas reprovações de rótulo de
anúncio (Meta/Google) em 20/08 e 23/08/2026 — ver `docs/HISTORICO.md`. O CEO decidiu manter o nome
de campanha mesmo assim; se o rótulo voltar a ser reprovado, é o mesmo problema recorrente, não um
bug novo.

**Este repositório não tem gêmeo.** `flaviosantos10193.com.br` segue em repositório próprio, com
conteúdo independente — alterar um não afeta o outro.

## Como está publicado

| | |
|---|---|
| **Hospedagem** | GitHub Pages, servindo a raiz da branch `main` |
| **Domínio** | `bombeiroflaviosantos.com.br`, declarado no arquivo `CNAME` |
| **DNS** | Cloudflare — os registros apontam para os IPs do GitHub Pages |
| **Registrador** | Registro.br (titular: o próprio cliente) |
| **HTTPS** | certificado emitido pelo GitHub; exige que o DNS resolva sem proxy da Cloudflare |

Publicar é empurrar para a `main` — não há build. O GitHub Pages leva de alguns segundos a poucos
minutos para refletir.

## Arquivos

```
index.html          a pagina inteira: HTML, CSS e conteudo, sem dependencia externa
assets/marca/       vetores da marca (assinatura, capacete, selo, onda, selo do partido),
                     extraidos de docs/referencias/praguinha.pdf
assets/fontes/      Transducer e TT Runs em WOFF2, subconjuntadas para pt-BR (90,9 KB no total)
assets/fotos/       retrato, corredor, ponte, ilustracao e ondas, em AVIF/WebP, 3 larguras cada
assets/js/site.js   sprite de icones Lucide, revela por IntersectionObserver, contagem animada,
                     barra de progresso de leitura, atalho do Instagram — 4 KB, sem dependencia
scripts/            geram assets a partir dos originais em MIDIA-VIRTUETECH (ver abaixo)
docs/               ACERVO-DE-CONTEUDO.md, BRIEFING-LANDING-PAGE.md, marca/MARCA.md, HISTORICO.md
CNAME               o dominio, exigido pelo GitHub Pages
```

## Mídia fora do git

Os originais pesados (manual de identidade visual, retrato oficial, fotos com fundo transparente,
ondas, ponte e as fontes com a licença do pacote) vivem em
`C:\Projetos\MIDIA-VIRTUETECH\clientes\flavio-santos\landing-page\bruto\`, fora deste repositório.
Os scripts em `scripts/` sabem buscar lá e avisam, em vez de falhar calado, quando a pasta não
existe.

## Decisões que não aparecem no código

- **Dois verdes de propósito.** O `#009C3B` do manual de marca reprova em contraste AA para texto
  pequeno (3,61:1). A página usa `--verde-texto: #00822F` (4,96:1) para texto; o verde do manual
  segue mandando em superfície, régua e marcador.
- **A imagem de fundo da ponte é um recorte do próprio carrossel da campanha**, sem arquivo
  original — está desbotada de propósito, como textura. Ao chegar o original, é trocar um arquivo.
- **As ondas do herói foram desenhadas pelo CEO** e não encostam na base entre 42% e 50% da
  largura (193 colunas de pixel com o azul indo até embaixo) — hoje isso fica escondido atrás da
  foto, mas é sorte de enquadramento, não garantia.
- **A ilustração da criança é sintética (Gemini)** — o `alt` diz "Ilustração" de propósito, para
  não sugerir uma pessoa real.
- Sem JavaScript a página permanece toda visível: um `<noscript>` desfaz a opacidade zero usada
  pelo revela por rolagem.

## De onde veio cada informação da página

| Afirmação | Fonte |
|---|---|
| Candidato a Deputado Estadual, Republicanos | Convenção do partido, noticiada por A Tribuna, Costa Norte e BS9 (01–03/08/2026) |
| Bombeiro / guarda-vidas de Praia Grande | Mesmas reportagens + perfil `@bombeiroflaviosantos` |
| "Sou Brasil. Sou São Paulo. Sou Republicanos." | Frase do próprio candidato, recorrente nas publicações dele |
| As 5 bandeiras e o Pacote de Valorização Policial/Bombeiro | Artes da campanha (carrossel e material gráfico), transcritas em `docs/ACERVO-DE-CONTEUDO.md` |
| Paleta, tipografia e vetores da marca | `docs/referencias/praguinha.pdf` (vetor puro) e o manual de identidade visual |
| Titularidade do domínio | RDAP do Registro.br — Flavio Henrique Pinto dos Santos |
| Nome civil e CNPJ da campanha (rodapé, exigido pelo rótulo de anúncio Meta/Google) | Comprovante de inscrição da Receita Federal — CNPJ 68.461.977/0001-40, dígitos verificadores conferidos por cálculo |
