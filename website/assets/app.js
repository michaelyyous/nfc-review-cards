/* ============================================================
   Site behaviour.
   Brand name lives in ONE place — see BRAND below.
   ============================================================ */

const BRAND = {
  name: '',              // ← Sæt navnet her. Tomt = pladsholder vises.
  placeholder: 'Firmanavn',
  cvr: '',               // ← CVR-nummer
  email: '',             // ← support-mail
  city: 'Danmark',
};

/* Shopify som ren kasseapparat: sitet bliver hvor det er, og "Gå til betaling"
   sender kurven videre via et cart-permalink. Udfyld de to felter, så skifter
   bestillingsformularen automatisk fra mail til rigtig checkout.

   variantId findes i Shopify under Produkter → dit produkt → Varianter.
   Det er tallet sidst i URL'en, fx .../variants/45678901234567
   Mængderabatten sættes op i Shopify under Rabatter → Automatisk rabat. */
const SHOPIFY = {
  domain: '',            // ← fx 'dit-shop.myshopify.com'
  variantId: '',         // ← fx '45678901234567'
};

/* Fragt. Pakkeshop er gratis uanset ordrestørrelse; hjemmelevering koster. */
const SHIPPING = {
  pakkeshop: 0,
  hjem: 49,
};

document.documentElement.classList.add('js');
window.BRAND = BRAND;

/* ---------- Brand injection ---------- */
(() => {
  const shown = BRAND.name || BRAND.placeholder;
  const empty = !BRAND.name;

  document.querySelectorAll('[data-brand]').forEach(el => {
    el.textContent = shown;
    if (empty) el.setAttribute('data-brand-empty', '');
  });
  document.querySelectorAll('[data-cvr]').forEach(el => {
    el.textContent = BRAND.cvr || '—';
  });
  document.querySelectorAll('[data-email]').forEach(el => {
    const v = BRAND.email || 'support@…';
    el.textContent = v;
    if (BRAND.email && el.tagName === 'A') el.href = `mailto:${BRAND.email}`;
  });

  if (empty) {
    const s = document.createElement('style');
    s.textContent = `[data-brand-empty]{
      background: color-mix(in srgb, var(--gold) 22%, transparent);
      box-shadow: 0 0 0 2px color-mix(in srgb, var(--gold) 30%, transparent);
      border-radius: 4px; padding-inline: .18em;
    }`;
    document.head.appendChild(s);
  }

  const t = document.title;
  if (t.includes('{brand}')) document.title = t.replace('{brand}', shown);
})();

/* ---------- Mobile nav ---------- */
(() => {
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.nav');
  if (!burger || !nav) return;

  const set = open => {
    burger.setAttribute('aria-expanded', String(open));
    nav.dataset.open = String(open);
  };
  burger.addEventListener('click', () => set(burger.getAttribute('aria-expanded') !== 'true'));
  nav.addEventListener('click', e => { if (e.target.tagName === 'A') set(false); });
  addEventListener('keydown', e => { if (e.key === 'Escape') set(false); });
  matchMedia('(min-width: 901px)').addEventListener('change', e => { if (e.matches) set(false); });
})();

/* ---------- Accordion ---------- */
document.querySelectorAll('.acc__btn').forEach(btn => {
  const panel = btn.nextElementSibling;
  btn.addEventListener('click', () => {
    const open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!open));
    panel.dataset.open = String(!open);
  });
});

/* ---------- Reveal on scroll ---------- */
(() => {
  const items = document.querySelectorAll('[data-reveal]');
  if (!items.length) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
    items.forEach(el => el.classList.add('is-in'));
    return;
  }
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const delay = Number(el.dataset.reveal) || 0;
      el.style.transitionDelay = `${delay}ms`;
      el.classList.add('is-in');
      io.unobserve(el);
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
  items.forEach(el => io.observe(el));
})();

/* ===========================================================================
   Spring — parameterised the way Apple parameterises them, not as
   mass/stiffness/damping.

     dampingRatio  1.0  = critically damped, settles with no overshoot
                  ~0.8  = slight overshoot, for momentum-carrying gestures
     response       seconds to reach the target. NOT a duration — a spring
                    has no fixed duration; settle time emerges from the maths.

   Always animates from its current value, so re-targeting mid-flight is
   continuous and velocity carries through instead of hard-cutting.
   =========================================================================== */
