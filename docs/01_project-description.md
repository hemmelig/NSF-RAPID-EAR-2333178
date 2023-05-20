---
mainfont: Arial
fontsize: 10pt
geometry: letterpaper, margin=1in
output: pdf_document
---
\pagenumbering{gobble}

## Collaborative Research: RAPID: A novel magnetometer network to capture the ongoing inflationary episode at Askja volcano, Iceland

***PI: Conor A. Bacon, Lamont-Doherty Earth Observatory, Columbia University***  
***Co-PI: Joseph A. Biasi, Dartmouth College***

We propose to study the ongoing inflation at Askja volcano, Iceland, using a novel network of magnetometers. This inflation—which started in August 2021 and is well on its way to reversing over 40 years of cumulative subsidence—suggests recharge of the shallow magmatic storage system beneath Askja caldera as the system primes for the next eruption. We will deploy a network of continuous, 3-component magnetometers to measure the time evolution of the subsurface magmatic system in August 2023. Changes to the distribution of magma should produce observable changes to the local magnetic field, which these instruments will measure. This novel technique is based on recent modeling by Biasi et al. (2022) and a successful deployment at Axial Seamount (Fluegel et al. 2022). The proposed network (Fig. 1) will complement the existing continuous seismic and geodetic networks, as well as benchmarks used for campaign gravimetry surveys. We will combine 6 high-sensitivity LEMI-039 fluxgate magnetometers, similar to those which we have successfully deployed in Alaska in 2022, with a large number (~15) of experimental, low-cost devices to densify coverage.

In addition to the instrument network, we will collaborate with Elisa Piispa at Háskoli Íslands to conduct aeromagnetic surveys of the caldera using a Matrice 600 drone with an attached survey magnetometer. Taking such a survey during the deployment and retrieval of the network will provide is with a high-resolution spatial map of the caldera to benchmark and calibrate the data recorded at the continuous network, as well as providing a reference field in the case of an eruption. These surveys may also have some peripheral value for mapping historical eruption domains within the caldera.

![Time-series data showing the evolution of the vertical position of GNSS stations deployed within Askja caldera, since August 2021. Uplift values are relative to the first vertical position value on or after August 1, 2021, for each station. Colors correspond to station colors in Fig 2. Data courtesy of Veðurstofan.](../figures/figure01/figure01.png)

Askja is a well-instrumented volcanic system in the Northern Volcanic Zone of Iceland. A number of geophysical methods have been employed to map out the subsurface magmatic system (e.g. Sturkell & Sigmundsson, 2000; de Zeeuw-van Dalfsen et al., 2012; Greenfield et al., 2016; Drouin et al., 2017; Bacon et al., 2022). However, the mechanism driving the current inflation is ill-constrained despite the available geodetic (GNSS and InSAR) and gravimetric data. Our proposed project will provide complementary information to help constrain this process, and also serve as a landmark case study of the potential for magnetometry to illuminate otherwise latent processes in subsurface magmatic systems, how they evolve, and to identify eruption precursors. The existing networks of seismic and geodetic instruments are shown in Figure 2.

![**Top:**  Existing networks and proposed sites within Askja caldera. GNSS sites are coloured by the colors used in the top panel. **Bottom:** Full map of existing networks and proposed magnetometer network. Access roads (red lines) and the central Askja volcanic system (dashed black line) are highlighted.](../figures/figure02/figure02.png){ width=400px }

### Science questions
This project will address several open questions in volcanology, including:

- Can changes in the crustal magnetic field constrain changes in subsurface magmatic systems?
- How does the time-series evolution of the magnetic field compare to other geophysical observables?
- Can low-cost instruments (<$250/unit) be used to improve spatial sampling, with less financial risk, without compromising our ability to resolve the geophysical signals of interest?

### Modeling and data analysis

