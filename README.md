# bombeiroflaviosantos.com.br

Site de **Flávio Henrique Pinto dos Santos, 10193** — candidato a Deputado Estadual por São Paulo
(Republicanos). Cliente da Idealis.

⚠️ **Desde 25/08/2026 este domínio voltou a ser um site distinto de `flaviosantos10193.com.br`.**
A página original está de volta ao ar: nome de campanha "Bombeiro Flávio Santos", selo "site em
construção", o lema "Sou Brasil. Sou São Paulo. Sou Republicanos.", a lista de recordes
esportivos e o link do Instagram. O rodapé com o nome civil completo e o CNPJ da campanha
(68.461.977/0001-40) permanece — é exigência da plataforma de anúncio e não mudou.

**Por quê:** entre 23/08 e 25/08/2026 este domínio serviu a mesma página de
`flaviosantos10193.com.br`, sem o termo "bombeiro", por causa da reprovação do rótulo de anúncio
(ver `docs/HISTORICO.md`). Em 25/08/2026 o CEO decidiu que os dois domínios voltam a ser sites
distintos. **Consequência aceita conscientemente:** trazendo o nome de campanha de volta, este
domínio volta a estar sujeito à mesma reprovação de rótulo de anúncio de 20 e 23/08 — o CEO foi
avisado e decidiu assim mesmo.

**Este repositório não tem mais gêmeo.** `flaviosantos10193.com.br` segue em repositório próprio,
com o conteúdo sem o termo "bombeiro", e as duas páginas agora evoluem de forma independente —
alterar uma não afeta a outra.

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