class Spring {
  constructor(value, { damping = 1.0, response = 0.4 } = {}) {
    this.value = value;
    this.target = value;
    this.velocity = 0;
    this.setParams({ damping, response });
  }
  setParams({ damping, response }) {
    this.zeta = damping;
    this.omega = (2 * Math.PI) / response;
  }
  /** Re-target without losing velocity — this is what prevents the
   *  "brick wall" when a gesture reverses mid-animation. */
  retarget(target, velocity) {
    this.target = target;
    if (velocity !== undefined) this.velocity = velocity;
  }
  step(dt) {
    // Clamp dt so a backgrounded tab can't explode the integration on return.
    dt = Math.min(dt, 1 / 30);
    const k = this.omega * this.omega;
    const c = 2 * this.zeta * this.omega;
    const a = -k * (this.value - this.target) - c * this.velocity;
    this.velocity += a * dt;
    this.value += this.velocity * dt;
    return this.value;
  }
  get settled() {
    return Math.abs(this.velocity) < 0.4 && Math.abs(this.value - this.target) < 0.15;
  }
}

/** Apple's momentum projection from Designing Fluid Interfaces.
 *  Exponential decay — NOT the textbook v²/(2a). Answers: where would this
 *  come to rest if I let go now? */
function projectMomentum(velocity, decelerationRate = 0.998) {
  return (velocity / 1000) * decelerationRate / (1 - decelerationRate);
}

