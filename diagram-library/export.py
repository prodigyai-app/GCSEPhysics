import asyncio,json,re
from playwright.async_api import async_playwright
import os
HERE=os.path.dirname(os.path.abspath(__file__))
C=os.path.join(HERE,'..','..','ALevelPhysics','platform','client')+'/'; OUT=HERE+'/'
FIGS=[
 ('energy-house-insulation','house',{},'Energy','Cutaway house: loft and cavity wall insulation, double glazing, draught excluder'),
 ('particle-model-states-of-matter','states',{'level':'gcse'},'Particle model','Particles in solids, liquids and gases'),
 ('particle-gas-pressure','gasPressure',{},'Particle model','Gas particles and pressure at two temperatures'),
 ('electricity-three-pin-plug','plug',{},'Electricity','Inside a UK three-pin plug'),
 ('electricity-national-grid','grid',{},'Electricity','The National Grid'),
 ('magnetism-transformer-step-up','transformer',{'np':6,'ns':12},'Magnetism','Step-up transformer'),
 ('magnetism-transformer-step-down','transformer',{'np':12,'ns':6},'Magnetism','Step-down transformer'),
 ('magnetism-field-magnet-solenoid','magField',{},'Magnetism','Field patterns of a bar magnet and a solenoid'),
 ('atomic-atom-lithium','atom',{'Z':3,'level':'gcse'},'Atomic structure','Lithium atom: nucleus, protons, neutrons, electron shells'),
 ('atomic-atom-carbon','atom',{'Z':6,'level':'gcse'},'Atomic structure','Carbon-12 atom'),
 ('atomic-atom-sodium','atom',{'Z':11,'level':'gcse'},'Atomic structure','Sodium atom (2,8,1)'),
 ('atomic-isotopes-carbon','isotopes',{'Z':6,'masses':[12,14],'level':'gcse'},'Atomic structure','Isotopes: carbon-12 and carbon-14'),
 ('atomic-models-of-the-atom','atomModels',{'level':'gcse'},'Atomic structure','Plum pudding, nuclear and Bohr models'),
 ('atomic-radiation-penetration','penetration',{},'Atomic structure','Alpha, beta and gamma penetration'),
 ('forces-stopping-distances','stopping',{},'Forces','Thinking and braking distances at 30, 50 and 70 mph'),
 ('waves-transverse-longitudinal','waves',{},'Waves','Transverse and longitudinal waves'),
 ('waves-electromagnetic-spectrum','emSpectrum',{},'Waves','The electromagnetic spectrum and uses'),
 ('waves-refraction-glass-block','glassBlock',{},'Waves','Refraction through a glass block'),
 ('waves-convex-concave-lenses','lenses',{},'Waves','Convex and concave lens ray diagrams'),
 ('space-life-cycle-of-a-star','starLife',{},'Space physics','Life cycle of a star'),
]
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1700,'height':1200},device_scale_factor=2)
    await pg.set_content('<html><body style="margin:0"></body></html>')
    for f in ['science-figures.js','science-figures-2.js']: await pg.add_script_tag(path=C+f)
    meta=[]
    for name,fig,o,topic,desc in FIGS:
      for theme,bg,ink,panel in [('light','#ffffff','#1d2733','#ffffff'),('dark','#0f1620','#e8ecf5','#0f1620')]:
        svg=await pg.evaluate("""([fig,o,bg,ink,panel])=>{let s=SciFig.svg(fig,o);
          s=s.replace(/<rect class="sf-blank"[^>]*\\/>/g,'').replace(/<circle class="sf-(ring|hit)"[^>]*\\/>/g,'')
           .replace(/var\\(--panel,#121a33\\)/g,panel).replace(/var\\(--ink,#e8ecf5\\)/g,ink).replace(/currentColor/g,ink)
           .replace(/class="sf-lab"/g,'class="sf-lab" fill="'+ink+'"').replace(/fill:#ffd0b0/g,bg==='#ffffff'?'fill:#c0392b':'fill:#ffd0b0').replace(/<g class="sf-(lbl|q)"[^>]*>/g,'<g>');
          // one svg (isotopes returns two side by side): wrap into a single svg
          if(s.startsWith('<div')){const parts=[...s.matchAll(/<svg[^>]*viewBox="0 0 (\\d+) (\\d+)"[^>]*>([\\s\\S]*?)<\\/svg>/g)];let x=0,H=0,inner='';for(const p of parts){inner+=`<svg x="${x}" y="0" width="${p[1]}" height="${p[2]}" viewBox="0 0 ${p[1]} ${p[2]}">${p[3]}</svg>`;x+=+p[1]+20;H=Math.max(H,+p[2]);}s=`<svg viewBox="0 0 ${x-20} ${H}" role="img">${inner}</svg>`;}
          const vb=s.match(/viewBox="([-\\d.]+) ([-\\d.]+) ([\\d.]+) ([\\d.]+)"/);
          s=s.replace(/^<svg([^>]*)>/,(m,a)=>`<svg xmlns="http://www.w3.org/2000/svg"${a.replace(/ class="[^"]*"/,'').replace(/ style="[^"]*"/,'')} width="${vb[3]}" height="${vb[4]}" font-family="Arial, Helvetica, sans-serif" color="${ink}"><rect x="${vb[1]}" y="${vb[2]}" width="${vb[3]}" height="${vb[4]}" fill="${bg}"/>`);
          return s}""",[fig,o,bg,ink,panel])
        if theme=='light': open(OUT+'svg/'+name+'.svg','w').write('<?xml version="1.0" encoding="UTF-8"?>\n'+svg)
        await pg.evaluate("s=>{document.body.innerHTML='<div id=w style=\"display:inline-block\">'+s+'</div>'}",svg)
        el=await pg.query_selector('#w svg'); await el.screenshot(path=OUT+f'png-{theme}/{name}.png')
      meta.append({'file':name,'figure':fig,'options':o,'topic':topic,'description':desc})
    json.dump(meta,open(OUT+'diagrams.json','w'),indent=1)
    await b.close(); print(len(meta),'diagrams')
asyncio.run(m())
