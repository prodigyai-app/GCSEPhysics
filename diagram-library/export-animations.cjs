/* Build one self-contained HTML file for every interactive simulation and required practical lab on the
   GCSE Physics site. Each file contains only the styles and scripts that animation needs (shared lab engine,
   lesson framework and the one lesson or lab), so it opens offline, from a USB stick or inside an iframe.

   Usage (from the repo root):  node diagram-library/export-animations.cjs
   Output: diagram-library/animations/*.html, animations.json and index.html. Run again after the site changes. */
'use strict';
const fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..'), OUT = path.join(__dirname, 'animations');
const html = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
const lines = html.split('\n');

// ---- split the page into its inline <script> blocks (each lesson and lab is its own block) ----
const blocks = [];
for (const m of html.matchAll(/<script>([\s\S]*?)<\/script>/g)) blocks.push({ code: m[1], at: m.index });
const find = (re, from = 0) => blocks.findIndex((b, i) => i >= from && re.test(b.code));
const iLab = find(/^\s*window\.LAB=\(\(\)=>\{/);
const iLearn = find(/Learning-content framework built on LAB/);
const iFirstUnit = find(/^\s*LEARN\.unit=/);
if (iLab < 0 || iLearn < 0 || iFirstUnit < 0) throw new Error('Page structure changed: cannot find the LAB engine, LEARN framework or first unit');
const core = blocks.slice(iLab, iLab + 1).map(b => b.code);
const framework = blocks.slice(iLearn, iFirstUnit).map(b => b.code); // LEARN, exam engine, icons, symbols, GCSE helpers

// ---- styles: every <style> block in the head and the layout stylesheets the lessons use ----
const head = html.slice(0, html.indexOf('<body'));
const styles = [...head.matchAll(/<style>([\s\S]*?)<\/style>/g)].map(m => m[1]);
const bodyStyles = [...html.slice(html.indexOf('<body')).matchAll(/<style>([\s\S]*?)<\/style>/g)].map(m => m[1]).filter(s => !/printTitle|PZCSS/.test(s));
const cssFiles = ['simple-layout.css', 'lesson-width.css', 'diagram-fit.css'].map(f => fs.readFileSync(path.join(ROOT, f), 'utf8'));
const fonts = (head.match(/<link href="https:\/\/fonts\.googleapis\.com[^>]*>/) || [''])[0];
// Theme: ?theme=light or ?theme=dark in the address (for embedding), otherwise the site's saved choice, otherwise dark like the site.
const themeScript = `<script>(function(){var t=(location.search.match(/[?&]theme=(light|dark)/)||[])[1];if(!t){try{t=localStorage.getItem("site-theme")}catch(e){}}document.documentElement.setAttribute("data-theme",t==="light"?"light":"dark");})();</script>`;
const templates = [...html.matchAll(/<template id="[^"]+">[\s\S]*?<\/template>/g)].map(m => m[0]).join('\n');
const jsFile = f => fs.readFileSync(path.join(ROOT, f), 'utf8');
const helpers = ['math-notation.js', 'numeric-tools.js', 'physics-equations.js'].filter(f => fs.existsSync(path.join(ROOT, f))).map(jsFile);
const examBoard = (html.match(/<script>\s*window\.EXAM_BOARD=[^<]*<\/script>/) || [''])[0];

const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const plain = s => String(s).replace(/<[^>]+>/g, '').replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').trim();
const safeScript = s => s.replace(/<\/script/gi, '<\\/script');

// ---- the animations: every B.sim(...) in a lesson, and every required practical lab ----
const UNIT = { energy: 'Energy', electricity: 'Electricity', particle: 'Particle model of matter', atomic: 'Atomic structure', forces: 'Forces', waves: 'Waves', magnetism: 'Magnetism and electromagnetism', space: 'Space physics' };
const unitName = u => UNIT[u] || Object.entries(UNIT).find(([k]) => u.startsWith(k.slice(0, 4)))?.[1] || u;
const items = [];
blocks.forEach((b, i) => {
  for (const m of b.code.matchAll(/B\.sim\("([\w-]+)","([^"]+)"/g)) {
    const L = b.code.match(/lesson\(\{id:"([\w-]+)"[^]*?name:"([^"]+)"/);
    let u = i; while (u >= 0 && !/^\s*LEARN\.unit=/.test(blocks[u].code)) u--;
    const unit = (blocks[u].code.match(/LEARN\.unit="([^"]+)"/) || [])[1] || '';
    items.push({ kind: 'sim', id: m[1], title: plain(m[2]), lesson: L[1], lessonName: plain(L[2]), unit, topic: unitName(unit), scripts: [...framework, blocks[u].code, b.code] });
  }
  const r = b.code.match(/register\(\{id:"([\w-]+)",group:"gcse",num:(\d+),name:"([^"]+)"/);
  if (r) items.push({ kind: 'lab', id: r[1], num: +r[2], title: plain(r[3]), topic: 'Required practicals', scripts: [b.code] });
});

const slug = s => s.toLowerCase().replace(/[’'“”]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const fileOf = it => it.kind === 'lab' ? `practical-${String(it.num).padStart(2, '0')}-${slug(it.title)}` : `${it.lesson}-${slug(it.title)}`;

// Runs after the lesson or lab has been built: open that page, then hide everything except the animation.
const isolate = it => `(function(){
 var KIND=${JSON.stringify(it.kind)}, PAGE=${JSON.stringify(it.kind === 'lab' ? it.id : it.lesson)}, TARGET=${JSON.stringify(it.kind === 'lab' ? 'lab-' + it.id : it.id)};
 try{ LAB.boot({groups:[["gcse",""]]}); }catch(e){ console.error(e); }
 var page=LAB.list.filter(function(p){return p.id===PAGE;})[0];
 var section=document.getElementById('lab-'+PAGE), target=document.getElementById(TARGET);
 if(!section||!target){ document.body.insertAdjacentHTML('afterbegin','<p style="padding:16px">This animation could not be built.</p>'); return; }
 LAB.list.forEach(function(p){ var s=document.getElementById('lab-'+p.id); if(s) s.hidden=p.id!==PAGE; });
 section.hidden=false; target.setAttribute('data-anim-root','');
 for(var el=target.parentElement; el&&el!==document.body; el=el.parentElement) el.setAttribute('data-anim-path','');
 if(KIND==='lab'){ var nb=section.querySelector('.lab-notebook'); if(nb) nb.remove(); }
 var redraw=function(){ if(page&&(page.redraw||page.onShow)) (page.redraw||page.onShow)(); };
 requestAnimationFrame(function(){ redraw(); window.dispatchEvent(new Event('resize')); });
})();`;

const page = it => `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(it.title)}</title>
<meta name="description" content="${esc(it.kind === 'lab' ? `AQA GCSE Physics required practical ${it.num}: ${it.title}. Interactive lab.` : `AQA GCSE Physics interactive: ${it.title} (${it.lessonName}).`)}">
${fonts}
${styles.map(s => `<style>${s}</style>`).join('\n')}
${cssFiles.map(s => `<style>${s}</style>`).join('\n')}
${bodyStyles.map(s => `<style>${s}</style>`).join('\n')}
<style>
/* Standalone animation: only the animation and a short heading are shown. */
body.anim-standalone .wrap>:not([data-anim-path]):not([data-anim-root]):not(.anim-head),
body.anim-standalone [data-anim-path]>:not([data-anim-path]):not([data-anim-root]):not(.anim-head):not(template){display:none!important}
body.anim-standalone .wrap{gap:12px}
body.anim-standalone [data-anim-root]{margin:0}${it.kind === 'lab' ? 'body.anim-standalone section[data-anim-root]{display:block!important}' : ''}
body.anim-standalone .anim-head{padding:4px 2px 0}
body.anim-standalone .anim-head .muted{margin:4px 0 0}
${it.kind === 'sim' ? 'body.anim-standalone [data-anim-root]>h3 .kind{display:none}' : ''}
</style>
<script>window.ALP_SITE="gcse-physics";window.LabNotebook={attach:function(){},observe:function(id,s){return s},flush:function(){}};</script>
${helpers.map(s => `<script>${safeScript(s)}</script>`).join('\n')}
</head>
<body class="anim-standalone">
${themeScript}
<div class="wrap">
<header class="anim-head"><span class="eyebrow">${esc(it.kind === 'lab' ? `AQA GCSE Physics · Required practical ${it.num}` : `AQA GCSE Physics · ${it.topic} · ${it.lessonName}`)}</span></header>
<nav id="switcher" hidden></nav>
${templates}
</div>
${examBoard}
${[...core, ...it.scripts].map(s => `<script>${safeScript(s)}</script>`).join('\n')}
<script>${isolate(it)}</script>
</body></html>
`;

fs.mkdirSync(OUT, { recursive: true });
for (const f of fs.readdirSync(OUT)) if (f.endsWith('.html')) fs.unlinkSync(path.join(OUT, f));
const meta = [];
for (const it of items) {
  const file = fileOf(it) + '.html';
  fs.writeFileSync(path.join(OUT, file), page(it));
  meta.push({ file, kind: it.kind, id: it.id, title: it.title, topic: it.topic, lesson: it.lesson || null, lessonName: it.lessonName || null, practical: it.num || null });
}
fs.writeFileSync(path.join(OUT, 'animations.json'), JSON.stringify(meta, null, 1));

// ---- browsing page ----
const order = ['Required practicals', ...Object.values(UNIT)];
const groups = order.map(t => [t, meta.filter(m => m.topic === t)]).filter(([, a]) => a.length);
const card = m => `<li><a href="${m.file}">${esc(m.kind === 'lab' ? `RP ${m.practical}: ${m.title}` : m.title)}</a>${m.kind === 'sim' ? `<span>${esc(m.lessonName)}</span>` : ''}<code>${m.file}</code></li>`;
fs.writeFileSync(path.join(OUT, 'index.html'), `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>GCSE Physics animations</title>
<style>:root{--bg:#f4f6f9;--card:#fff;--ink:#1d2733;--muted:#5a6b7d;--line:#d9e0e8;--acc:#1f6fd1}@media (prefers-color-scheme:dark){:root{--bg:#0f1620;--card:#172131;--ink:#e8ecf5;--muted:#9aa8ba;--line:#2a3a50;--acc:#7fb2ff}}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 system-ui,Segoe UI,Arial,sans-serif}main{max-width:1100px;margin:0 auto;padding:24px 16px 60px}h1{margin:0 0 4px}p{color:var(--muted);margin:0 0 12px}
h2{margin:28px 0 10px;font-size:1.15rem}ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr));gap:10px}
li{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px;display:grid;gap:2px}li span{color:var(--muted);font-size:.9rem}code{font-size:.75rem;color:var(--muted);overflow-wrap:anywhere}a{color:var(--acc);font-weight:600}pre{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px;overflow-x:auto;font-size:.82rem}</style></head>
<body><main><h1>GCSE Physics animations</h1>
<p>${meta.length} interactive animations from the GCSE Physics site: ${meta.filter(m => m.kind === 'sim').length} lesson simulations and ${meta.filter(m => m.kind === 'lab').length} required practical labs. Each is a single self-contained HTML file that works offline. Open one in a browser, or put it in a lesson page with an iframe. Add <code>?theme=light</code> to the address for the light theme (dark is the default, as on the site).</p>
<pre>&lt;iframe src="animations/wa1-watching-a-wave-pass.html?theme=light" style="width:100%;height:640px;border:0" title="Watching a wave pass"&gt;&lt;/iframe&gt;</pre>
${groups.map(([t, a]) => `<h2>${esc(t)}</h2><ul>${a.map(card).join('')}</ul>`).join('\n')}
</main></body></html>
`);
console.log(`${meta.length} animations (${meta.filter(m => m.kind === 'sim').length} simulations, ${meta.filter(m => m.kind === 'lab').length} labs) written to ${path.relative(ROOT, OUT)}/`);
