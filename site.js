const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
const $ = (s, el = document) => el.querySelector(s);
const $$ = (s, el = document) => [...el.querySelectorAll(s)];

// WhatsApp links: number is set once in the layout (window.WA)
$$('.js-wa').forEach(a => {
  a.href = `https://wa.me/${window.WA}?text=${encodeURIComponent(a.dataset.msg || 'Hello!')}`;
  a.target = '_blank';
  a.rel = 'noopener';
});

// Mobile menu
const menuBtn = $('.menu-btn');
menuBtn?.addEventListener('click', () => {
  const open = document.body.classList.toggle('nav-open');
  menuBtn.setAttribute('aria-expanded', open);
  menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
});

// Language menu: closes on a click outside it or on Escape
const langDd = $('.lang-dd');
document.addEventListener('click', e => { if (langDd?.open && !langDd.contains(e.target)) langDd.open = false; });
document.addEventListener('keydown', e => { if (e.key === 'Escape' && langDd?.open) { langDd.open = false; langDd.querySelector('summary').focus(); } });

// Category / blog filter chips
$$('.js-filter').forEach(bar => bar.addEventListener('click', e => {
  const chip = e.target.closest('[data-filter]');
  if (!chip) return;
  bar.querySelectorAll('.chip').forEach(c => c.classList.toggle('on', c === chip));
  const f = chip.dataset.filter;
  let shown = 0;
  $$('.js-items > [data-cats]', bar.parentElement).forEach(el => {
    const hit = f === 'all' || el.dataset.cats.split(/\s+/).includes(f) || el.dataset.cats === f;
    el.hidden = !hit;
    shown += hit;
  });
  $('.empty', bar.parentElement).hidden = shown > 0;
}));

// Form validation with the copy from UX-COPY.md. Returns true when the form is valid.
function validate(form) {
  let first = null;
  $$('[data-err]', form).forEach(input => {
    input.classList.remove('invalid');
    input.parentElement.querySelector('.err')?.remove();
    const pastDate = input.type === 'date' && input.value && new Date(input.value) < new Date(new Date().toDateString());
    if (!input.checkValidity() || pastDate) {
      input.classList.add('invalid');
      input.insertAdjacentHTML('afterend', `<span class="err" role="alert">${input.dataset.err}</span>`);
      first ??= input;
    }
  });
  first?.focus();
  return !first;
}

// Quote forms. Prototype only: in WordPress, Fluent Forms sends the email.
$$('.js-form').forEach(form => form.addEventListener('submit', e => {
  e.preventDefault();
  if (validate(form)) location.href = form.getAttribute('action');
}));

// ---------------------------------------------------------------- 1. descent into the cellar
$$('.descent').forEach(d => {
  if (reduceMotion) return; // stays a plain list of facts
  d.classList.add('live');
  const facts = $$('.d-fact', d), depth = $('.d-depth', d);
  let queued = false;
  const update = () => {
    queued = false;
    const r = d.getBoundingClientRect();
    const p = Math.min(1, Math.max(0, -r.top / (r.height - innerHeight)));
    d.style.setProperty('--p', p.toFixed(3));
    depth.textContent = p > 0.01 ? `−${Math.round(p * 80)} m` : '0 m';
    const active = Math.min(facts.length - 1, Math.floor(p * facts.length * 1.05));
    facts.forEach((f, i) => f.classList.toggle('on', i === active));
  };
  addEventListener('scroll', () => { if (!queued) { queued = true; requestAnimationFrame(update); } }, { passive: true });
  addEventListener('resize', update);
  update();
});