/* ---------- The 3D card ----------------------------------------------------
   · feedback on pointer-down, not release
   · ~10px hysteresis before committing to a drag
   · 1:1 tracking via setPointerCapture, so it keeps up outside the bounds
   · velocity history, not a single delta, so release velocity is honest
   · momentum projected forward, then snapped to the nearest face
   · release velocity handed to the spring — no seam between drag and animate
   · fully interruptible: grabbing mid-flight continues from the live value
   · rubber-banding on X instead of a hard stop
   · X and Y are independent springs — a 2D spring desyncs
   No CSS transition on the transform: it would fight the physics.
--------------------------------------------------------------------------- */
(() => {
  const wrap = document.querySelector('[data-card3d]');
  if (!wrap) return;

  const card   = wrap.querySelector('.card3d');
  const shadow = wrap.querySelector('.card3d__shadow');
  const hint   = document.querySelector('[data-card3d-hint]');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');

  const REST_RX  = 8;
  const RX_LIMIT = 58;          // past this, resistance instead of a wall
  const DEG_PER_PX_Y = 0.42;    // horizontal drag → yaw
  const DEG_PER_PX_X = 0.34;    // vertical drag  → pitch
  const HYSTERESIS = 10;        // px before we commit to a drag

  // Two independent springs. A single 2D spring desyncs when the axes carry
  // different velocities, so pitch and yaw are separate.
  //   pitch: repositioning → critically damped, no overshoot
  //   yaw:   momentum-carrying → slight bounce, because a flick preceded it
  const sx = new Spring(REST_RX, { damping: 1.0, response: 0.4 });
  const sy = new Spring(-22,     { damping: 0.8, response: 0.4 });

  let dragging = false, committed = false, pointerId = null;
  let startX = 0, startY = 0, lastX = 0, lastY = 0;
  let history = [];             // recent {t, ry, rx} for an honest release velocity
  let lastFrame = performance.now();
  let idlePhase = 0, idleAmp = 0;
  let snappedFace = null;

  const rubber = (overshoot, dim, c = 0.55) =>
    (overshoot * dim * c) / (dim + c * Math.abs(overshoot));

  const clampRx = v =>
    v >  RX_LIMIT ?  RX_LIMIT + rubber(v - RX_LIMIT, 90) :
    v < -RX_LIMIT ? -RX_LIMIT + rubber(v + RX_LIMIT, 90) : v;

  /** Velocity in deg/s over a short trailing window — a single frame delta is
   *  noisy and produces a release that doesn't match what the hand did. */
  function releaseVelocity(key) {
    const now = performance.now();
    const recent = history.filter(s => now - s.t < 90);
    if (recent.length < 2) return 0;
    const a = recent[0], b = recent[recent.length - 1];
    const dt = (b.t - a.t) / 1000;
    return dt > 0 ? (b[key] - a[key]) / dt : 0;
  }

  function paint(ry, rx) {
    card.style.setProperty('--rx', rx.toFixed(2) + 'deg');
    card.style.setProperty('--ry', ry.toFixed(2) + 'deg');

    const yr = ((ry % 360) + 360) % 360;
    const rad = yr * Math.PI / 180;
    // The light source stays fixed in the room, so the glare travels across
    // the surface as the card turns rather than being painted onto it.
    card.style.setProperty('--glare-angle', (114 + yr * 0.55).toFixed(1) + 'deg');
    card.style.setProperty('--glare-a', (0.16 + 0.2 * Math.abs(Math.cos(rad))).toFixed(3));

    const face = Math.abs(Math.cos(rad));
    shadow.style.setProperty('--shadow-s', (0.62 + 0.38 * face).toFixed(3));
    shadow.style.setProperty('--shadow-o', (0.34 + 0.5 * face).toFixed(3));
  }

  function frame(now) {
    try {
      const dt = Math.max(0.001, (now - lastFrame) / 1000);
      lastFrame = now;

      let ry = sy.value, rx = sx.value;

      if (!dragging) {
        ry = sy.step(dt);
        rx = clampRx(sx.step(dt));

        // Haptic + visual commit land on the same frame, never staggered.
        if (snappedFace !== null && sy.settled) {
          if (navigator.vibrate && matchMedia('(pointer: coarse)').matches) navigator.vibrate(8);
          snappedFace = null;
        }

        // A resting object shouldn't look dead. This is a render-time offset,
        // not spring state, so the physics stay clean. ~0.07 Hz — well clear of
        // the vestibular band, tiny amplitude, and off under reduced motion.
        if (!reduce.matches) {
          idleAmp = Math.min(1, idleAmp + dt * 0.35);
          idlePhase += dt;
          ry += Math.sin(idlePhase * 0.44) * 1.5 * idleAmp;
          rx += Math.cos(idlePhase * 0.33) * 0.9 * idleAmp;
        }
      }

      paint(ry, rx);
    } catch (err) {
      console.error('card3d frame:', err);
    }
    requestAnimationFrame(frame);
  }

  wrap.addEventListener('pointerdown', e => {
    dragging = true;
    committed = false;
    pointerId = e.pointerId;
    try { wrap.setPointerCapture(pointerId); } catch (_) {}

    // Grabbing mid-flight continues from the live on-screen value — never the
    // target — so there's no jump, and it kills momentum so the object is ours.
    sy.retarget(sy.value, 0);
    sx.retarget(sx.value, 0);

    startX = lastX = e.clientX;
    startY = lastY = e.clientY;
    history = [{ t: performance.now(), ry: sy.value, rx: sx.value }];
    idleAmp = 0;
    wrap.dataset.grabbing = 'true';       // feedback on pointer-DOWN
    if (hint) hint.dataset.hidden = 'true';
    e.preventDefault();
  });

  wrap.addEventListener('pointermove', e => {
    if (!dragging || e.pointerId !== pointerId) return;

    // Hysteresis: don't commit to a drag until the intent is unambiguous.
    if (!committed) {
      if (Math.hypot(e.clientX - startX, e.clientY - startY) < HYSTERESIS) return;
      committed = true;
      lastX = e.clientX; lastY = e.clientY;
    }

    // 1:1 with the pointer. The value IS the spring's value — no lag layer.
    sy.value += (e.clientX - lastX) * DEG_PER_PX_Y;
    sx.value  = clampRx(sx.value - (e.clientY - lastY) * DEG_PER_PX_X);
    sy.target = sy.value;
    sx.target = sx.value;

    lastX = e.clientX; lastY = e.clientY;
    history.push({ t: performance.now(), ry: sy.value, rx: sx.value });
    if (history.length > 8) history.shift();
  });

  const release = e => {
    if (!dragging || (e && e.pointerId !== pointerId)) return;
    dragging = false;
    wrap.dataset.grabbing = 'false';
    try {
      if (pointerId !== null && wrap.hasPointerCapture(pointerId)) wrap.releasePointerCapture(pointerId);
    } catch (_) {}
    pointerId = null;

    if (!committed) { idleAmp = 0; return; }   // a tap, not a throw

    let vy = releaseVelocity('ry');
    let vx = releaseVelocity('rx');
    vy = Math.max(-1500, Math.min(1500, vy));
    vx = Math.max(-900,  Math.min(900,  vx));

    // Project where the momentum would carry it, THEN pick the nearest face.
    // Snapping from the release point instead would ignore the throw entirely.
    const projected = sy.value + projectMomentum(vy);
    const targetFace = Math.round(projected / 180) * 180;

    sy.retarget(targetFace, vy);   // velocity handed over — no seam
    sx.retarget(REST_RX, vx);
    snappedFace = targetFace;
    idleAmp = 0;
  };
  wrap.addEventListener('pointerup', release);
  wrap.addEventListener('pointercancel', release);

  // Hover parallax: a gentle re-target, not a takeover. Fine pointers only.
  if (matchMedia('(hover: hover) and (pointer: fine)').matches && !reduce.matches) {
    wrap.addEventListener('pointermove', e => {
      if (dragging) return;
      const r = wrap.getBoundingClientRect();
      const nx = (e.clientX - r.left) / r.width - 0.5;
      const ny = (e.clientY - r.top) / r.height - 0.5;
      const face = Math.round(sy.value / 180) * 180;
      sy.target = face + nx * 16;
      sx.target = REST_RX - ny * 14;
    });
    wrap.addEventListener('pointerleave', () => {
      if (dragging) return;
      sy.target = Math.round(sy.value / 180) * 180;
      sx.target = REST_RX;
    });
  }

  // Reachable without a pointer.
  wrap.tabIndex = 0;
  wrap.setAttribute('role', 'img');
  wrap.setAttribute('aria-label',
    'Anmeldelseskort i 3D. Piletaster drejer det, mellemrum vender det om.');
  wrap.addEventListener('keydown', e => {
    const keys = {
      ArrowLeft:  () => sy.retarget(sy.target - 45),
      ArrowRight: () => sy.retarget(sy.target + 45),
      ArrowUp:    () => sx.retarget(Math.max(-RX_LIMIT, sx.target - 15)),
      ArrowDown:  () => sx.retarget(Math.min( RX_LIMIT, sx.target + 15)),
      ' ':        () => sy.retarget(Math.round(sy.value / 180) * 180 + 180),
      Enter:      () => sy.retarget(Math.round(sy.value / 180) * 180 + 180),
    };
    const fn = keys[e.key];
    if (!fn) return;
    fn(); idleAmp = 0; e.preventDefault();
    if (hint) hint.dataset.hidden = 'true';
  });

  paint(sy.value, sx.value);
  requestAnimationFrame(frame);
})();

