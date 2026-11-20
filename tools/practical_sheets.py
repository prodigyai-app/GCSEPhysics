"""Printable student sheets for the ten GCSE Physics required practicals, done with the Practical Lab simulations.
Writes practical-sheets/html/*.html; tools/practical_sheets_pdf.cjs turns them into A4 PDFs.
Run from the repo root: python3 tools/practical_sheets.py && node tools/practical_sheets_pdf.cjs"""
import html, os, re

SITE = 'physicsgcse.prodigyai.uk'
OUT = os.path.join(os.path.dirname(__file__), '..', 'practical-sheets', 'html')

def md(s):
    """**bold**, _italic_ and HT tag in short strings."""
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w])_(.+?)_(?![\w])', r'<i>\1</i>', s)
    s = s.replace('[HT]', '<span class="ht">HT</span>')
    return s

def lines(n):
    return '<div class="lines">' + '<div></div>' * n + '</div>'

def table(t):
    cols, rows = t['cols'], t['rows']
    widths = t.get('widths')
    h = f'<div class="tcap"><b>{md(t["caption"])}</b></div><table class="res">'
    if widths:
        h += '<colgroup>' + ''.join(f'<col style="width:{w}%">' for w in widths) + '</colgroup>'
    h += '<thead><tr>' + ''.join(f'<th>{md(c)}</th>' for c in cols) + '</tr></thead><tbody>'
    for r in rows:
        r = r + [''] * (len(cols) - len(r))
        h += '<tr>' + ''.join(f'<td>{md(str(c))}</td>' for c in r) + '</tr>'
    h += '</tbody></table>'
    if t.get('after'):
        h += f'<p class="fill">{md(t["after"])}</p>'
    return h