// ---------------------------------------------------------------- 2. illustrated map of Moldova
$$('.js-map').forEach(map => {
  const svg = $('.mdmap', map);
  const legend = $('.legend', map);
  const mobile = () => matchMedia('(max-width: 980px)').matches;
  const select = (key, reveal) => {
    const badge = key && $(`.badge[data-dest="${key}"]`, svg);
    if (badge && zoomed && !inBox(badge)) setZoom(false); // a place outside the zoomed area: show the whole country
    $$('[data-dest]', map).forEach(el => el.classList.toggle('on', !!key && el.dataset.dest === key));
    $$('.dest-panel', map).forEach(p => { p.hidden = p.dataset.dest !== (key || ''); });
    if (key && map.classList.contains('js-hash')) history.replaceState(null, '', '#' + key);
    // on phones the list is a horizontal carousel: centre the chosen place in it (no vertical jump)
    const item = $(`.legend [data-dest="${key}"]`, map);
    if (item && legend.scrollWidth > legend.clientWidth)
      legend.scrollLeft = item.parentElement.offsetLeft - legend.offsetLeft - (legend.clientWidth - item.offsetWidth) / 2; // instant: a smooth one gets cancelled by the page scroll below
    // ...and bring the details just into view
    if (reveal && mobile())
      $(`.dest-panel[data-dest="${key}"]`, map)?.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'nearest' });
  };
  // a tap anywhere near a point picks the nearest visible one: small points are hard to hit with a finger
  svg.addEventListener('click', e => {
    const ctm = svg.getScreenCTM();
    if (!ctm) return;
    const p = new DOMPoint(e.clientX, e.clientY).matrixTransform(ctm.inverse());
    let best = null, bestD = Infinity;
    $$('.badge', svg).forEach(b => {
      if (getComputedStyle(b).pointerEvents === 'none') return; // hidden by the filter
      const [x, y] = b.dataset.xy.split(',').map(Number);
      const d = Math.hypot(x - p.x, y - p.y);
      if (d < bestD) { bestD = d; best = b; }
    });
    if (best && bestD < (zoomed ? 20 : 40)) select(best.dataset.dest, true);
  });
  // zoom on the crowded Chișinău area: the viewBox glides between the whole country and the box built into the page
  const zoomBtn = $('.map-zoom', map);
  const whole = svg.getAttribute('viewBox').split(' ').map(Number), box = svg.dataset.zoom.split(' ').map(Number);
  let zoomed = false, anim;
  const inBox = b => { const [x, y] = b.dataset.xy.split(',').map(Number); return x > box[0] && y > box[1] && x < box[0] + box[2] && y < box[1] + box[3]; };
  const setZoom = on => {
    zoomed = on;
    map.classList.toggle('zoomed', on);
    zoomBtn.setAttribute('aria-pressed', on);
    $('span', zoomBtn).textContent = on ? 'Show all of Moldova' : 'Zoom in on Chișinău';
    const from = svg.getAttribute('viewBox').split(' ').map(Number), to = on ? box : whole, t0 = performance.now(), dur = reduceMotion ? 0 : 450;
    cancelAnimationFrame(anim);
    const step = now => {
      const k = dur ? Math.min(1, (now - t0) / dur) : 1, ease = 1 - (1 - k) ** 3;
      svg.setAttribute('viewBox', from.map((v, i) => (v + (to[i] - v) * ease).toFixed(1)).join(' '));
      if (k < 1) anim = requestAnimationFrame(step);
    };
    anim = requestAnimationFrame(step);
  };
  zoomBtn.addEventListener('click', () => setZoom(!zoomed));
  // the list (legend) and anything else outside the drawing
  map.addEventListener('click', e => {
    const hit = e.target.closest('.legend [data-dest]');
    if (hit) select(hit.dataset.dest, true);
  });
  map.addEventListener('keydown', e => {
    const b = e.target.closest('.badge');
    if (b && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); select(b.dataset.dest, true); }
  });
  // SVG has no z-index: move the badge under the mouse (or keyboard focus) to the top so its label stays readable
  const toTop = b => { if (b && b.nextElementSibling) b.parentNode.appendChild(b); };
  map.addEventListener('pointerover', e => { if (e.pointerType === 'mouse') toTop(e.target.closest?.('.badge')); });
  map.addEventListener('focusin', e => toTop(e.target.closest?.('.badge')));
  // filter: all places / wineries / monasteries & sights (CSS dims the rest and swaps the legend)
  $$('.map-filter [data-show]', map).forEach(b => b.addEventListener('click', () => {
    map.dataset.show = b.dataset.show;
    $$('.map-filter .chip', map).forEach(c => c.classList.toggle('on', c === b));
  }));
  const fromHash = location.hash.slice(1);
  if (fromHash && $(`.badge[data-dest="${fromHash}"]`, map)) select(fromHash);
});