/* ---------- Quantity → price calculator ---------- */
(() => {
  const root = document.querySelector('[data-calc]');
  if (!root) return;

  const TIERS = JSON.parse(root.dataset.calc);           // [{min, price}] ex. moms
  const input = root.querySelector('[data-calc-qty]');
  const outUnit = root.querySelector('[data-calc-unit]');
  const outTotal = root.querySelector('[data-calc-total]');
  const outVat = root.querySelector('[data-calc-vat]');

  const kr = n => n.toLocaleString('da-DK', { minimumFractionDigits: 0, maximumFractionDigits: 2 });
  const unitFor = q => TIERS.reduce((acc, t) => (q >= t.min ? t.price : acc), TIERS[0].price);

  const render = () => {
    const q = Math.max(1, Math.min(5000, Number(input.value) || 1));
    const u = unitFor(q);
    const total = u * q;
    outUnit.textContent = kr(u);
    outTotal.textContent = kr(total);
    if (outVat) outVat.textContent = kr(total * 1.25);
  };
  input.addEventListener('input', render);
  root.querySelectorAll('[data-calc-set]').forEach(b => {
    b.addEventListener('click', () => { input.value = b.dataset.calcSet; render(); });
  });
  render();
})();

/* ---------- Chrome gains weight once content passes under it ----------
   On pages with a dark hero block the nav sits *on* that block and stays
   transparent. It only becomes light translucent chrome once the block has
   actually scrolled past — switching on scrollY alone would put pale text
   on a dark background for the whole height of the hero. */
(() => {
  const bar = document.querySelector('.topbar');
  if (!bar) return;
  const hero = document.querySelector('.heroblock');
  let ticking = false;

  const update = () => {
    ticking = false;
    bar.dataset.scrolled = String(
      hero ? hero.getBoundingClientRect().bottom <= bar.offsetHeight : scrollY > 8
    );
  };
  addEventListener('scroll', () => {
    if (!ticking) { ticking = true; requestAnimationFrame(update); }
  }, { passive: true });
  addEventListener('resize', update, { passive: true });
  update();
})();