def gridsvg(w, h):
    """Graph paper drawn as lines (CSS background grids drop out when printed to PDF): 2 mm minor, 10 mm major."""
    l = []
    for x in range(0, w + 1, 2):
        l.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}" class="{"M" if x % 10 == 0 else "m"}"/>')
    for y in range(0, h + 1, 2):
        l.append(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" class="{"M" if y % 10 == 0 else "m"}"/>')
    return (f'<svg class="grid" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}"><style>.m{{stroke:#c9d4de;stroke-width:.15}}.M{{stroke:#8299ad;stroke-width:.3}}</style>'
            + ''.join(l) + f'<rect x="0" y="0" width="{w}" height="{h}" fill="none" stroke="#5f7486" stroke-width=".5"/></svg>')

def grid(g):
    w, hgt = g.get('w', 170), g.get('h', 150)
    return (f'<div class="graph"><div class="gtitle">{md(g["title"])}</div>'
            + gridsvg(w, hgt)
            + (f'<p class="hint">{md(g["hint"])}</p>' if g.get('hint') else '') + '</div>')

def step(i, s):
    text, tip = (s if isinstance(s, tuple) else (s, None))
    return (f'<li><span class="box"></span><span class="n">{i}</span><div>{md(text)}'
            + (f'<div class="tip">{md(tip)}</div>' if tip else '') + '</div></li>')

def question(i, q):
    text, n = q[0], q[1]
    extra = q[2] if len(q) > 2 else ''
    return f'<div class="q"><div class="qn">{i}</div><div class="qb"><p>{md(text)}</p>{extra}{lines(n)}</div></div>'

VARS = ('<table class="vars"><tr><th>Independent variable</th><td></td></tr><tr><th>Dependent variable</th><td></td></tr>'
        '<tr><th>Control variables (two)</th><td></td></tr></table>')

def sheet(s):
    num = s['num']
    comb = f' · Combined Science required practical {s["comb"]}' if s.get('comb') else ' · Physics only'
    h = [f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>RP{num} {html.escape(s["title"])}</title>'
         '<link rel="stylesheet" href="sheet.css"></head><body>']
    h.append(f'<header><div class="eyebrow">AQA GCSE Physics · Required practical {num}{comb}</div>'
             f'<h1>{md(s["title"])}</h1><div class="sub">Simulation practical</div></header>')
    h.append('<table class="who"><tr><th>Name</th><td></td><th>Class</th><td></td><th>Date</th><td></td></tr></table>')
    h.append(f'<p class="aim"><b>Aim:</b> {md(s["aim"])}</p>')
    h.append(f'<div class="open"><b>Open:</b> {SITE} → Practical Lab → <b>{md(s["lab"])}</b></div>')
    h.append('<h2>Before you start</h2>')
    for i, q in enumerate(s['before'], 1):
        if q == 'VARS':
            h.append(question(i, ('Complete the variables.', 0, VARS)))
        else:
            h.append(question(i, q))
    stepno = 1
    for part in s['parts']:
        h.append(f'<section class="part"><h2>{md(part["title"])}</h2><ol class="steps">')
        for st in part['steps']:
            h.append(step(stepno, st)); stepno += 1
        h.append('</ol>')
        for t in part.get('tables', []):
            h.append(table(t))
        if part.get('note'):
            h.append(f'<p class="fill">{md(part["note"])}</p>')
        h.append('</section>')
    if s.get('analysis') or s.get('graphs'):
        h.append('<section class="analysis"><h2>Analysis</h2>')
        if s.get('graphs'):
            word = 'graph' if len(s['graphs']) == 1 else 'graphs'
            h.append(f'<p class="gonote"><b>First draw your {word} on the last page.</b> ' + ' '.join(md(x) for x in s.get('graph_steps', [])) + '</p>')
        for i, a in enumerate(s.get('analysis', []), 1):
            h.append(question(i, a))
        h.append('</section>')
    h.append('<section class="concl"><h2>Conclusion and evaluation</h2>')
    for i, q in enumerate(s['questions'], 1):
        h.append(question(i, q))
    h.append('</section>')
    if s.get('graphs'):
        h.append('<section class="graphs">')
        h.append('<h2>Graph</h2>' if len(s['graphs']) == 1 else '<h2>Graphs</h2>')
        for g in s['graphs']:
            h.append(grid(g))
        h.append('</section>')
    h.append('</body></html>')
    return '\n'.join(h)

CSS = r"""
@page{size:A4;margin:14mm 14mm 16mm}
*{box-sizing:border-box}
body{font:10.5pt/1.4 "Segoe UI",Arial,sans-serif;color:#1d2733;margin:0}
header{border-bottom:2px solid #1f5f8b;padding-bottom:6px;margin-bottom:8px}
.eyebrow{font-size:8.5pt;font-weight:700;color:#1f5f8b;letter-spacing:.02em}
h1{font-size:22pt;margin:2px 0 0;color:#14324a;font-weight:600}
.sub{color:#5a6b7d;font-size:10pt}
h2{font-size:13pt;color:#14324a;margin:14px 0 6px;padding-bottom:3px;border-bottom:1px solid #b9c8d6;break-after:avoid}
table.who{width:100%;border-collapse:collapse;margin:4px 0 10px}
table.who th{font-weight:600;text-align:left;font-size:9pt;color:#5a6b7d;width:9%;padding:6px 4px}
table.who td{border-bottom:1px solid #8a99a8;width:24%}
.aim{margin:6px 0}
.open{background:#eaf3fa;border-left:4px solid #1f5f8b;padding:7px 10px;margin:8px 0 4px;font-size:10pt}
ol.steps{list-style:none;padding:0;margin:4px 0 8px}
ol.steps li{display:flex;gap:7px;margin:0 0 6px;break-inside:avoid}
.box{flex:0 0 3.6mm;height:3.6mm;border:1.2px solid #1f5f8b;border-radius:1px;margin-top:1mm}
.n{flex:0 0 5mm;font-weight:700;color:#1f5f8b}
.tip{font-size:9pt;color:#5a6b7d;font-style:italic;margin-top:1px}
.tcap{font-size:9.5pt;margin:8px 0 3px;break-after:avoid}
table.res{width:100%;border-collapse:collapse;margin-bottom:6px;break-inside:avoid;table-layout:fixed}
table.res th{background:#1f5f8b;color:#fff;font-size:9pt;font-weight:600;padding:5px 4px;border:1px solid #1f5f8b;text-align:center;line-height:1.25}
table.res td{border:1px solid #9fb0c0;height:8.5mm;text-align:center;font-size:10pt;padding:0 4px}
table.res td:first-child{background:#f3f7fa;font-weight:600}
table.vars{width:100%;border-collapse:collapse;margin:4px 0}
table.vars th{text-align:left;font-weight:600;font-size:9.5pt;width:34%;padding:4px 6px;background:#f3f7fa;border:1px solid #9fb0c0}
table.vars td{border:1px solid #9fb0c0;height:9mm}
.q{display:flex;gap:8px;margin:0 0 8px;break-inside:avoid}
.qn{flex:0 0 6mm;font-weight:700;color:#1f5f8b}
.qb{flex:1}
.qb p{margin:0 0 2px}
.lines div{border-bottom:1px solid #a9b6c3;height:8mm}
.fill{margin:6px 0;font-size:10pt}
.ht{display:inline-block;background:#14324a;color:#fff;font-size:7.5pt;font-weight:700;padding:0 4px;border-radius:3px;margin-right:4px}
.graph{break-inside:avoid;margin:6px 0 10px}
.gtitle{font-weight:700;font-size:10pt;margin-bottom:4px}
.grid{border:1.2px solid #6f8396;
 background-image:linear-gradient(#8fa3b6 .5px,transparent .5px),linear-gradient(90deg,#8fa3b6 .5px,transparent .5px),
 linear-gradient(#d3dde6 .4px,transparent .4px),linear-gradient(90deg,#d3dde6 .4px,transparent .4px);
 background-size:10mm 10mm,10mm 10mm,2mm 2mm,2mm 2mm;background-position:-.25px -.25px}
.hint{font-size:9pt;color:#5a6b7d;font-style:italic;margin:3px 0 0}
section.graphs{break-before:page}
.diagram{margin:4px 0}
.gonote{background:#f3f7fa;border-left:4px solid #8299ad;padding:6px 10px;margin:8px 0;font-size:10pt}
"""

# A ray meeting a glass block at P, for RP9 "Before you start"
RAY_SVG = ('<svg class="diagram" viewBox="0 0 400 170" width="105mm"><rect x="60" y="70" width="280" height="90" fill="#eaf3fa" stroke="#1d2733" stroke-width="1.5"/>'
           '<text x="70" y="62" font-size="13" fill="#5a6b7d">air</text><text x="70" y="150" font-size="13" fill="#5a6b7d">glass block</text>'
           '<path d="M110 10 L200 70" stroke="#c0392b" stroke-width="2.5"/><path d="M200 70 L240 160" stroke="#c0392b" stroke-width="2.5"/>'
           '<path d="M152 38 l-2 -9 l8 3z" fill="#c0392b"/><circle cx="200" cy="70" r="3" fill="#1d2733"/><text x="207" y="64" font-size="14" font-weight="700">P</text></svg>')

SHEETS = [
 dict(num=1, comb=14, slug='rp01-specific-heat-capacity', title='Specific heat capacity', lab='Specific heat capacity',
  aim='To find the specific heat capacity of a metal block by heating it with an electric heater.',
  before=[('Complete the sentence: the specific heat capacity of a substance is the energy needed to raise the temperature of ............ of the substance by ............ .', 1),
          'VARS',
          ('Why is the block wrapped in an insulating jacket?', 2)],
  parts=[dict(title='Method: Part A — heating the aluminium block', steps=[
      'Set the metal block to **Aluminium** and the power supply to **12 V**. Tick **Insulating jacket** and **Drop of oil in the thermometer hole**.',
      'Set **Total time** to **10 min** and **Clock speed** to **×30**.',
      ('Press **Switch on and start timing**. A reading is taken every minute.', 'Copy each reading into Table 1 as it appears.'),
      ('Calculate the energy transferred for each row: E = V × I × t.', 't must be in seconds.')],
     tables=[dict(caption='Table 1: heating 1.00 kg of aluminium', cols=['Time t / s', 'Temperature / °C', 'p.d. V / V', 'Current I / A', 'Energy E / J'],
                  rows=[[t] for t in range(0, 601, 60)])]),
   dict(title='Method: Part B — without the insulation', steps=[
      ('Press **Reset**. Untick the jacket and the oil. Keep aluminium and 12 V. Run for 10 minutes again.', 'Only the insulation has changed.'),
      'Record the start temperature and the temperature at 600 s in Table 2.'],
     tables=[dict(caption='Table 2: effect of insulation', cols=['Run', 'Start / °C', 'At 600 s / °C', 'Rise / °C'],
                  rows=[['Jacket and oil'], ['No jacket, no oil']], widths=[34, 22, 22, 22])])],
  graph_steps=['Plot temperature (y-axis) against energy transferred (x-axis) from Table 1.',
               'Draw a line of best fit through the straight part of the graph.'],
  graphs=[dict(title='Temperature against energy transferred', h=150)],
  analysis=[('Find the gradient of your line: gradient = change in temperature ÷ change in energy. Show the triangle on your graph.', 2),
            ('Calculate the specific heat capacity: c = 1 ÷ (gradient × mass). The mass is 1.00 kg.', 2),
            ('The accepted value for aluminium is 900 J/kg °C. Calculate the percentage difference: (your value − 900) ÷ 900 × 100.', 2)],
  questions=[('Is your value higher or lower than 900 J/kg °C? Explain why.', 3),
             ('Use Table 2. How did the jacket and oil change the temperature rise? Explain why.', 3),
             ('Why do you use only the straight part of the graph to find the gradient?', 2),
             ('Suggest one way to make the real experiment more accurate.', 2)]),

 dict(num=2, slug='rp02-thermal-insulation', title='Thermal insulation', lab='Thermal insulation',
  aim='To find out which material is the best thermal insulator, and how the number of layers affects the rate of cooling.',
  before=['VARS',
          ('Predict which material will be the best insulator. Give a reason.', 2)],
  parts=[dict(title='Method: Part A — different materials', steps=[
      'Choose **None (control)** and **1** layer. Tick **Cardboard lid on the beaker**.',
      'Set **Read every** to **1 minute**, **Total time** to **10 min** and **Clock speed** to **×60**.',
      ('Press **Pour hot water**, then **Start stopwatch**. Copy the temperature every 2 minutes into Table 1.', 'Readings appear on screen every minute.'),
      'Press **Reset** and repeat for **Newspaper**, **Bubble wrap**, **Cotton wool** and **Felt**.',
      'Work out the temperature drop for each material: start temperature − temperature at 10 min.'],
     tables=[dict(caption='Table 1: temperature of the water / °C', cols=['Time / min', 'None', 'Newspaper', 'Bubble wrap', 'Cotton wool', 'Felt'],
                  rows=[[t] for t in (0, 2, 4, 6, 8, 10)] + [['Drop / °C']])]),
   dict(title='Method: Part B — number of layers', steps=[
      'Choose **Newspaper**. Find the temperature drop in 10 minutes for 1, 2, 3 and 4 layers.'],
     tables=[dict(caption='Table 2: layers of newspaper', cols=['Number of layers', 'Start / °C', 'At 10 min / °C', 'Drop / °C'],
                  rows=[[1], [2], [3], [4]], widths=[28, 24, 24, 24])])],
  graph_steps=['Plot temperature (y-axis) against time (x-axis) for **None** and for your **best material**. Use a different symbol for each, and add a key.',
               'Draw a smooth curve through each set of points.'],
  graphs=[dict(title='Temperature of the water against time', h=140)],
  analysis=[('Rank the five materials from best to worst insulator.', 1),
            ('Calculate the mean rate of cooling for the control: drop ÷ 10 minutes. Give the unit.', 2)],
  questions=[('Which material was the best insulator? Use your results to explain.', 2),
             ('Describe how the number of layers affected the temperature drop.', 2),
             ('Why did you use a cardboard lid on every run?', 2),
             ('Use your graph: why does the water cool fastest at the start?', 2),
             ('Why did you do a run with no insulation?', 1)]),

 dict(num=3, comb=15, slug='rp03-resistance', title='Resistance', lab='Resistance',
  aim='To investigate how the length of a wire affects its resistance, and to find the resistance of resistors in series and in parallel.',
  before=[('Complete the sentence: the ammeter is connected in ............ with the wire, and the voltmeter is connected in ............ with the wire.', 1),
          'VARS',
          ('Predict what will happen to the resistance if you double the length of the wire.', 1)],
  parts=[dict(title='Method: Part A — length of wire', steps=[
      'Choose **Length of wire** and **Constantan 0.32 mm**.',
      ('Set the length between the clips to **10 cm**. Press **Close the switch**, then **Record reading**. Open the switch again.', 'Opening the switch between readings stops the wire heating up.'),
      'Copy the p.d. and current into Table 1 and calculate R = V ÷ I.',
      'Repeat for lengths up to 100 cm.'],
     tables=[dict(caption='Table 1: resistance of the wire', cols=['Length / cm', 'p.d. V / V', 'Current I / A', 'Resistance R / Ω'],
                  rows=[[l] for l in range(10, 101, 10)])]),
   dict(title='Method: Part B — series and parallel', steps=[
      'Choose **Series and parallel**. Set **R₁ = 10 Ω** and **R₂ = 22 Ω**.',
      'For each arrangement in Table 2, close the switch, record V and I, then open the switch. Calculate R.'],
     tables=[dict(caption='Table 2: resistors in series and parallel', cols=['Arrangement', 'p.d. V / V', 'Current I / A', 'Resistance R / Ω'],
                  rows=[['R₁ only'], ['R₂ only'], ['Series'], ['Parallel']])])],
  graph_steps=['Plot resistance (y-axis) against length (x-axis) from Table 1. Draw a line of best fit.'],
  graphs=[dict(title='Resistance against length of wire', h=140)],
  analysis=[('Use your graph to find the resistance of 75 cm of wire. Show the reading on the graph.', 1),
            ('Calculate the gradient of your line. Give the unit.', 2)],
  questions=[('Describe the relationship between the resistance and the length of the wire.', 2),
             ('Compare the total resistance in series with R₁ + R₂.', 2),
             ('Explain why the total resistance in parallel is less than either resistor on its own.', 2),
             ('Suggest why a line of best fit for a real wire might not pass through the origin.', 2)]),

 dict(num=4, comb=16, slug='rp04-iv-characteristics', title='I–V characteristics', lab='I–V characteristics',
  aim='To find how the current through a fixed resistor, a filament lamp and a diode depends on the potential difference across it.',
  before=[('Which meter measures the potential difference, and how is it connected?', 1),
          ('Sketch the shape you expect for the I–V graph of a fixed resistor.', 0, '<div style="height:32mm;border:1px dashed #9fb0c0;width:60mm"></div>'),
          ('Why does the supply need to be reversed during the experiment?', 1)],
  parts=[dict(title='Method: Part A — fixed resistor and filament lamp', steps=[
      'Choose **Fixed resistor**. Set the supply to each value in Table 1, read the voltmeter and ammeter, and press **Record reading**.',
      ('For the negative values, tick **Reverse the supply connections**.', 'Untick it again for the positive values.'),
      'Choose **Filament lamp** and repeat.'],
     tables=[dict(caption='Table 1: fixed resistor and filament lamp', cols=['Supply setting / V', 'Resistor: V / V', 'Resistor: I / A', 'Lamp: V / V', 'Lamp: I / A'],
                  rows=[[v] for v in ('−6', '−4', '−2', '0', '1', '2', '3', '4', '6')])]),
   dict(title='Method: Part C — diode', steps=[
      ('Choose **Diode** and repeat for the settings in Table 2.', 'Take more readings near 0.5–1 V, where the current starts to flow.')],
     tables=[dict(caption='Table 2: diode', cols=['Supply setting / V', 'p.d. V / V', 'Current I / A'],
                  rows=[[v] for v in ('−6', '−3', '0', '0.5', '0.75', '1.0', '1.5', '2', '4', '6')], widths=[34, 33, 33])])],
  graph_steps=['Draw the axes through the middle of the grid, so you can plot negative values.',
               'Plot current (y-axis) against p.d. (x-axis) for all three components. Use a different symbol for each, and add a key.'],
  graphs=[dict(title='Current against potential difference', h=160)],
  analysis=[('Use Table 1 to calculate the resistance of the lamp at 2 V and at 6 V.', 2)],
  questions=[('Describe the I–V graph for the fixed resistor. What does it tell you about its resistance?', 2),
             ('Explain the shape of the graph for the filament lamp.', 3),
             ('Describe how the current through the diode changes as the p.d. goes from −6 V to +6 V.', 3),
             ('Why does the real diode circuit need a protective resistor in series?', 2)]),

 dict(num=5, comb=17, slug='rp05-density', title='Density', lab='Density',
  aim='To find the density of regular solids, irregular solids and liquids.',
  before=[('Write the equation that links density, mass and volume.', 1),
          ('How can you find the volume of an irregular object, such as a pebble?', 2)],
  parts=[dict(title='Method: Part A — regular solids', steps=[
      'Choose **Regular solid** and **Aluminium block**. Follow the numbered steps on screen: mass, then length, width and height.',
      'Record the readings in Table 1. Calculate volume = length × width × height, then density = mass ÷ volume.',
      'Press **Start this sample again** and repeat for the **Oak block** and the **Brass block**.'],
     tables=[dict(caption='Table 1: regular solids', cols=['Block', 'Mass / g', 'Length / cm', 'Width / cm', 'Height / cm', 'Volume / cm³', 'Density / g/cm³'],
                  rows=[['Aluminium'], ['Oak'], ['Brass']])]),
   dict(title='Method: Part B — irregular solids', steps=[
      ('Choose **Irregular solid**. For the **Pebble**, **Steel bolt** and **Modelling clay**, follow the steps on screen and record the mass and the volume of water collected.', 'Read the measuring cylinder at eye level, from the bottom of the meniscus.')],
     tables=[dict(caption='Table 2: irregular solids', cols=['Object', 'Mass / g', 'Volume / cm³', 'Density / g/cm³'],
                  rows=[['Pebble'], ['Steel bolt'], ['Modelling clay']])]),
   dict(title='Method: Part C — liquids', steps=[
      'Choose **Liquid** and set the volume to pour to **50 cm³**. For each liquid, follow the steps on screen and record the mass.'],
     tables=[dict(caption='Table 3: liquids (50 cm³ each)', cols=['Liquid', 'Mass / g', 'Volume / cm³', 'Density / g/cm³'],
                  rows=[['Water', '', '50'], ['Salt solution', '', '50'], ['Cooking oil', '', '50'], ['Ethanol', '', '50']])])],
  analysis=[('Convert the density of the aluminium block to kg/m³ (multiply by 1000).', 1)],
  questions=[('Which of your solids and liquids would float on water? Explain how you can tell.', 2),
             ('Why must the eureka can be filled until water drips from the spout before you lower the object in?', 2),
             ('Why are calipers better than a ruler for measuring the blocks?', 2),
             ('Suggest why pouring 100 cm³ of liquid gives a more accurate density than pouring 20 cm³.', 2)]),

 dict(num=6, comb=18, slug='rp06-force-and-extension', title='Force and extension', lab='Force and extension',
  aim='To investigate how the extension of a spring depends on the force acting on it.',
  before=[('Calculate the weight of a 100 g mass. Use W = m × g, where g = 9.8 N/kg.', 1),
          'VARS'],
  parts=[dict(title='Method: Part A — spring A', steps=[
      'Choose **Spring A (soft)**. With no load, record the pointer reading in Table 1.',
      ('Press **+ 100 g**. Wait for the spring to stop bouncing, then press **Record reading** and copy the reading.', 'Read the pointer at eye level, using the magnified view.'),
      'Keep adding 100 g up to 800 g.',
      'Calculate the force (W = m × g) and the extension (reading − starting reading).'],
     tables=[dict(caption='Table 1: spring A', cols=['Mass / g', 'Force / N', 'Pointer reading / cm', 'Extension / cm'],
                  rows=[[m] for m in range(0, 801, 100)])],
     note='Remove all the masses. Does the pointer go back to its starting reading? ...........................................'),
   dict(title='Method: Part B — spring B', steps=[
      'Press **Replace with a new spring** and choose **Spring B (stiff)**. Repeat for the masses in Table 2.'],
     tables=[dict(caption='Table 2: spring B', cols=['Mass / g', 'Force / N', 'Pointer reading / cm', 'Extension / cm'],
                  rows=[[m] for m in (0, 200, 400, 600, 800)])])],
  graph_steps=['Plot force (y-axis) against extension (x-axis) for both springs, with a key. Draw a line of best fit for each.'],
  graphs=[dict(title='Force against extension', h=150)],
  analysis=[('Calculate the spring constant of spring A: k = force ÷ extension. Use a point on the straight part and convert the extension to metres.', 2),
            ('Calculate the elastic potential energy stored in spring A at an extension of your choice: Eₑ = ½ k e².', 2)],
  questions=[('Describe your graph for spring A. Does it show that force is directly proportional to extension? Explain.', 3),
             ('Which spring is stiffer? How can you tell from the graph?', 2),
             ('If a line curves at the top, what has happened to the spring?', 2),
             ('Why must you read the pointer at eye level?', 1)]),

 dict(num=7, comb=19, slug='rp07-acceleration', title='Acceleration', lab='Acceleration',
  aim='To investigate how the acceleration of a trolley depends on the force acting on it, and on its mass.',
  before=[('Write the equation that links resultant force, mass and acceleration.', 1),
          'VARS'],
  parts=[dict(title='Method: Part A — varying the force', steps=[
      'Choose **Vary the force**. Tick **Runway tilted to compensate for friction**.',
      ('Set **Masses on the hanger** to **1**. Press **Release the trolley**. Copy the times at gate 1 (t₁), gate 2 (t₂) and between the gates (t₁₂).', 'The other masses ride on the trolley, so the total mass stays 0.600 kg.'),
      'Repeat for 2, 3, 4 and 5 masses on the hanger.',
      ('Calculate v₁ = 0.050 ÷ t₁, v₂ = 0.050 ÷ t₂ and a = (v₂ − v₁) ÷ t₁₂.', 'The card on the trolley is 5.0 cm (0.050 m) long.')],
     tables=[dict(caption='Table 1: varying the force (total mass 0.600 kg)', cols=['Masses on hanger', 'Force / N', 't₁ / s', 't₂ / s', 't₁₂ / s', 'v₁ / m/s', 'v₂ / m/s', 'a / m/s²'],
                  rows=[[1, '0.196'], [2, '0.392'], [3, '0.588'], [4, '0.784'], [5, '0.980']])]),
   dict(title='Method: Part B — varying the mass', steps=[
      ('Choose **Vary the mass**. For each extra mass in Table 2, release the trolley and copy the acceleration from the results on screen.', 'The hanger keeps 3 × 20 g, so the force stays 0.588 N.'),
      'Calculate 1 ÷ mass for each row.'],
     tables=[dict(caption='Table 2: varying the mass (force 0.588 N)', cols=['Extra mass / g', 'Total mass / kg', 'a / m/s²', '1 ÷ mass / kg⁻¹'],
                  rows=[[0, '0.560'], [250, '0.810'], [500, '1.060'], [750, '1.310'], [1000, '1.560']])])],
  graph_steps=['On Graph A, plot acceleration (y-axis) against force (x-axis) from Table 1. Draw a line of best fit.',
               'On Graph B, plot acceleration (y-axis) against 1 ÷ mass (x-axis) from Table 2. Draw a line of best fit.'],
  graphs=[dict(title='Graph A: acceleration against force', h=105), dict(title='Graph B: acceleration against 1 ÷ mass', h=105)],
  questions=[('Describe the relationship between acceleration and force shown by Graph A.', 2),
             ('Describe how the acceleration changed as the mass increased.', 2),
             ('Why was the runway tilted slightly?', 2),
             ('In Part A, why were the masses moved from the trolley to the hanger, rather than new masses added?', 2),
             ('Give one advantage of using light gates instead of a stopwatch.', 2)]),

 dict(num=8, comb=20, slug='rp08-waves', title='Waves', lab='Waves',
  aim='To measure the frequency, wavelength and speed of waves in a ripple tank and on a string.',
  before=[('Write the wave equation. Give the unit of each quantity.', 2),
          ('Why is it better to measure across ten waves and divide by ten, than to measure one wave?', 2)],
  parts=[dict(title='Method: Part A — ripple tank', steps=[
      'Choose **Ripple tank**. Set the frequency to **6 Hz**.',
      ('Press **Freeze the pattern**. Drag the two orange markers onto bright lines, as far apart as you can. Count the whole waves between them and press **Record**.', 'Each gap between two bright lines is one wave.'),
      'Copy the distance and the number of waves into Table 1. Calculate λ = distance ÷ waves, then v = f × λ.',
      'Repeat for the other frequencies in Table 1.'],
     tables=[dict(caption='Table 1: ripple tank', cols=['Frequency f / Hz', 'Distance / cm', 'Number of waves', 'Wavelength λ / cm', 'Speed v / m/s'],
                  rows=[[f] for f in (6, 10, 15, 20, 25)])]),
   dict(title='Method: Part B — waves on a string', steps=[
      'Choose **Waves on a string** and a hanging mass of **200 g**. The vibrating length is 1.00 m.',
      ('Change the frequency until you see a clear standing wave, then press **Record**. Count the loops.', 'Each loop is half a wavelength.'),
      'Find three different patterns (different numbers of loops). Calculate λ = 2 × 1.00 m ÷ number of loops, then v = f × λ.'],
     tables=[dict(caption='Table 2: waves on a string (200 g)', cols=['Number of loops', 'Frequency f / Hz', 'Wavelength λ / m', 'Speed v / m/s'],
                  rows=[[], [], []])])],
  analysis=[('Calculate the mean wave speed in the ripple tank.', 1),
            ('Calculate the mean wave speed on the string.', 1)],
  questions=[('Describe what happened to the wavelength in the ripple tank as the frequency increased.', 2),
             ('Did the wave speed in the ripple tank change with frequency? Use your results.', 2),
             ('Why does freezing the pattern (taking a photo) make the wavelength easier to measure?', 2),
             ('Explain why the string gives the same wave speed for each pattern.', 2)]),

 dict(num=9, slug='rp09-reflection-and-refraction', title='Reflection and refraction', lab='Reflection and refraction',
  aim='To investigate how light is reflected by different surfaces, and refracted by different substances.',
  before=[('Draw the normal at P with a dashed line. Label the angle of incidence i and the angle of refraction r.', 0, RAY_SVG),
          ('Why are the angles measured from the normal and not from the surface?', 1),
          'VARS'],
  parts=[dict(title='Method: Part A — refraction by a glass block', steps=[
      'Choose **Refraction** and **Glass block**. Tick **Show the protractor**.',
      ('Set the angle of incidence to **20°**. Press **Record angles** and copy the angle of refraction into Trial 1.', 'Read the angle from the normal.'),
      'Repeat for each angle in Table 1.',
      'Go through the angles again for Trial 2. Calculate the mean.'],
     tables=[dict(caption='Table 1: refraction by glass', cols=['Angle of incidence i / °', 'r / ° Trial 1', 'r / ° Trial 2', 'Mean r / °'],
                  rows=[[a] for a in (20, 30, 40, 50, 60, 70)])],
     note='At i = 0° the ray ...............................................................................................'),
   dict(title='Method: Part B — different substances', steps=[
      'Change the substance to **Perspex block**, then **Water in a clear box**. Record r at 20°, 40° and 60°.'],
     tables=[dict(caption='Table 2: angle of refraction / °', cols=['Angle of incidence i / °', 'Glass (mean, Table 1)', 'Perspex', 'Water'],
                  rows=[[20], [40], [60]])]),
   dict(title='Method: Part C — reflection', steps=[
      'Choose **Reflection** and **Plane mirror**. Record the angle of reflection for each angle in Table 3.',
      'Change the surface to **White card**, then **Crinkled foil**. Describe what you see.'],
     tables=[dict(caption='Table 3: plane mirror', cols=['Angle of incidence / °', '20', '40', '60'],
                  rows=[['Angle of reflection / °']], widths=[40, 20, 20, 20])],
     note='White card and crinkled foil: ...............................................................................................')],
  graph_steps=['Plot the mean angle of refraction (y-axis) against the angle of incidence (x-axis) for glass. Include (0, 0). Draw a smooth line of best fit.'],
  graphs=[dict(title='Angle of refraction against angle of incidence (glass)', h=140)],
  analysis=[('Use your graph to find the angle of refraction when i = 45°. Show the reading on the graph.', 1)],
  questions=[('Describe how the angle of refraction changes as the angle of incidence increases.', 2),
             ('Which substance changed the direction of the light the most? How can you tell from Table 2?', 2),
             ('Explain why light bends towards the normal when it enters the glass block.', 2),
             ('[HT] Use the idea of wave fronts to explain why light changes direction when it slows down.', 3),
             ('Why was there one clear reflected ray from the mirror, but not from the white card?', 2)]),

 dict(num=10, comb=21, slug='rp10-infrared-radiation', title='Infrared radiation', lab='Infrared radiation',
  aim='To investigate how the type of surface affects the amount of infrared radiation it emits.',
  before=['VARS',
          ('Predict which surface will emit the most infrared radiation, and which the least.', 2)],
  parts=[dict(title='Method: Part A — four surfaces', steps=[
      'Press **Fill with hot water**. Set the distance from the detector to **10 cm**.',
      'Choose **Matt black**. Press **Record reading** and copy the detector reading into Trial 1.',
      ('Repeat for **Shiny black**, **Matt white** and **Shiny silver**.', 'Work quickly, so the water temperature hardly changes.'),
      'Go through the four surfaces again for Trial 2. Calculate the mean.'],
     tables=[dict(caption='Table 1: detector reading / mV (distance 10 cm)', cols=['Surface', 'Trial 1', 'Trial 2', 'Mean'],
                  rows=[['Matt black'], ['Shiny black'], ['Matt white'], ['Shiny silver']])]),
   dict(title='Method: Part B — distance', steps=[
      'Choose **Matt black**. Record the reading at each distance in Table 2.'],
     tables=[dict(caption='Table 2: matt black surface', cols=['Distance / cm', '5', '10', '15', '20'],
                  rows=[['Reading / mV']], widths=[32, 17, 17, 17, 17])])],
  graph_steps=['Draw a bar chart of the mean reading for each surface from Table 1. Label both axes.'],
  graphs=[dict(title='Mean detector reading for each surface', h=120)],
  questions=[('Rank the surfaces from best to worst emitter of infrared radiation.', 1),
             ('Why must the distance be the same for every surface?', 2),
             ('Why do you take the four readings quickly?', 2),
             ('Describe how the reading changed with distance in Part B.', 2),
             ('Suggest why the pipes on the back of a fridge are painted matt black.', 2)]),
]

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, 'sheet.css'), 'w').write(CSS)
    for s in SHEETS:
        open(os.path.join(OUT, s['slug'] + '.html'), 'w').write(sheet(s))
    print(len(SHEETS), 'sheets written to', os.path.normpath(OUT))
