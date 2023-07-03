---
mainfont: Arial
fontsize: 10pt
geometry: letterpaper, margin=1in
output: pdf_document
---
\pagenumbering{gobble}

## Collaborative Research: RAPID: A novel magnetometer network to capture the ongoing inflationary episode at Askja volcano, Iceland

We propose to study the ongoing unrest at Askja volcano, Iceland, using a novel network of magnetometers. Askja has been inflating since August 2021 and is well on its way to reversing over 40 years of cumulative subsidence, suggesting recharge of the shallow magmatic storage system beneath Askja caldera as the system primes itself for the next eruption. In August 2023, we will deploy a network of continuous, 3-component magnetometers to measure the time evolution of the subsurface magmatic system. Changes in the distribution of magma should produce observable changes to the local magnetic field, which these instruments will measure. This novel technique is based on recent modeling by Biasi et al. (2022) and a successful deployment at Axial Seamount (Fluegel et al. 2022). The proposed network will complement the existing continuous seismic and geodetic networks (Fig. 1), as well as benchmarks used for campaign gravimetry surveys. We will combine 6 high-sensitivity LEMI-039 fluxgate magnetometers, similar to those that we successfully deployed in Alaska in 2022, with a large number (~15) of experimental, low-cost devices to densify coverage.

In addition to the instrument network, we will collaborate with Elisa Piispa at Háskoli Íslands to conduct aeromagnetic surveys of the caldera using a Matrice 600 drone with an attached survey magnetometer. Taking such a survey during the deployment and retrieval of the network will provide us with a high-resolution spatial map of the caldera to benchmark and calibrate the data recorded at the continuous network, as well as providing a reference field in the case of an eruption. These surveys may also have some value for mapping historical eruption domains within the caldera.

![*Time-series data showing the evolution of the vertical position of GNSS stations deployed within Askja caldera, since August 2021. Uplift values are relative to the first vertical position value on or after August 1, 2021, for each station. Colors correspond to station colors in Fig 2. Data courtesy of Veðurstofan.*](../figures/figure01/figure01.png)

Askja is a well-instrumented volcanic system in the Northern Volcanic Zone of Iceland. A number of geophysical methods have been employed to map out the subsurface magmatic system (e.g. Sturkell & Sigmundsson, 2000; de Zeeuw-van Dalfsen et al., 2012; Greenfield et al., 2016; Drouin et al., 2017; Bacon et al., 2022). However, the mechanism driving the current inflation is ill-constrained despite the available geodetic (GNSS and InSAR) and gravimetric data. As shown by Biasi et al. (2022) and Fluegel et al. (2022), magnetometry is sensitive to subsurface movements of magma because molten and therefore unmagnetized rock displaces or demagnetizes through heating pre-existing magnetized rocks within the plumbing system. Net inflation or significant mass changes, sensed by geodesy and gravimetry, may or may not occur in the same places or at the same times as these demagnetization events. Hence, our proposed project will provide complementary information to help constrain subsurface changes, and also serve as a landmark case study of the potential for magnetometry to illuminate otherwise latent processes in subsurface magmatic systems, to track their evolution, and to identify eruption precursors. The existing networks of seismic and geodetic instruments are shown in Figure 2.

![***Top:** Existing networks and proposed sites within Askja caldera. **Bottom:** Full map of existing networks and proposed magnetometer network. Access roads (red lines) and the central Askja volcanic system (dashed black line) are highlighted.*](../figures/figure02/figure02.png){ width=580px }

### Science questions
This project will address several open questions in volcanology, including:

- Can changes in the crustal magnetic field constrain changes in subsurface magmatic systems?
- How does the time-series evolution of the magnetic field compare to other geophysical observations?
- Can low-cost instruments (<$250/unit) be used to improve spatial sampling, with less financial risk, without compromising our ability to resolve the geophysical signals of interest?

### Instrumentation
We will use two complementary sets of magnetometers to populate the instrument network. One set consists of 6 high-end LEMI-039 fluxgate magnetometers, which will be borrowed from the EarthScope Primary Instrument Center (EPIC, previously PASSCAL) at no cost to the project. These high-sensitivity systems have a long track record of use in magnetotelluric applications, and PI Bacon has previously deployed a similar system at the remote Cleveland and Okmok volcanoes in the Aleutians. The necessary equipment for the auxiliary power infrastructure (solar panels, solar power controllers, batteries, etc.) will be purchased in Iceland or rented from EPIC.

The second set of magnetometers consists of ~15 low-cost instruments (<$250 per unit). This experimental instrument cluster will be used to densify coverage and determine if low-cost data collection with magnetometers is possible. Preliminary models of the Askja system suggest that this is the case (Figure 3). Each instrument consists of a magnetometer, microprocessor, SD card, battery, solar panel, case, and various other components. Some systems will be equipped with satellite connectivity for continuous data transmission. A variety of components from different manufacturers will be used to determine which components can withstand the cold, wet conditions of Iceland. Low-cost instruments that withstand a year of exposure here will be usable on the majority of volcanoes worldwide.

