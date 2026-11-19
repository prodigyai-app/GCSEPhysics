# GCSE Physics diagram library

105 GCSE Physics diagrams and 71 animations from the prodigyai GCSE Physics site.

- **56 realistic figures** drawn by the shared figure library (`science-figures.js`, `science-figures-2.js`, `gcse-figures.js`), exported by `export.py`.
- **49 lesson figures, circuit symbols and exam-question figures** taken from the lesson and exam-paper pages, exported by `export-site-figures.cjs`.
- **71 animations** in `animations/`: 61 lesson simulations and 10 required practical labs, exported by `export-animations.cjs`.

Open `index.html` to browse the diagrams, and `animations/index.html` for the animations.

| Folder | Contents |
|---|---|
| `svg/` | Scalable vector files on a white background. They stay sharp at any size, and PowerPoint can convert them to editable shapes (Insert ▸ Pictures, then right-click ▸ Convert to Shape). |
| `png-light/` | 2× PNG images on white, for slides, worksheets and printing. |
| `png-dark/` | 2× PNG images on a dark background, for dark slide templates. |
| `diagrams.json` | The list of diagrams: file name, topic, description, and either the figure options used or the page it came from. |
| `animations/` | One self-contained HTML file per animation, plus `animations.json` and a browsing page. |

File names start with the topic (energy, particle, electricity, magnetism, atomic, forces, waves, space, practical, exam-paper).

## Using an animation in a lesson

Each animation is a single HTML file with everything it needs inside it, so it works offline. Open it in a browser to
use it on the board, or put it in a lesson page with an iframe:

```html
<iframe src="animations/wa1-watching-a-wave-pass.html" style="width:100%;height:640px;border:0" title="Watching a wave pass"></iframe>
```

They open in the light theme; add `?theme=dark` to the address for the dark theme. Readings in the practical labs are not saved
between visits (there is no sign-in or notebook in the standalone files).

## KS3 heat transfer animations

`animations/ks3/` holds three interactive models from the KS3 Science site (Year 9 Heating and cooling), useful for
recapping before GCSE energy transfers: `ks3-conduction-along-a-rod.html`, `ks3-convection-currents.html` and
`ks3-infrared-radiation.html`. They are single offline HTML files like the others. Rebuild them from the KS3Science repo
with `node scripts/export_models.cjs`.

## Diagrams