The time evolution of the local magnetic field is an under-explored geophysical signal at volcanic systems. Magnetic lows are commonly observed at volcanic centers, and attributed to the presence of magma or hydrothermal systems (Jónsson & Kristjánsson, 2000). Before deployment, we will model different scenarios for changes in the magmatic system at Askja (Fig. 2) to explore the effect on the local magnetic field. After data collection, we will construct inversion models of the magnetic data to constrain the subsurface magma geometry and better understand inflationary (or possibly eruptive) episodes in caldera systems. All modeling will be done with SimPEG, which can incorporate magnetic, gravity, and deformational data into unified forward and inversion models (Cockett et al., 2017; Heagy et al., 2017).

![Magnetic models of Askja, showing how even small changes to the magmatic system are detectable. A–D: Block models (based on Greenfield et al., 2016) illustrating pre-eruptive or inflationary scenarios. Insets show magma geometries in more detail. Modeled magma volume in C/D is 0.04 km3, c. 2% of the 1875 eruptive volume (Hartley & Thordarson, 2012). E–F: Magnetic difference maps showing changes to the local field compared to the initial conditions. Dark colored areas are above the detection limit for the low-cost magnetometers; all changes are detectable by standard magnetometers. Changes to the hydrothermal system are not modeled here, but would enhance the signal (Biasi et al. 2022).](../figures/figure03/figure03.png)

### Broader impacts

This deployment could pave the way towards a new, powerful tool for studying the evolution of magmatic systems both during crises and times of repose. Magnetometers are significantly less expensive than other potential field sensors such as gravimeters—widespread adoption of this method would disproportionately benefit developing nations with high volcanic risk and low monitoring budgets (Philippines, D.R. Congo, etc.). The low-cost magnetometers are made with off-the-shelf components. The plans, code, and parts list will be made publicly available.

### International Collaboration

Fieldwork will be coordinated with the Cambridge Volcano Seismology group, led by Prof. Nick Rawlinson, and colleagues at Háskoli Íslands, Bryndís Brandsdóttir & Sveinbjörn Steinþórsson. This team has decades of invaluable experience working in and around Iceland’s volcanic systems, particularly Askja. We will also work with Elisa Piispa (Háskoli Íslands) to conduct aerial magnetic surveys of the caldera during the network deployment and recovery, in order to benchmark the continuous data.

### Field safety

Contact with the Icelandic Meteorological Office will be maintained to communicate the current state of activity at Askja. In the event of increased unrest or an eruption, we would evacuate the Highlands to reassess. Should Askja erupt prior to the proposed fieldwork, we will coordinate with the Civil Protection and Emergency working group to collect in-situ magnetic field measurements to study the evolution of the magmatic system (and lava flows) during an eruption, should conditions allow.

### Data sharing

All continuous magnetic field data will be made openly available via the EarthScope DMC. We will register the network with the International Federation of Digital Seismograph Networks (FDSN) organization, which accepts magnetic field data. This will provide a citable DOI for the network and the data. Drone-based field survey data and modeling results will be made available via Zenodo. All analysis code written or used for this project will be made available via a GitHub repository, which will be registered with Zenodo to provide a citable DOI.

### Why RAPID?

It is critical to collect field data during the precursory phase to provide insight into how magmatic systems evolve in the build up to an eruption. However, such precursory data is often difficult to obtain, because many volcanic systems do not show clear evidence of unrest for a long-enough period of time for instruments to be deployed. Askja may be the exception to this rule and thus presents an excellent opportunity to characterize the restless (pre-eruptive?) state of this caldera-forming system.

This active period of uplift at Askja may develop into an eruption or may end at any time, making this data collection activity time sensitive. The typical NSF review timeline of multiple months may be too long to allow us to capture these transient precursory signals. In addition, access to the Iceland Highlands is time-sensitive due to weather conditions and arrival of snow to Askja (typically around mid-September). Given these factors, we believe that the RAPID program is appropriate for this proposal.