To be clear, only the high-end LEMI magnetometers are necessary to accomplish the science goals of this project. Data from the low-cost magnetometers would be a valuable addition, but if most of these instruments fail or are unable to detect a meaningful signal the LEMI data will be sufficient. The LEMI instrument’s history of success in volcanological applications gives us high confidence that these systems will withstand a year of field deployment at Askja.

### Modeling and data analysis

The time evolution of the local magnetic field is an under-explored geophysical signal at volcanic systems. Magnetic lows are commonly observed at volcanic centers; these are attributed to the presence of magma or hydrothermal systems (Jónsson & Kristjánsson, 2000). Before and during deployment, we will model different scenarios for changes in the magmatic system at Askja (Fig. 3) to explore their effect on the local magnetic field. After data collection, we will construct inversion models of the magnetic data to constrain the subsurface magma geometry and better understand inflationary (or possibly eruptive) episodes in caldera systems. All modeling will be done with SimPEG, which is a free and open-source program that can incorporate magnetic, gravity, and geodetic data into unified forward and inverse models (Cockett et al., 2017; Heagy et al., 2017). This will allow us to cross-reference our novel dataset with more established geophysical techniques that are currently being used at Askja.


### Broader impacts

This deployment will pave the way towards a new, powerful tool for studying the evolution of magmatic systems both during crises and times of repose. Magnetometers are significantly less expensive than other potential field sensors such as gravimeters. A technique that is as powerful as gravimetry, but can be done at a fraction of the cost, will significantly improve a government’s ability to monitor volcanoes and potentially forecast eruptions. Widespread adoption of this method would disproportionately benefit developing nations with high volcanic risk and low geoscience budgets (Philippines, D.R. Congo, etc.). The low-cost magnetometers are made with off-the-shelf components. The plans, code, and parts list will be made open-source and publicly available. With sufficient interest, the low-cost magnetometers could be mass-produced for <$100. At this price point, they can be widely deployed and used as a first line of defense in volcanically active areas. Their data would also be useful as a way to determine how other instruments should be allocated and where they should be deployed on a volcano. The success of this project could bring high-quality volcanic risk-mitigation to all.

![*Magnetic models of Askja, showing how even small changes to the magmatic system are detectable. **A–D**: Block models (based on Greenfield et al., 2016) illustrating pre-eruptive or inflationary scenarios. Insets show magma geometries in more detail. Modeled magma volume in C/D is 0.04 km<sup>3</sup>, c. 2% of the 1875 eruptive volume (Hartley & Thordarson, 2012). **E–F**: Magnetic difference maps showing changes to the local field compared to the initial conditions. Dark colored areas are above the detection limit for the low-cost magnetometers; all changes are detectable by standard magnetometers. Changes to the hydrothermal system are not modeled here, but would enhance the signal (Biasi et al. 2022).*](../figures/figure03/figure03.png)

### International Collaboration

Fieldwork will be coordinated with the Cambridge Volcano Seismology group, led by Prof. Nick Rawlinson, and colleagues at Háskoli Íslands (Bryndís Brandsdóttir, Dr Elisa Piispa, and Sveinbjörn Steinþórsson). This team has decades of invaluable experience working in and around Iceland’s volcanic systems, particularly Askja. We will also work with Elisa Piispa (Háskoli Íslands) to conduct aerial magnetic surveys of the caldera during the network deployment and recovery, in order to benchmark the continuous data.

### Field safety

Contact with the Icelandic Meteorological Office will be maintained to communicate the current state of activity at Askja. A full field risk assessment will be conducted prior to the deployment and recovery efforts, based on prior experience of PI Bacon working in and around Askja. Communication when working inside Askja caldera will be maintained via a Garmin InReach device, which uses the Iridium satellite constellation. In the event of increased unrest or an eruption, we would evacuate the Highlands to reassess. Should Askja erupt prior to the proposed fieldwork, we will coordinate with the Civil Protection and Emergency working group to collect in-situ magnetic field measurements to study the evolution of the magmatic system (and lava flows) during an eruption, should conditions allow.

### Data sharing

All continuous magnetic field data will be made openly available via the EarthScope DMC. We will register the network with the International Federation of Digital Seismograph Networks (FDSN) organization, which accepts magnetic field data. This will provide a citable DOI for the network and the data. Drone-based field survey data and modeling results will be made available via Zenodo. All analysis code written or used for this project will be made available via a GitHub repository, which will be registered with Zenodo to provide a citable DOI.

### Why RAPID?

It is critical to collect field data during the precursory phase to provide insight into how magmatic systems evolve in the buildup to an eruption. However, such precursory data is often difficult to obtain, because many volcanic systems do not show clear evidence of unrest for a long-enough period of time for instruments to be deployed. Askja may be the exception to this rule and thus presents an excellent opportunity to characterize the restless (pre-eruptive?) state of this caldera-forming system.

This active period of uplift at Askja may develop into an eruption or may end at any time, making this data collection activity time sensitive. The typical NSF review timeline of multiple months may be too long to allow us to capture these transient precursory signals. In addition, access to the Iceland Highlands is time-sensitive due to weather conditions and arrival of snow to Askja (typically around mid-September). Given these factors, we believe that the RAPID program is appropriate for this proposal.
