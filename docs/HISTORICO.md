# Histórico do projeto — bombeiroflaviosantos.com.br

Diário append-only. Entrada mais recente no topo.

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