// tour photos on phones: the dot under the gallery follows the swipe
$$('.gallery-wrap').forEach(w => {
  const g = $('.gallery', w), dots = $$('.g-dots i', w);
  if (!dots.length) return;
  const sync = () => { const i = Math.round(g.scrollLeft / (g.clientWidth || 1)); dots.forEach((d, n) => d.classList.toggle('on', n === i)); };
  g.addEventListener('scroll', sync, { passive: true });
  sync();
});

// ---------------------------------------------------------------- 3. trip builder
const builder = $('.js-builder');
if (builder) {
  const root = $('.js-builder-root');
  const data = JSON.parse($('#trip-data').textContent);
  const pax = $('#b-pax'), days = $('#b-days');
  const steps = $$('.bstep', builder);

  const go = n => {
    steps.forEach(s => { s.hidden = +s.dataset.step !== n; });
    root.style.setProperty('--fill', (n - 1) / 3);
    $('.js-stepnum').textContent = `Step ${n} of 4`;
    if (n === 4) render();
    root.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth' });
    $(`.bstep[data-step="${n}"] legend`).setAttribute('tabindex', '-1');
    $(`.bstep[data-step="${n}"] legend`).focus({ preventScroll: true });
  };
  builder.addEventListener('click', e => {
    const b = e.target.closest('[data-go]');
    if (b) go(+b.dataset.go);
    const p = e.target.closest('[data-pax]');
    if (p) pax.value = Math.max(1, Math.min(40, (+pax.value || 1) + +p.dataset.pax));
  });
  $$('input[name="who"]', builder).forEach(r => r.addEventListener('change', () => { pax.value = r.value; }));
  const dayLabel = () => { $('.js-days-out').textContent = days.value === '1' ? '1 day' : `${days.value} days`; };
  days.addEventListener('input', dayLabel);
  dayLabel();

  const euro = n => '€' + n.toLocaleString('en');
  function plan() {
    const people = Math.max(1, +pax.value || 1);
    const d = +days.value;
    let wants = $$('input[name="interest"]:checked', builder).map(i => i.value);
    if (!wants.length) wants = ['wine', 'history', 'soviet', 'nature', 'villages', 'food'];
    const tripDays = d === 1 ? 1 : d - 1 - (d >= 4 ? 1 : 0); // arrival day, and a departure day on longer trips
    const ranked = data.tours
      .map(t => ({ t, score: t.tags.filter(x => wants.includes(x)).length }))
      .filter(x => x.score > 0)
      .sort((a, b) => b.score - a.score || a.t.order - b.t.order);
    const picks = [], used = new Set();
    for (const { t } of ranked) {
      if (picks.length === tripDays) break;
      if (!used.has(t.group)) { picks.push(t); used.add(t.group); }
    }
    const priceFor = t => (people > 6 ? null : t.prices.find(p => p.pax === people)?.eur ?? null);
    const priced = picks.map(priceFor);
    const pp = priced.reduce((s, x) => s + (x || 0), 0);
    const multi = wants.includes('wine') || wants.includes('food') ? data.multi['wine-and-gastronomy']
      : wants.includes('nature') || wants.includes('villages') ? data.multi['countryside-tour'] : data.multi['culturewineandgastronomytour'];
    return { people, d, wants, picks, priced, pp, unpriced: priced.some(x => x === null), multi, freeDays: tripDays - picks.length };
  }

  function render() {
    const p = plan();
    const rows = [];
    let n = 1;
    if (p.d > 1) rows.push(`<li class="free"><span class="day">Day ${n++}</span><h4>Arrive in Chișinău</h4><p class="small">We can arrange your airport transfer.</p></li>`);
    p.picks.forEach((t, i) => rows.push(`<li><span class="pimg" style="background-image:url('${t.img}')"></span>
      <div><span class="day">Day ${n++} · day trip</span><h4><a href="${t.url}" target="_blank">${t.title}</a></h4></div>
      <span class="pp">${p.priced[i] ? euro(p.priced[i]) + '<small>per person</small>' : '<small>price on request</small>'}</span></li>`));
    for (let i = 0; i < p.freeDays; i++) rows.push(`<li class="free"><span class="day">Day ${n++}</span><h4>Free day in Chișinău</h4><p class="small">Or ask us to add another tour.</p></li>`);
    if (p.d >= 4) rows.push(`<li class="free"><span class="day">Day ${n++}</span><h4>Departure</h4></li>`);
    const est = p.people > 6
      ? `<div><small>Estimated price</small><b>Group price</b><small>For 7+ travellers we send a group quote.</small></div>`
      : `<div><small>Estimated price for ${p.people} ${p.people === 1 ? 'traveller' : 'travellers'}</small><b>${euro(p.pp)} per person</b>
         <small>${euro(p.pp * p.people)} in total for the day trips${p.unpriced ? ' · tours marked “price on request” are quoted separately' : ''}</small></div>`;
    const tn = p.picks.some(t => t.transnistria)
      ? '<p class="note">ℹ️ Your trip includes Transnistria: check your government’s travel advice and bring your passport.</p>' : '';
    const alt = p.d >= 5 && p.multi
      ? `<div class="alt">Prefer everything arranged, hotels included? Our <a href="${p.multi.url}" target="_blank">${p.multi.title}</a> starts from ${euro(p.multi.price)} per person.</div>` : '';
    $('.b-result', builder).innerHTML = `<ol class="plan">${rows.join('')}</ol>
      <div class="est">${est}<span class="small" style="color:var(--on-dark-muted)">Private tours · licensed guide · transport included</span></div>${tn}${alt}`;
    $$('.plan li', builder).forEach((li, i) => { li.style.animationDelay = `${i * 70}ms`; });

    const month = $('#b-month').value || 'dates flexible';
    const summary = [`Travellers: ${p.people}`, `Days: ${p.d} (${month})`, `Interests: ${p.wants.join(', ')}`, '',
      ...p.picks.map((t, i) => `• ${t.title}${p.priced[i] ? ` (${euro(p.priced[i])} pp)` : ''}`),
      '', p.people > 6 ? 'Group quote requested' : `Estimate: ${euro(p.pp)} per person`].join('\n');
    $('.js-summary', builder).value = summary;
  }

  builder.addEventListener('submit', e => {
    e.preventDefault();
    if (!validate(builder)) return;
    try { sessionStorage.setItem('trip', $('.js-summary', builder).value); } catch {}
    if (reduceMotion) return (location.href = builder.getAttribute('action'));
    $('.pop-up').hidden = false;
    setTimeout(() => { location.href = builder.getAttribute('action'); }, 1400);
  });
}

