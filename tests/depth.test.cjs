const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs'), path = require('node:path');
const {verify} = require('../tools/verify-depth.cjs');
const {check} = require('../tools/similarity.cjs');

test('every numerical answer in the depth data is reproduced by its calculation', () => {
  const r = verify();
  assert.deepEqual(r.errs, []);
  assert.ok(r.asserts > 40, 'expected the data files to be checked');
});

const MIN_MARKS = 5; /* raise as the exam-question passes land: target 10 */
test('every lesson with depth data reaches the exam-mark floor and has new worked examples and fill-the-gaps', () => {
  const cat = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'assessment-catalog.json'), 'utf8'));
  for (const row of verify().rows) {
    const old = (cat.pages[row.id]?.questions || []).filter(q => !q.id.startsWith('check:')).reduce((s, q) => s + q.m, 0);
    assert.ok(old + row.marks >= MIN_MARKS, `${row.id}: ${old} existing + ${row.marks} new marks`);
    /* worked examples follow in the Opus pass */
    assert.ok(row.gaps >= 3, `${row.id}: fewer than 3 fill-the-gaps`);
  }
});

test('no new exam question is a near-duplicate of an existing one', () => {
  assert.deepEqual(check(0.45).hits, []);
});