/* ---------- Order form ------------------------------------------------------
   Interim ordering flow until Shopify checkout is wired up. Takes no payment —
   it composes the order and hands it to the customer's mail client, so it
   works with no backend and no account. Swap ORDER_ENDPOINT below for a POST
   URL (Shopify, Formspree, whatever) and it submits there instead.
--------------------------------------------------------------------------- */
const ORDER_ENDPOINT = '';   // ← tom = send via mailklient

(() => {
  const form = document.querySelector('[data-order]');
  if (!form) return;

  const TIERS = JSON.parse(form.dataset.tiers);
  const VAT = 0.25;

  const qtyInput = form.querySelector('[data-qty]');
  const presets  = form.querySelectorAll('[data-qty-set]');
  const linkWrap = form.querySelector('[data-link-wrap]');
  const shipRadios = form.querySelectorAll('[data-ship]');

  const shipMode = () => (form.querySelector('[data-ship]:checked') || {}).value || 'pakkeshop';
  const shipCost = () => SHIPPING[shipMode()] ?? 0;

  const out = {
    qty:   form.querySelector('[data-sum-qty]'),
    unit:  form.querySelector('[data-sum-unit]'),
    ship:  form.querySelector('[data-sum-ship]'),
    total: form.querySelector('[data-sum-total]'),
    ex:    form.querySelector('[data-sum-ex]'),
    save:  form.querySelector('[data-sum-save]'),
  };

  const kr = n => n.toLocaleString('da-DK', { maximumFractionDigits: 2 });
  const unitFor = q => TIERS.reduce((acc, t) => (q >= t.min ? t.price : acc), TIERS[0].price);
  const clampQty = () => Math.max(1, Math.min(5000, Number(qtyInput.value) || 1));

  function render() {
    const q = clampQty();
    const unit = unitFor(q);
    const goods = unit * q;
    const ship = shipCost();
    const total = goods + ship;

    out.qty.textContent = q;
    out.unit.textContent = kr(unit);
    out.ship.textContent = ship === 0 ? 'Gratis' : kr(ship) + ' kr';
    out.total.textContent = kr(total);
    out.ex.textContent = `heraf moms ${kr(total - total / (1 + VAT))} kr · ekskl. moms ${kr(total / (1 + VAT))} kr`;

    const saved = (TIERS[0].price - unit) * q;
    out.save.textContent = saved > 0 ? `Du sparer ${kr(saved)} kr i forhold til enkeltstykspris` : '';

    presets.forEach(b => b.classList.toggle('is-on', Number(b.dataset.qtySet) === q));
  }

  qtyInput.addEventListener('input', render);
  presets.forEach(b => b.addEventListener('click', () => { qtyInput.value = b.dataset.qtySet; render(); }));
  shipRadios.forEach(r => r.addEventListener('change', render));

  // The link field only matters if we're doing the programming.
  form.querySelectorAll('[data-prog]').forEach(radio => {
    radio.addEventListener('change', () => {
      const needsLink = form.querySelector('[data-prog]:checked').value.startsWith('Programmeret');
      linkWrap.hidden = !needsLink;
    });
  });

  function note(msg, isError) {
    form.querySelector('.formnote')?.remove();
    const el = document.createElement('p');
    el.className = 'formnote' + (isError ? ' formnote--err' : '');
    el.setAttribute('role', isError ? 'alert' : 'status');
    el.textContent = msg;
    form.querySelector('.sumbox').appendChild(el);
    el.scrollIntoView({ block: 'nearest' });
  }

  form.addEventListener('submit', e => {
    e.preventDefault();

    // Validate inline rather than on submit-and-bounce.
    const required = [...form.querySelectorAll('[required]')];
    const missing = required.filter(f => !f.value.trim() || (f.type === 'email' && !f.checkValidity()));
    required.forEach(f => f.setAttribute('aria-invalid', String(missing.includes(f))));
    if (missing.length) {
      missing[0].focus();
      note('Udfyld de markerede felter, så sender vi bestillingen.', true);
      return;
    }

    const q = clampQty(), unit = unitFor(q);
    const goods = unit * q, ship = shipCost();
    const d = Object.fromEntries(new FormData(form).entries());

    // Shopify as the till: hand the basket over via a cart permalink and let
    // Shopify own payment, shipping selection and the receipt. The Google link
    // and the programming choice ride along as cart attributes, so they land
    // on the order without us needing a backend of our own.
    if (SHOPIFY.domain && SHOPIFY.variantId) {
      const attrs = new URLSearchParams();
      attrs.set('attributes[Programmering]', d.programmering || '');
      if (d.google_link) attrs.set('attributes[Google-link]', d.google_link);
      if (d.virksomhed)  attrs.set('attributes[Virksomhed]', d.virksomhed);
      if (d.cvr)         attrs.set('attributes[CVR]', d.cvr);
      if (d.besked)      attrs.set('attributes[Besked]', d.besked);
      attrs.set('attributes[Levering]', shipMode() === 'hjem' ? 'Hjemmelevering' : 'Pakkeshop');
      note('Sender dig til betaling…');
      location.href = `https://${SHOPIFY.domain}/cart/${SHOPIFY.variantId}:${q}?${attrs}`;
      return;
    }

    const lines = [
      `Antal:            ${q} stk.`,
      `Pris pr. stk.:    ${kr(unit)} kr`,
      `Varer i alt:      ${kr(goods)} kr`,
      `Levering:         ${shipMode() === 'hjem' ? 'Hjemmelevering' : 'Pakkeshop'}`,
      `Fragt:            ${ship === 0 ? 'Gratis' : kr(ship) + ' kr'}`,
      `I ALT:            ${kr(goods + ship)} kr inkl. moms`,
      '',
      `Programmering:    ${d.programmering}`,
      d.google_link ? `Google-link:      ${d.google_link}` : null,
      '',
      `Virksomhed:       ${d.virksomhed}`,
      d.cvr ? `CVR:              ${d.cvr}` : null,
      `Navn:             ${d.navn}`,
      `E-mail:           ${d.email}`,
      d.telefon ? `Telefon:          ${d.telefon}` : null,
      `Adresse:          ${d.adresse}`,
      d.besked ? `\nBesked:\n${d.besked}` : null,
    ].filter(Boolean).join('\n');

    if (ORDER_ENDPOINT) {
      fetch(ORDER_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...d, antal: q, pris_pr_stk: unit, i_alt: goods + ship }),
      })
        .then(r => r.ok ? note('Tak — din bestilling er sendt. Du får en bekræftelse på mail.')
                        : note('Noget gik galt. Prøv igen, eller skriv til os direkte.', true))
        .catch(() => note('Kunne ikke sende. Tjek forbindelsen, eller skriv til os direkte.', true));
      return;
    }

    const to = (window.BRAND && window.BRAND.email) || '';
    location.href = `mailto:${to}?subject=${encodeURIComponent('Bestilling — ' + q + ' anmeldelseskort')}&body=${encodeURIComponent(lines)}`;
    note('Din mailklient åbner med bestillingen. Tryk send, så vender vi tilbage med en bekræftelse.');
  });

  linkWrap.hidden = false;
  render();
})();

/* ---------- Sticky bottom CTA — appears once the hero is behind you ---------- */
(() => {
  const bar = document.querySelector('[data-stickybar]');
  if (!bar) return;
  const hero = document.querySelector('.heroblock');
  if (!hero) return;

  // Show only while the hero is off-screen and the footer hasn't arrived —
  // a bar that overlaps the page's own CTA is just noise.
  const foot = document.querySelector('.foot');
  const io = new IntersectionObserver(() => {
    const heroGone = hero.getBoundingClientRect().bottom < 0;
    const footHere = foot ? foot.getBoundingClientRect().top < innerHeight : false;
    bar.dataset.show = String(heroGone && !footHere);
  }, { threshold: 0 });
  io.observe(hero);
  if (foot) io.observe(foot);

  let ticking = false;
  addEventListener('scroll', () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      ticking = false;
      const heroGone = hero.getBoundingClientRect().bottom < 0;
      const footHere = foot ? foot.getBoundingClientRect().top < innerHeight : false;
      bar.dataset.show = String(heroGone && !footHere);
    });
  }, { passive: true });
})();

/* ---------- Year ---------- */
document.querySelectorAll('[data-year]').forEach(el => {
  el.textContent = String(new Date().getFullYear());
});
