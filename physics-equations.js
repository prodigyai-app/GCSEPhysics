/* Formula summary checked against AQA 8463, June 2027 equation sheet.
   Higher-only entries follow the HT markers on that sheet. */
(function(root){
  "use strict";
  const officialURL="https://www.aqa.org.uk/filestore/physics/AQA-GCSE-Science-8463-INS-AI-V2.3.pdf";
  const rows=[
    ["Kinetic energy","E<sub>k</sub> = ½mv²"],
    ["Elastic potential energy","E<sub>e</sub> = ½ke²"],
    ["Gravitational potential energy","E<sub>p</sub> = mgh"],
    ["Thermal energy change","ΔE = mcΔθ"],
    ["Power from energy","P = E/t"],
    ["Power from work done","P = W/t"],
    ["Efficiency from energy","efficiency = useful energy output / total energy input"],
    ["Efficiency from power","efficiency = useful power output / total power input"],
    ["Charge flow","Q = It"],
    ["Potential difference","V = IR"],
    ["Electrical power","P = VI"],
    ["Heating in a resistor","P = I²R"],
    ["Energy from power","E = Pt"],
    ["Energy from charge","E = QV"],
    ["Density","ρ = m/V"],
    ["Energy for a change of state","E = mL"],
    ["Gas at constant temperature","pV = constant"],
    ["Weight","W = mg"],
    ["Work done along the force","W = Fs"],
    ["Spring force","F = ke"],
    ["Moment; d is the perpendicular distance","M = Fd"],
    ["Pressure on a surface","p = F/A"],
    ["Pressure due to a column of liquid","p = hρg",1],
    ["Distance at constant speed","s = vt"],
    ["Acceleration","a = Δv/t"],
    ["Uniform acceleration","v² − u² = 2as"],
    ["Resultant force","F = ma"],
    ["Momentum","p = mv",1],
    ["Force and change of momentum","F = mΔv/Δt",1],
    ["Wave period","T = 1/f"],
    ["Wave speed","v = fλ"],
    ["Magnification","magnification = image height / object height"],
    ["Wire perpendicular to a magnetic field","F = BIl",1],
    ["Transformer turns and voltage","V<sub>p</sub>/V<sub>s</sub> = n<sub>p</sub>/n<sub>s</sub>",1],
    ["Ideal transformer power","V<sub>p</sub>I<sub>p</sub> = V<sub>s</sub>I<sub>s</sub>",1]
  ];
  const api={rows,officialURL};
  if(typeof module!=="undefined"&&module.exports)module.exports=api;
  else root.PhysicsEquations=api;
})(typeof window!=="undefined"?window:globalThis);
