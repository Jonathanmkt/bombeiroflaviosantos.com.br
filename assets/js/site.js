/* =============================================================================
   Bombeiro Flávio Santos · 10193 — comportamento

   Sem dependência externa, num IIFE só. Tudo aqui é enfeite com função: se o
   JavaScript não rodar, a página continua legível, navegável e com o número, as
   propostas e o rodapé legal no lugar — nada de conteúdo depende deste arquivo.

   Quem pede sossego (prefers-reduced-motion) recebe o resultado final de cara,
   sem transição e sem contagem.
   ========================================================================== */
(() => {
  'use strict';

  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const calmo = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- revela ao entrar na tela -------------------------------------------
     Quem já revelou sai da observação: o observador não fica pesando a rolagem
     pelo resto da visita. */
  const alvos = $$('[data-revela]');
  if (calmo || !('IntersectionObserver' in window)) {
    alvos.forEach(el => el.classList.add('vem'));
  } else {
    const olho = new IntersectionObserver((itens, obs) => {
      itens.forEach(i => {
        if (!i.isIntersecting) return;
        i.target.classList.add('vem');
        obs.unobserve(i.target);
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
    alvos.forEach(el => olho.observe(el));
  }

  /* --- barra de progresso da leitura -------------------------------------- */
  const barra = $('#progresso');
  if (barra) {
    const aoRolar = () => {
      const alcance = document.documentElement.scrollHeight - innerHeight;
      barra.style.transform = `scaleX(${alcance > 0 ? scrollY / alcance : 0})`;
    };
    addEventListener('scroll', aoRolar, { passive: true });
    aoRolar();
  }

  /* --- os números contam quando aparecem ----------------------------------
     O texto final já está no HTML; a contagem só o substitui enquanto roda, e
     o devolve intacto no fim. Assim o número certo aparece mesmo sem JS, e
     também para quem lê por leitor de tela (aria-hidden no elemento animado
     não serve aqui — o valor é o conteúdo). */
  const conta = (el) => {
    const alvo = parseFloat(el.dataset.conta);
    const texto = el.textContent;
    const casas = (el.dataset.casas | 0);
    const dur = 1100;
    const t0 = performance.now();
    const passo = (agora) => {
      const t = Math.min(1, (agora - t0) / dur);
      const suave = 1 - Math.pow(1 - t, 3);          // desacelera no fim
      el.textContent = (alvo * suave).toLocaleString('pt-BR', {
        minimumFractionDigits: casas, maximumFractionDigits: casas });
      if (t < 1) requestAnimationFrame(passo);
      else el.textContent = texto;                    // devolve o original
    };
    requestAnimationFrame(passo);
  };

  const numeros = $$('[data-conta]');
  if (!calmo && 'IntersectionObserver' in window && numeros.length) {
    const olhoN = new IntersectionObserver((itens, obs) => {
      itens.forEach(i => {
        if (!i.isIntersecting) return;
        conta(i.target);
        obs.unobserve(i.target);
      });
    }, { threshold: 0.6 });
    numeros.forEach(el => olhoN.observe(el));
  }

  /* --- atalho flutuante para o Instagram ----------------------------------
     Aparece depois que o herói sai de vista: antes disso o mesmo link já está
     na tela, e dois botões iguais ao mesmo tempo é ruído. */
  const flut = $('#instaFlut');
  const heroi = $('.heroi');
  if (flut && heroi && 'IntersectionObserver' in window) {
    new IntersectionObserver(([i]) => {
      flut.classList.toggle('vem', !i.isIntersecting);
    }, { threshold: 0 }).observe(heroi);
  }
})();