- **Energy**: Cutaway house: loft and cavity wall insulation, double glazing, draught excluder (`energy-house-insulation`)
- **Energy**: Heating curve: melting and boiling plateaus (`energy-heating-curve`)
- **Energy**: Kinetic and gravitational potential energy on a roller coaster (`energy-ke-gpe`)
- **Energy**: Energy stored in a stretched spring: the area under the force–extension graph (`energy-elastic-potential-energy`)
- **Energy**: Power ratings of appliances, kilowatt-hours and the cost of electricity (`energy-power-and-energy-bills`)
- **Energy**: Renewable and non-renewable energy resources (`energy-resources`)
- **Energy**: The seven energy stores and the four transfer pathways. (`energy-the-seven-energy-stores-and-the-four`)
- **Energy**: In a Sankey diagram the width of each arrow is proportional to the energy. (`energy-in-a-sankey-diagram-the-width-of`)
- **Electricity**: Inside a UK three-pin plug (`electricity-three-pin-plug`)
- **Electricity**: The National Grid (`electricity-national-grid`)
- **Electricity**: Series and parallel circuits with ammeters and voltmeter (`electricity-series-parallel`)
- **Electricity**: Alternating and direct p.d. traces (`electricity-ac-dc`)
- **Electricity**: Electrical power in a circuit: ammeter and voltmeter readings, P = VI, P = I²R and E = Pt (`electricity-power-in-circuits`)
- **Electricity**: Rubbing moves electrons from one insulator to the other. (`electricity-rubbing-moves-electrons-from-one-insulator-to`)
- **Circuit symbols**: Circuit symbol: Cell (`electricity-symbol-cell`)
- **Circuit symbols**: Circuit symbol: Battery (`electricity-symbol-battery`)
- **Circuit symbols**: Circuit symbol: Switch (open) (`electricity-symbol-switch-open`)
- **Circuit symbols**: Circuit symbol: Switch (closed) (`electricity-symbol-switch-closed`)
- **Circuit symbols**: Circuit symbol: Lamp (`electricity-symbol-lamp`)
- **Circuit symbols**: Circuit symbol: Resistor (`electricity-symbol-resistor`)
- **Circuit symbols**: Circuit symbol: Variable resistor (`electricity-symbol-variable-resistor`)
- **Circuit symbols**: Circuit symbol: Fuse (`electricity-symbol-fuse`)
- **Circuit symbols**: Circuit symbol: Diode (`electricity-symbol-diode`)
- **Circuit symbols**: Circuit symbol: LED (`electricity-symbol-led`)
- **Circuit symbols**: Circuit symbol: Thermistor (`electricity-symbol-thermistor`)
- **Circuit symbols**: Circuit symbol: LDR (`electricity-symbol-ldr`)
- **Circuit symbols**: Circuit symbol: Ammeter (`electricity-symbol-ammeter`)
- **Circuit symbols**: Circuit symbol: Voltmeter (`electricity-symbol-voltmeter`)
- **Particle model**: Particles in solids, liquids and gases (`particle-model-states-of-matter`)
- **Particle model**: Gas particles and pressure at two temperatures (`particle-gas-pressure`)
- **Particle model**: Pressure and volume of a gas: Boyle’s law apparatus and a graph of pressure against 1 ÷ volume (`particle-boyles-law`)
- **Atomic structure**: Lithium atom: nucleus, protons, neutrons, electron shells (`atomic-atom-lithium`)
- **Atomic structure**: Carbon-12 atom (`atomic-atom-carbon`)
- **Atomic structure**: Sodium atom (2,8,1) (`atomic-atom-sodium`)
- **Atomic structure**: Isotopes: carbon-12 and carbon-14 (`atomic-isotopes-carbon`)
- **Atomic structure**: Plum pudding, nuclear and Bohr models (`atomic-models-of-the-atom`)
- **Atomic structure**: Alpha, beta and gamma penetration (`atomic-radiation-penetration`)
- **Atomic structure**: Nuclear fission chain reaction (`atomic-nuclear-fission`)
- **Atomic structure**: Alpha and beta decay equations (`atomic-nuclear-equations`)
- **Atomic structure**: Irradiation and contamination (`atomic-irradiation-contamination`)
- **Atomic structure**: Half-life read from a decay curve: activity halves every half-life (`atomic-half-life-curve`)
- **Atomic structure**: Read the half-life from the time taken to fall to half of any starting value. (`atomic-read-the-half-life-from-the-time`)
- **Atomic structure**: Fission of uranium-235 after absorbing a neutron. (`atomic-fission-of-uranium-235-after-absorbing-a`)
- **Forces**: Thinking and braking distances at 30, 50 and 70 mph (`forces-stopping-distances`)
- **Forces**: Resultant force from balanced and unbalanced forces (`forces-resultant-force`)
- **Forces**: Spring extension and Hooke's law graph (`forces-spring-hookes-law`)
- **Forces**: Distance-time graph: speed from the gradient (`forces-distance-time-graph`)
- **Forces**: Pressure increases with depth in a liquid (`forces-liquid-pressure`)
- **Forces**: Scalars and vectors (`forces-scalars-vectors`)
- **Forces**: Conservation of momentum in a collision (`forces-momentum-collision`)
- **Forces**: Mass and weight: the same 60 kg mass on Earth and on the Moon (`forces-mass-and-weight`)
- **Forces**: Work done: a force moving an object through a distance (`forces-work-done`)
- **Forces**: A small gear driving a large gear: lower speed, larger moment. (`forces-a-small-gear-driving-a-large-gear`)
- **Forces**: A skydiver reaches terminal velocity; opening the parachute increases the drag, giving a lower terminal velocity. (`forces-a-skydiver-reaches-terminal-velocity-opening-the`)
- **Waves**: Transverse and longitudinal waves (`waves-transverse-longitudinal`)
- **Waves**: The electromagnetic spectrum and uses (`waves-electromagnetic-spectrum`)
- **Waves**: Refraction through a glass block (`waves-refraction-glass-block`)
- **Waves**: Convex and concave lens ray diagrams (`waves-convex-concave-lenses`)
- **Waves**: Prism, filters and coloured objects (`waves-colour-filters`)
- **Waves**: Uses and hazards of each part of the electromagnetic spectrum (`waves-uses-of-em-waves`)
- **Waves**: Seismic waves through the Earth. (`waves-seismic-waves-through-the-earth`)
- **Magnetism**: Step-up transformer (`magnetism-transformer-step-up`)
- **Magnetism**: Step-down transformer (`magnetism-transformer-step-down`)
- **Magnetism**: Field patterns of a bar magnet and a solenoid (`magnetism-field-magnet-solenoid`)
- **Magnetism**: Magnetic field around a current-carrying wire (`magnetism-field-around-wire`)
- **Magnetism**: Electromagnetic induction (`magnetism-induction`)
- **Magnetism**: Fleming’s left-hand rule. (`magnetism-flemings-left-hand-rule`)
- **Magnetism**: A moving-coil loudspeaker. (`magnetism-a-moving-coil-loudspeaker`)
- **Space physics**: Life cycle of a star (`space-life-cycle-of-a-star`)
- **Space physics**: Circular orbit: gravity provides the centripetal force (`space-orbits`)
- **Space physics**: Our solar system: the Sun, planets and their orbits (`space-solar-system`)
- **Space physics**: As the universe expands, all distant galaxies move further apart. (`space-as-the-universe-expands-all-distant-galaxies`)
- **Required practicals**: Specific heat capacity: heater and thermometer in an insulated aluminium block (`practical-specific-heat-capacity`)
- **Required practicals**: Thermal insulation: beakers wrapped in different materials, with cooling curves (`practical-thermal-insulation`)
- **Required practicals**: Resistance of a wire: metre rule, crocodile clip, ammeter and voltmeter (`practical-resistance-of-a-wire`)
- **Required practicals**: I–V characteristics: circuit and graphs for a resistor, filament lamp and diode (`practical-iv-characteristics`)
- **Required practicals**: Density: regular block on a balance and an irregular object in a eureka can (`practical-density`)
- **Required practicals**: Acceleration: trolley, light gates, pulley and hanging masses (`practical-acceleration`)
- **Required practicals**: Waves: ripple tank and a vibrating string (`practical-waves`)
- **Required practicals**: Infrared radiation: Leslie cube and infrared detector (`practical-infrared-leslie-cube`)
- **Required practicals**: Specific latent heat of fusion: heater in crushed ice with a control funnel (`practical-specific-latent-heat`)
- **Exam question figures**: Exam question figure (Elastic potential energy): The graph shows how the force on a rubber band changes with its extension. (`energy-exam-question-the-graph-shows-how-the-force-on`)
- **Exam question figures**: Exam question figure (Resistance and V = IR): The diagram shows a circuit used to find the resistance R of a resistor. (`electricity-exam-question-the-diagram-shows-a-circuit-used-to`)
- **Exam question figures**: Exam question figure (Internal energy and changes of state): The graph shows how the temperature of a substance changes as it cools. (`particle-exam-question-the-graph-shows-how-the-temperature-of`)
- **Exam question figures**: Exam question figure (Half-life): The graph shows how the count rate from a radioactive sample changes with time (background has been subtracted). (`atomic-exam-question-the-graph-shows-how-the-count-rate`)
- **Exam question figures**: Exam question figure (Forces and elasticity): The graph shows force against extension for a different spring. (`forces-exam-question-the-graph-shows-force-against-extension-for`)
- **Exam question figures**: Exam question figure (Speed and distance–time graphs): The distance–time graph shows a short walk. (`forces-exam-question-the-distance-time-graph-shows-a-short`)
- **Exam question figures**: Exam question figure (Acceleration and velocity–time graphs): The velocity–time graph shows a train leaving a station. (`forces-exam-question-the-velocity-time-graph-shows-a-train`)
- **Exam question figures**: Exam question figure (Set 1 · Paper 1 (Higher tier)): A student investigated how the current in a filament lamp depends on the potential difference across it. (`exam-paper-pp11-a-student-investigated-how-the-current-in`)
- **Exam question figures**: Exam question figure (Set 1 · Paper 1 (Higher tier)): Polonium-210 is radioactive and decays by emitting alpha particles. (`exam-paper-pp11-polonium-210-is-radioactive-and-decays-by`)
- **Exam question figures**: Exam question figure (Set 1 · Paper 1 (Higher tier)): Figure 5 shows a circuit used as a temperature sensor. (`exam-paper-pp11-figure-5-shows-a-circuit-used-as`)
- **Exam question figures**: Exam question figure (Set 1 · Paper 2 (Higher tier)): A student investigated how the extension of a spring depends on the force applied to it. She hung the spring from a clamp and added weights one at a time. (`exam-paper-pp12-a-student-investigated-how-the-extension-of`)
- **Exam question figures**: Exam question figure (Set 1 · Paper 2 (Higher tier)): Figure 2 shows a velocity–time graph for a cyclist. (`exam-paper-pp12-figure-2-shows-a-velocity-time-graph`)
- **Exam question figures**: Exam question figure (Set 2 · Paper 1 (Higher tier)): A student heated 0.40 kg of solid wax with a 150 W heater. Figure 1 shows how the temperature of the wax changed. (`exam-paper-pp21-a-student-heated-0-40-kg-of`)
- **Exam question figures**: Exam question figure (Set 2 · Paper 1 (Higher tier)): Figure 4 shows two lamps connected in parallel to a 12 V battery. The current in lamp A is 2.0 A and the current in lamp B is 0.50 A. (`exam-paper-pp21-figure-4-shows-two-lamps-connected-in`)
- **Exam question figures**: Exam question figure (Set 2 · Paper 2 (Higher tier)): A boy walks to a bus stop, waits, and then runs to catch the bus. Figure 1 shows the distance–time graph for his journey. (`exam-paper-pp22-a-boy-walks-to-a-bus-stop`)
- **Exam question figures**: Exam question figure (Set 3 · Paper 1 (Higher tier)): A student investigated how the current in a component depends on the potential difference across it. (`exam-paper-pp31-a-student-investigated-how-the-current-in`)
- **Exam question figures**: Exam question figure (Set 3 · Paper 2 (Higher tier)): A student drops a steel sphere of mass 0.050 kg into a tall tube of oil. Figure 1 shows how the velocity of the sphere changes as it falls through the oil. (`exam-paper-pp32-a-student-drops-a-steel-sphere-of`)
- **Exam question figures**: Exam question figure (Foundation Set 1 · Paper 1): Figure 1 shows a series circuit. (`exam-paper-pf11-figure-1-shows-a-series-circuit`)
- **Exam question figures**: Exam question figure (Foundation Set 1 · Paper 2): Figure 1 shows the distance–time graph for a car. (`exam-paper-pf12-figure-1-shows-the-distance-time-graph`)
- **Exam question figures**: Exam question figure (Foundation Set 2 · Paper 1): A student measured the current in a resistor for different potential differences. Figure 1 shows the results. (`exam-paper-pf21-a-student-measured-the-current-in-a`)
- **Exam question figures**: Exam question figure (Foundation Set 2 · Paper 1): A student heated a tube of stearic acid until it melted, then let it cool. Figure 2 shows how the temperature of the stearic acid changed as it cooled. (`exam-paper-pf21-a-student-heated-a-tube-of-stearic`)
- **Exam question figures**: Exam question figure (Foundation Set 2 · Paper 2): Figure 1 shows a velocity–time graph for a bus between two stops. (`exam-paper-pf22-figure-1-shows-a-velocity-time-graph`)
- **Exam question figures**: Exam question figure (Foundation Set 3 · Paper 1): Figure 1 shows two lamps, X and Y, connected in parallel. The current in lamp X is 0.40 A and the current in lamp Y is 0.20 A. (`exam-paper-pf31-figure-1-shows-two-lamps-x-and`)
- **Exam question figures**: Exam question figure (Foundation Set 3 · Paper 1): Uranium-238 (23892U) decays by emitting an alpha particle to form thorium. (`exam-paper-pf31-uranium-238-23892u-decays-by-emitting-an`)

## Making more or changing one

The diagrams are drawn by code, so a change made in the figure library can be re-exported for every diagram at once
(`export.py`, needs Python with Playwright). Figures accept options, for example a different element for the atom
(`{"Z": 19}` for potassium) or the number of turns on each transformer coil (`{"np": 10, "ns": 2}`).

To refresh everything after the site changes, serve the repos folder (`python3 -m http.server 8800` from the folder
that contains `GCSEPhysics`), then from the repo root run:

```
python3 diagram-library/export.py                 # realistic figures
node diagram-library/export-site-figures.cjs      # lesson figures, circuit symbols, exam-question figures
node diagram-library/export-animations.cjs        # animations
node diagram-library/build-index.cjs              # browsing pages and this README's list
```
