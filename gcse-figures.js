/* GCSE Physics: extra figures that replace repeated or mismatched ones (work done, elastic energy, electrical power,
   half-life, uses of EM waves, the solar system). Registers on window.SciFig; load after science-figures-2.js. */
(function (root) {
  'use strict';
  const S = root.SciFig;
  if (!S || !S._more) return;
  const { T, arrow, id } = S._more, wrap = S._wrap, f = S._f;
  const INK = 'currentColor', BLUE = '#3a78d8', ORG = '#e8792a', GRN = '#2f9e6b', RED = '#c2442f', GREY = '#8a94a3';
  const box = (x, y, w, h, c, op = 0.14, r = 10) => `<rect x="${f(x)}" y="${f(y)}" width="${f(w)}" height="${f(h)}" rx="${r}" fill="${c}" fill-opacity="${op}" stroke="${c}" stroke-width="1.6"/>`;
  const line = (x1, y1, x2, y2, c = INK, w = 2, d = '') => `<path d="M${f(x1)} ${f(y1)}L${f(x2)} ${f(y2)}" stroke="${c}" stroke-width="${w}" fill="none"${d ? ` stroke-dasharray="${d}"` : ''} stroke-linecap="round"/>`;

  function workDone(o = {}) {
    const W = 900, H = 330; let g = '';
    g += `<rect x="40" y="226" width="820" height="14" rx="4" fill="${GREY}" fill-opacity=".35"/>`;
    g += `<rect x="90" y="170" width="86" height="56" rx="6" fill="${ORG}" fill-opacity=".25" stroke="${ORG}" stroke-width="2"/>` + T(133, 205, 'crate', { size: 14 });
    g += `<rect x="640" y="170" width="86" height="56" rx="6" fill="none" stroke="${ORG}" stroke-width="2" stroke-dasharray="6 5"/>` + T(683, 205, 'later', { size: 13, fill: GREY });
    
    g += arrow(46, 198, 88, 198, RED, 5, 15) + T(46, 154, 'force F = 40 N', { size: 15, w: 700, fill: RED, a: 'start' });
    g += line(133, 250, 133, 276, INK, 1.5) + line(683, 250, 683, 276, INK, 1.5) + arrow(133, 266, 683, 266, BLUE, 2.5, 11) + arrow(683, 266, 133, 266, BLUE, 2.5, 11) + T(408, 292, 'distance moved in the direction of the force, s = 6.0 m', { size: 15, w: 700, fill: BLUE });
    g += box(560, 40, 300, 84, GRN, 0.14) + T(710, 70, 'work done = force × distance', { size: 15, w: 700 }) + T(710, 96, 'W = F s = 40 × 6.0 = 240 J', { size: 17, w: 700, fill: GRN }) + T(710, 116, '1 joule = 1 N moving an object 1 m', { size: 12 });
    g += T(40, 50, 'Work done: energy transferred by a force', { size: 17, w: 700, a: 'start' }) + T(40, 74, 'The same amount of energy is transferred to the crate’s kinetic store', { size: 12, a: 'start' }) + T(40, 90, 'and to the thermal store of the floor and crate (friction).', { size: 12, a: 'start' });
    return wrap(W, H, o.aria || 'A crate pushed 6.0 metres by a 40 newton force: work done is force times distance, 240 joules', '', g);
  }

  function elasticEnergy(o = {}) {
    const W = 900, H = 400, ox = 120, oy = 330, ex = 520, ey = 70; let g = '';
    g += arrow(ox, oy, 640, oy, INK, 2.5, 12) + arrow(ox, oy, ox, 40, INK, 2.5, 12);
    g += T(390, 372, 'extension e (m)', { size: 15, w: 700 }) + `<text x="40" y="190" font-size="15" font-weight="700" text-anchor="middle" class="sf-lab" transform="rotate(-90 40 190)">force F (N)</text>`;
    g += `<path d="M${ox} ${oy}L${ex} ${oy}L${ex} ${ey}Z" fill="${GRN}" fill-opacity=".25" stroke="none"/>`;
    g += line(ox, oy, ex + 30, ey - 15, BLUE, 4) + line(ex, ey, ex, oy, GREY, 1.5, '6 5') + line(ox, ey, ex, ey, GREY, 1.5, '6 5');
    g += `<circle cx="${ex}" cy="${ey}" r="6" fill="${BLUE}"/>` + T(ex, oy + 22, 'e', { size: 16, w: 700 }) + T(ox - 16, ey + 5, 'F', { size: 16, w: 700, a: 'end' });
    g += T(390, 280, 'area = ½ F e', { size: 16, w: 700, fill: GRN }) + T(390, 300, '= energy stored', { size: 14, fill: GRN });
    g += T(215, 150, 'gradient = k', { size: 15, w: 700, fill: BLUE }) + T(215, 170, '(F = k e)', { size: 13, fill: BLUE });
    g += box(650, 80, 230, 120, GRN, 0.14) + T(765, 110, 'Elastic potential energy', { size: 15, w: 700 }) + T(765, 140, 'E_e = ½ k e²', { size: 20, w: 700, fill: GRN }) + T(765, 168, 'k in N/m, e in m', { size: 13 }) + T(765, 188, 'valid below the limit of proportionality', { size: 11 });
    return wrap(W, H, o.aria || 'A straight force–extension graph. The area under the line is the energy stored in the spring, one half times force times extension', '', g);
  }

  function powerCircuit(o = {}) {
    const W = 900, H = 380; let g = '';
    const L = 90, R = 500, Tp = 130, Bt = 280;
    const wire = d => `<path d="${d}" fill="none" stroke="${INK}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>`;
    g += wire(`M${L} 186V${Tp}H248`) + wire(`M292 ${Tp}H${R}V196`) + wire(`M${R} 244V${Bt}H${L}V228`);
    g += line(L - 22, 192, L + 22, 192, INK, 3) + line(L - 11, 206, L + 11, 206, INK, 6) + line(L - 22, 222, L + 22, 222, INK, 3) + T(L + 36, 214, '12 V cell', { size: 14, w: 700, a: 'start' });
    g += `<circle cx="270" cy="${Tp}" r="22" fill="#e0a64a" fill-opacity=".3" stroke="${INK}" stroke-width="2.5"/>` + line(256, Tp - 14, 284, Tp + 14, INK, 2) + line(284, Tp - 14, 256, Tp + 14, INK, 2) + T(270, Tp + 44, 'lamp', { size: 14 });
    g += `<path d="M230 ${Tp}V62H248M292 62H310V${Tp}" fill="none" stroke="${GRN}" stroke-width="2.5"/><circle cx="270" cy="62" r="22" fill="none" stroke="${GRN}" stroke-width="3"/>` + T(270, 69, 'V', { size: 20, w: 700, fill: GRN }) + T(318, 28, 'voltmeter reads 12 V (in parallel with the lamp)', { size: 13, w: 700, a: 'start', fill: GRN });
    g += `<circle cx="${R}" cy="220" r="24" fill="none" stroke="${BLUE}" stroke-width="3"/>` + T(R, 227, 'A', { size: 20, w: 700, fill: BLUE }) + T(R - 34, 226, '2.0 A', { size: 15, w: 700, fill: BLUE, a: 'end' });
    g += T(300, 330, 'The ammeter is in series; the voltmeter is across the lamp.', { size: 13 });
    g += box(560, 60, 320, 240, ORG, 0.12) + T(720, 92, 'Electrical power', { size: 17, w: 700 });
    g += T(720, 128, 'P = V I', { size: 20, w: 700, fill: ORG }) + T(720, 152, '= 12 × 2.0 = 24 W', { size: 15 });
    g += T(720, 190, 'P = I² R', { size: 20, w: 700, fill: ORG }) + T(720, 214, '(use when V is not known)', { size: 12 });
    g += T(720, 250, 'E = P t', { size: 20, w: 700, fill: ORG }) + T(720, 274, 'energy (J) = power (W) × time (s)', { size: 12 });
    g += T(300, 358, '24 W means 24 J of energy is transferred by the lamp every second.', { size: 14 });
    return wrap(W, H, o.aria || 'A lamp circuit with a 12 volt cell, an ammeter reading 2.0 amps and a voltmeter across the lamp reading 12 volts: power is 24 watts', '', g);
  }

  function halfLifeCurve(o = {}) {
    const W = 900, H = 400, ox = 110, oy = 320, wd = 640, ht = 250; let g = '';
    const X = t => ox + t * wd / 4, Y = a => oy - a * ht / 800;
    g += arrow(ox, oy, ox + wd + 30, oy, INK, 2.5, 12) + arrow(ox, oy, ox, 50, INK, 2.5, 12);
    g += T(ox + wd / 2, 372, 'time (in half-lives)', { size: 15, w: 700 }) + `<text x="38" y="185" font-size="15" font-weight="700" text-anchor="middle" class="sf-lab" transform="rotate(-90 38 185)">activity (Bq)</text>`;
    let d = ''; for (let i = 0; i <= 80; i++) { const t = i / 20; d += (i ? 'L' : 'M') + f(X(t)) + ' ' + f(Y(800 * Math.pow(0.5, t))); }
    g += `<path d="${d}" fill="none" stroke="${BLUE}" stroke-width="4"/>`;
    [0, 1, 2, 3].forEach(n => { const a = 800 / Math.pow(2, n); g += line(X(n), oy, X(n), Y(a), GREY, 1.5, '6 5') + line(ox, Y(a), X(n), Y(a), GREY, 1.5, '6 5') + `<circle cx="${f(X(n))}" cy="${f(Y(a))}" r="6" fill="${ORG}"/>` + T(ox - 12, Y(a) + 5, String(a), { size: 14, a: 'end' }) + T(X(n), oy + 22, String(n), { size: 14, w: 700 }); });
    g += T(X(1) + 50, Y(400) - 14, '÷ 2 every half-life', { size: 14, w: 700, fill: ORG, a: 'start' });
    g += box(590, 70, 290, 108, GRN, 0.14) + T(735, 98, 'Half-life', { size: 16, w: 700 }) + T(735, 124, 'time for the activity (or the number', { size: 12 }) + T(735, 142, 'of nuclei) to fall to half', { size: 12 }) + T(735, 166, 'Short half-life: strong, but gone quickly', { size: 12, w: 700, fill: GRN });
    return wrap(W, H, o.aria || 'A decay curve: the activity halves from 800 to 400 to 200 to 100 becquerel after each half-life', '', g);
  }

  function emUses(o = {}) {
    const W = 980, H = 430; let g = '';
    const rows = [['Radio', 'TV and radio broadcasts', 'none at normal levels', '#c2442f'], ['Microwave', 'cooking, satellite links', 'heats: body cells', '#e8792a'], ['Infrared', 'heaters, remote controls, cameras', 'skin burns', '#d9a521'], ['Visible', 'sight, fibre optics', 'too bright: eye damage', '#3fae6c'], ['Ultraviolet', 'sun beds, security marking', 'skin cancer: eye damage', '#3a78d8'], ['X-rays', 'imaging bones', 'ionising: cell damage', '#6a5bd0'], ['Gamma', 'sterilising, radiotherapy', 'ionising: cancer', '#a24bc2']];
    const w = 118, gap = 12, x0 = 40;
    g += arrow(30, 52, 950, 52, INK, 2, 11) + T(40, 36, 'low frequency, long wavelength', { size: 12, a: 'start' }) + T(940, 36, 'high frequency, short wavelength', { size: 12, a: 'end' });
    rows.forEach((r, i) => { const x = x0 + i * (w + gap); g += box(x, 76, w, 70, r[3], 0.22) + T(x + w / 2, 118, r[0], { size: 15, w: 700 }); g += T(x + w / 2, 176, 'USE', { size: 11, w: 700, fill: GRN }); r[1].split(', ').forEach((l, j) => { g += T(x + w / 2, 198 + j * 18, l, { size: 12 }); }); g += T(x + w / 2, 292, 'HAZARD', { size: 11, w: 700, fill: RED }); r[2].split(': ').forEach((l, j) => { g += T(x + w / 2, 314 + j * 18, l, { size: 12 }); }); });
    g += T(490, 390, 'Higher-frequency waves carry more energy, so X-rays and gamma rays (ionising) are the most hazardous.', { size: 14, w: 700 });
    return wrap(W, H, o.aria || 'The electromagnetic spectrum from radio waves to gamma rays, with one use and one hazard for each type', '', g);
  }

  function solarSystem(o = {}) {
    const W = 980, H = 330; let g = '';
    g += `<circle cx="20" cy="150" r="80" fill="#f2b632" fill-opacity=".9"/><circle cx="20" cy="150" r="80" fill="none" stroke="#e08a1a" stroke-width="3"/>` + T(70, 258, 'Sun', { size: 15, w: 700 });
    const P = [['Mercury', 130, 6, '#9a9a9a'], ['Venus', 190, 11, '#d9b36a'], ['Earth', 255, 12, '#3a78d8'], ['Mars', 315, 8, '#c2442f'], ['Jupiter', 470, 38, '#d49a6a'], ['Saturn', 610, 32, '#d9c28a'], ['Uranus', 740, 20, '#6ec6d9'], ['Neptune', 860, 19, '#3a5fd8']];
    g += `<path d="M20 150H970" stroke="${GREY}" stroke-width="1" stroke-dasharray="4 6"/>`;
    P.forEach((p, i) => { g += `<circle cx="${p[1]}" cy="150" r="${p[2]}" fill="${p[3]}"/>`; if (p[0] === 'Saturn') g += `<ellipse cx="${p[1]}" cy="150" rx="${p[2] * 1.9}" ry="7" fill="none" stroke="#b79a5c" stroke-width="3"/>`; const up = i % 2 === 0; g += T(p[1], up ? 150 - p[2] - 16 : 150 + p[2] + 28, p[0], { size: 13, w: 700 }); });
    for (let i = 0; i < 14; i++) g += `<circle cx="${f(375 + (i * 37) % 60)}" cy="${f(138 + (i * 53) % 26)}" r="2.2" fill="${GREY}"/>`;
    g += T(405, 98, 'asteroid belt', { size: 12, fill: GREY });
    g += box(20, 280, 940, 36, GRN, 0.1, 8) + T(490, 303, 'Not to scale. The solar system is one small part of the Milky Way galaxy, which contains billions of stars.', { size: 13, w: 700 });
    return wrap(W, H, o.aria || 'The Sun and the eight planets in order: Mercury, Venus, Earth, Mars, the asteroid belt, Jupiter, Saturn, Uranus and Neptune, not drawn to scale', '', g);
  }

  function isotopesPair(o = {}) {
    const W = 900, H = 380; let g = '';
    const atom = (cx, n, name, mass) => {
      let s = `<circle cx="${cx}" cy="170" r="110" fill="none" stroke="${GREY}" stroke-width="1.5" stroke-dasharray="3 5"/><circle cx="${cx}" cy="170" r="62" fill="none" stroke="${GREY}" stroke-width="1.5" stroke-dasharray="3 5"/>`;
      const N = 6 + n, isP = i => [0, 1, 2, 3, 4, 5].some(k => Math.round(k * N / 6 + (N / 12)) % N === i);
      for (let i = 0; i < N; i++) { const r = 8.4 * Math.sqrt(i + 0.5), a = i * 2.39996; s += `<circle cx="${f(cx + r * Math.cos(a))}" cy="${f(170 + r * Math.sin(a))}" r="9" fill="${isP(i) ? RED : GREY}" stroke="#fff" stroke-width="1"/>`; }
      const e = [[cx + 62 * Math.cos(0.6), 170 - 62 * Math.sin(0.6)], [cx - 62 * Math.cos(0.6), 170 + 62 * Math.sin(0.6)], [cx + 110, 170], [cx - 110, 170], [cx + 110 * Math.cos(2.4), 170 - 110 * Math.sin(2.4)], [cx + 110 * Math.cos(5.2), 170 - 110 * Math.sin(5.2)]];
      e.forEach(p => { s += `<circle cx="${f(p[0])}" cy="${f(p[1])}" r="7" fill="${BLUE}" stroke="#fff" stroke-width="1"/>`; });
      s += T(cx, 312, name, { size: 20, w: 700 }) + T(cx, 338, '6 protons · ' + n + ' neutrons · 6 electrons', { size: 14 }) + T(cx, 360, 'mass number ' + mass, { size: 14, fill: GRN, w: 700 });
      return s;
    };
    g += atom(230, 6, 'Carbon-12', 12) + atom(670, 8, 'Carbon-14', 14);
    g += T(450, 150, 'same number of', { size: 15, w: 700, fill: ORG }) + T(450, 172, 'protons', { size: 18, w: 700, fill: ORG }) + T(450, 200, 'different number of', { size: 15, w: 700, fill: ORG }) + T(450, 222, 'neutrons', { size: 18, w: 700, fill: ORG });
    g += T(450, 40, 'Isotopes: atoms of the same element', { size: 18, w: 700 });
        g += `<circle cx="30" cy="26" r="7" fill="${RED}"/>` + T(44, 31, 'proton', { size: 13, a: 'start' }) + `<circle cx="30" cy="50" r="7" fill="${GREY}"/>` + T(44, 55, 'neutron', { size: 13, a: 'start' }) + `<circle cx="30" cy="74" r="7" fill="${BLUE}"/>` + T(44, 79, 'electron', { size: 13, a: 'start' });
    return wrap(W, H, o.aria || 'Two isotopes of carbon: carbon-12 with 6 protons and 6 neutrons, and carbon-14 with 6 protons and 8 neutrons', '', g);
  }

  S.register('isotopesPair', isotopesPair);

  S.register('workDone', workDone); S.register('elasticEnergy', elasticEnergy); S.register('powerCircuit', powerCircuit);
  S.register('halfLifeCurve', halfLifeCurve); S.register('emUses', emUses); S.register('solarSystem', solarSystem);
})(typeof window === 'undefined' ? globalThis : window);
