/* Print practical-sheets/html/*.html to A4 PDFs in practical-sheets/, with a footer and page numbers.
   Run from the repo root after tools/practical_sheets.py: node tools/practical_sheets_pdf.cjs */
'use strict';
const fs = require('fs'), path = require('path'), { chromium } = require('playwright');
const DIR = path.join(__dirname, '..', 'practical-sheets'), SRC = path.join(DIR, 'html');
(async () => {
  const b = await chromium.launch(), p = await b.newPage();
  for (const f of fs.readdirSync(SRC).filter(f => f.endsWith('.html')).sort()) {
    await p.goto('file://' + path.join(SRC, f)); await p.waitForTimeout(200);
    const title = await p.title();
    await p.pdf({ path: path.join(DIR, f.replace(/\.html$/, '.pdf')), format: 'A4', printBackground: true, displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: `<div style="font:8px Arial,sans-serif;color:#6b7b8b;width:100%;padding:0 14mm;display:flex;justify-content:space-between"><span>${title.replace(/^RP(\d+)/, 'Required practical $1 ·')} · simulation practical</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>`,
      margin: { top: '14mm', bottom: '16mm', left: '14mm', right: '14mm' } });
    console.log(f);
  }
  await b.close();
})();
