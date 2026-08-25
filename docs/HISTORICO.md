# Histórico do projeto — bombeiroflaviosantos.com.br

Diário append-only. Entrada mais recente no topo.

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
