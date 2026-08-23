# bombeiroflaviosantos.com.br

Site de **Flávio Henrique Pinto dos Santos, 10193** — candidato a Deputado Estadual por São Paulo
(Republicanos). Cliente da Idealis.

⚠️ **Desde 23/08/2026 este domínio serve a MESMA página de `flaviosantos10193.com.br`**, e a
palavra "bombeiro" não aparece mais em nenhum conteúdo renderizado — só no próprio domínio, que
é o que o cliente possui.

**Por quê:** o rótulo de anúncio ("Pago por…", categoria "assuntos sociais, eleições ou política")
foi reprovado **duas vezes** nesta página. A primeira reprovação, corrigida em 20/08/2026, era
falta do nome civil e do CNPJ no rodapé. Depois da segunda, o CEO decidiu (23/08/2026) publicar
uma versão sem o nome de campanha "Bombeiro Flávio Santos" — só cargo, **nome civil completo** e
número — e apontar os dois domínios para ela.

**O conteúdo anterior** (lema, recordes esportivos, menção a guarda-vidas, link do Instagram)
está preservado no histórico do git, no commit anterior a esta troca.

⚠️ **A página vive duplicada em dois repositórios**, porque o GitHub Pages aceita um domínio
personalizado por repositório. O gêmeo é `Jonathanmkt/flaviosantos10193.com.br`, e a única
diferença entre os dois arquivos é o `CNAME` e as três URLs de auto-referência (`canonical`,
`og:url`, `og:image`). **Ao alterar esta página, altere as duas** — mudar só uma faz os domínios
divergirem em silêncio.

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
index.html        a página inteira: HTML, CSS e conteúdo, sem dependência externa
assets/flavio.jpg retrato do candidato
CNAME             o domínio, exigido pelo GitHub Pages
```

## ⚠️ Duas pendências conhecidas

1. **O retrato está em 150×150 px**, capturado do perfil público do Instagram — é o maior tamanho
   que o Instagram expõe. Ele é exibido em 132 px, então não aparenta baixa qualidade, **mas não
   serve para nenhum uso maior**. Ao receber a foto oficial do cliente, basta substituir
   `assets/flavio.jpg` — nada mais muda.
2. **O número de urna não está na página**, de propósito: ele não foi confirmado em fonte oficial
   até a publicação. Só entra depois de conferido no TSE ou com o cliente.

## De onde veio cada informação da página

| Afirmação | Fonte |
|---|---|
| Candidato a Deputado Estadual, Republicanos | Convenção do partido, noticiada por A Tribuna, Costa Norte e BS9 (01–03/08/2026) |
| Bombeiro / guarda-vidas de Praia Grande | Mesmas reportagens + perfil `@bombeiroflaviosantos` |
| "Sou Brasil. Sou São Paulo. Sou Republicanos." | Frase do próprio candidato, recorrente nas publicações dele |
| Recordes de corrida (168 km rua, 201 km esteira, Ironman) | Biografia do perfil oficial dele no Instagram |
| Titularidade do domínio | RDAP do Registro.br — Flavio Henrique Pinto dos Santos |
| Nome civil e CNPJ da campanha (rodapé, exigido pelo rótulo de anúncio Meta/Google) | Comprovante de inscrição da Receita Federal — CNPJ 68.461.977/0001-40, dígitos verificadores conferidos por cálculo |