// Tour page: the booking card price follows the traveller count (prices from the tour's price table)
const book = $('.book[data-prices]');
if (book) {
  const prices = JSON.parse(book.dataset.prices);
  const paxInput = $('#f-pax', book);
  const show = () => {
    const pax = Math.max(1, +paxInput.value || 1);
    const row = prices.find(p => p.pax === pax);
    $('.js-plabel', book).textContent = `Price for ${pax} ${pax === 1 ? 'traveller' : 'travellers'}`;
    $('.js-pp', book).textContent = row ? `€${row.eur}` : 'Group price';
    $('.js-ptotal', book).textContent = row
      ? `€${(row.eur * pax).toLocaleString('en')} in total. The bigger the group, the lower the price.`
      : 'For 7 or more travellers we send a group quote.';
    $$('.ptable [data-pax]').forEach(c => c.classList.toggle('on', +c.dataset.pax === pax));
  };
  paxInput.addEventListener('input', show);
  show();
}

// Thank-you page: show the trip they just sent
const summaryBox = $('.js-trip-summary');
if (summaryBox) {
  let trip = null;
  try { trip = sessionStorage.getItem('trip'); sessionStorage.removeItem('trip'); } catch {}
  if (trip) { $('pre', summaryBox).textContent = trip; summaryBox.hidden = false; }
}
