# GCSE Physics diagram library

20 realistic GCSE Physics diagrams, exported from the shared figure library used on the prodigyai revision sites
(`ALevelPhysics/platform/client/science-figures.js` and `science-figures-2.js`).

Open `index.html` to browse them.

| Folder | Contents |
|---|---|
| `svg/` | Scalable vector files on a white background. They stay sharp at any size, and PowerPoint can convert them to editable shapes (Insert ▸ Pictures, then right-click ▸ Convert to Shape). |
| `png-light/` | 2× PNG images on white, for slides, worksheets and printing. |
| `png-dark/` | 2× PNG images on a dark background, for dark slide templates. |
| `diagrams.json` | The list of diagrams: file name, topic, description and the figure options used. |

File names start with the topic (energy, particle, electricity, magnetism, atomic, forces, waves, space).

## Diagrams

- **Energy**: Cutaway house: loft and cavity wall insulation, double glazing, draught excluder (`energy-house-insulation`)
- **Particle model**: Particles in solids, liquids and gases (`particle-model-states-of-matter`)
- **Particle model**: Gas particles and pressure at two temperatures (`particle-gas-pressure`)
- **Electricity**: Inside a UK three-pin plug (`electricity-three-pin-plug`)
- **Electricity**: The National Grid (`electricity-national-grid`)
- **Magnetism**: Step-up transformer (`magnetism-transformer-step-up`)
- **Magnetism**: Step-down transformer (`magnetism-transformer-step-down`)
- **Magnetism**: Field patterns of a bar magnet and a solenoid (`magnetism-field-magnet-solenoid`)
- **Atomic structure**: Lithium atom: nucleus, protons, neutrons, electron shells (`atomic-atom-lithium`)
- **Atomic structure**: Carbon-12 atom (`atomic-atom-carbon`)
- **Atomic structure**: Sodium atom (2,8,1) (`atomic-atom-sodium`)
- **Atomic structure**: Isotopes: carbon-12 and carbon-14 (`atomic-isotopes-carbon`)
- **Atomic structure**: Plum pudding, nuclear and Bohr models (`atomic-models-of-the-atom`)
- **Atomic structure**: Alpha, beta and gamma penetration (`atomic-radiation-penetration`)
- **Forces**: Thinking and braking distances at 30, 50 and 70 mph (`forces-stopping-distances`)
- **Waves**: Transverse and longitudinal waves (`waves-transverse-longitudinal`)
- **Waves**: The electromagnetic spectrum and uses (`waves-electromagnetic-spectrum`)
- **Waves**: Refraction through a glass block (`waves-refraction-glass-block`)
- **Waves**: Convex and concave lens ray diagrams (`waves-convex-concave-lenses`)
- **Space physics**: Life cycle of a star (`space-life-cycle-of-a-star`)

## Making more or changing one

The diagrams are drawn by code, so a change made in the figure library can be re-exported for every diagram at once
(`export.py`, needs Python with Playwright). Figures accept options, for example a different element for the atom
(`{"Z": 19}` for potassium) or the number of turns on each transformer coil (`{"np": 10, "ns": 2}`).
