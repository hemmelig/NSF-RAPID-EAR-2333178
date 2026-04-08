---
mainfont: Arial
fontsize: 10pt
geometry: letterpaper, margin=1in
output: pdf_document
---
\pagenumbering{gobble}

# Summary of Lemi-424 Field Performance, Askja 2023–2025

## Field team

- 2025: Conor Bacon (Columbia University), Elisa Piispa (University of Iceland), Nyla Rechtyzgiel (University of Wyoming), Alexander Cortese (University of Wyoming)
- 2024: Conor Bacon (Columbia University), Joe Biasi (University of Wyoming), Elisa Piispa (University of Iceland), Nyla Rechtzygiel (incoming University of Wyoming)
- 2023: Conor Bacon (Columbia University), Evelyn Powell (Columbia University), Elisa Piispa (University of Iceland)

## Overview

As part of the NSF funded project "Collaborative Research: RAPID: A novel magnetometer network to capture the ongoing inflationary episode at Askja volcano, Iceland" (ID: 2333178), 6 Lemi magnetometer units (comprising a Lemi-424 datalogger and a Lemi-039 3-component fluxgate magnetometer) were deployed in and around the Askja volcano caldera (Figure 1). The objectives of this project were two-fold:

- to measure changes in the local magnetic field that could be associated with changes to the subsurface magma storage system, indicated by ongoing inflation seen in GNSS observations;
- and to compare the performance of the Lemi systems (hereafter described as 'fine-resolution' magnetometers) with a low-cost alternative being developed by project co-PI Joe Biasi (hereafter described as 'coarse-resolution' magnetometers). One such device was co-located with each Lemi system.

![***Top:** Existing networks and deployed magnetometer sites within Askja caldera. **Bottom:** Full map of existing networks and deployed magnetometer network. Access roads (red lines) and the central Askja volcanic system (dashed black line) are highlighted.*](figures/field-summary/map.png){ width=350px }

Modelling of the different potential scenarios driving the inflationary episode that started in August 2021 suggest that variations in the local magnetic field could be on the order of 10s to 100s of nanoTesla, which is well above the resolution of the Lemi systems.

The experiment also offered an opportunity to test the performance of the Lemi systems for long-term monitoring deployments, as opposed to the more typical campaign-style deployments as part of magnetotelluric surveys. The initial field deployment took place in August 2023, with our first site visit to recover data and fix any issues in July 2024. The network of instruments was recovered in August 2025. Our power system followed the design settled on after 15+ years of experience deploying long-term, but non-permanent, seismic stations in the Icelandic highlands, consisting of a wooden solar panel stand, a single 100 W flexible solar panel mounted on a rigid wood backing board, and 3 100 Ah deep-cycle AGM (Absorbent Glass Mat) batteries in a plastic box—see Figure 2. The battery box also housed the Lemi datalogger and the solar charge controller, while simultaneously serving as a weight to hold the solar panel stand in place. The typical rule of thumb is that a single 100 Ah battery can provide 1 W for 1 month, so 3 batteries gives us 3 months of power (assuming the system consumes 1 W). We actually found the system was able to run for 8 months with no charge input, suggesting the combined datalogger and fluxgate system only consumed around 0.4 W, which is inline with the values provided in the system documentation. Below we include a picture of the power infrastructure for one of the sites.

![*The power system as seen at OLFM (Ólafsgígar, in the centre of the caldera). Panels **a** and **b** show the front and back of the panel stand, as it is left during the year. Panel **c** shows the inside of the battery box, with the batteries outlined in blue, the Lemi datalogger outlined in pink, and the solar charge controller outlined in green. The solar panel and GPS antenna cables exit the box in the right-hand side (when facing the back of the panel), while the instrument cable exist the box on the left-hand side, without any coiling.*](figures/field-summary/site-example.png)

## Data recovery

In total, we recovered approximately 90% of the potential data, with the majority lost at the three stations inside/nearest to the caldera, which were covered by snow earlier in the year, and were uncovered later. Further, data from RIFM in the second year were only recorded up to June 2025, as the SD card had filled up. Figure 3 shows a summary of the data availability. We note a number of gaps of a handful of days across all of the sites, which do not appear to be consistent (except two gaps in OLFM and KAFM in February 2024). Another indication that these are not power-related gaps is the fact that these gaps are full days, suggesting an issue with the datalogger firmware is more likely, e.g., it failed to initialise the file or there was an issue writing the final file to SD storage.

In the following breakdown, the number of potential recording days is calculated from the deployment and recovery dates.

- DYFM: 668 days / 738 total = 90.51 %
- KAFM: 599 days / 734 total = 81.61 %
- MOFM: 681 days / 732 total = 93.03 %
- OLFM: 655 days / 708 total = 92.51 %
- RIFM: 624 days / 734 total = 85.01 %
- STFM: 691 days / 729 total = 94.79 %
  
This gives an overall recovery of: 3918 days / 4375 total = 89.55 %

One suggestion for future long-term experiments is that the low-voltage disconnect, and the reconnect voltage, could both be lowered to improve data recovery. The minimum input voltage for the system is 5 V, so even lowering the LVD from 11.4 V to ~11 V and the reconnect voltage from 11.8 V to 11.5 V would likely lead to few-to-no data gaps from power outages.

The GPS timing at the MOFM station failed on March 2, 2025, with new data being timestamped from 0000-00-00 00:00:00.0. On inspection, the data after this time appeared to be ok and just had to be time corrected. This was done by assuming the data continued recording with no offset, which was verified by comparing the data recorded across the network during large geomagnetic storms. These storms cause changes in the geomagnetic field that would occur simultaneously across the small footprint of the network. After time correction, the peaks of these storms recorded at MOFM correspond in time with those same peaks recorded at the other stations in the network. 

The final data archive was manually cleaned, with some data around the site visits being removed due to being contaminated by our presence. A complete log of data that were removed from the archive has been retained.

![*Data availability overview for the fine-resolution magnetometers. The relative thickness and colour of the bar indicates the data availability (with gaps indicating a complete lack of data for the given day).*](figures/field-summary/askja-mag-availability-plot.png)

## Data overview

Below we show overviews of the data recorded on the instruments. We observe a correlation between temperature (at the fluxgate sensor) and the recorded magnetic field strengths, which we will need to correct prior to analysis. Temperatures stabilise while the ground is frozen and snow insulates the surface.

Aero-mag surveys were conducted using a MagArrow system (a Caesium vapour absolute magnetometer capable of sampling at 1000 Hz), with hand samples collected at each site in order to properly characterise the settings for each deployment site. When conditions were not appropriate for flights, walking surveys were conducted with a GEM GSM-19T proton magnetometer. A number of benchmarks established for geodetic (campaign GPS and gravimetry) surveys were also surveyed with the GSM-19T magnetometer in order to look for year-on-year changes.

In the following data summaries (Figures 4–9), the panels show the following, from top to bottom:

- the X-component of the magnetic field (i.e., north-south)
- the Y-component of the magnetic field (i.e., east-west)
- the Z-component of the magnetic field (i.e., vertical, positive-down)
- the absolute field
- the temperatures as measured by the probes inside the datalogger and the fluxgate instrument
- the voltage as measured by the datalogger

Of note is the fact that the two stations situated inside the caldera proper (OLFM and KAFM) exhibit a significantly lower absolute field strength than those outside. By using the absolute magnetometer in the MagArrow, which is less sensitive to strong magnetic gradients, we found the gradient of the field at ground level to be very strong inside the caldera. While earlier aeromagnetic surveys suggest a lower field inside the caldera, it is likely the gradient that is behind the low field values measured by the fluxgates. Many of the strong geomagnetic storms were also recorded across the network, such as the Ganon storm on May 10–11, 2024, which are evident across all of the sites as high-amplitude deviations from the background field, on the order of 500–1000 nT.

![*Overview of the data recorded at DYFM.*](figures/field-summary/DYFM-1d-summary.png){ width=600px }

![*Overview of the data recorded at KAFM.*](figures/field-summary/KAFM-1d-summary.png){ width=600px }

![*Overview of the data recorded at MOFM.*](figures/field-summary/MOFM-1d-summary.png){ width=600px }

![*Overview of the data recorded at OLFM.*](figures/field-summary/OLFM-1d-summary.png){ width=600px }

![*Overview of the data recorded at RIFM.*](figures/field-summary/RIFM-1d-summary.png){ width=600px }

![*Overview of the data recorded at STFM.*](figures/field-summary/STFM-1d-summary.png){ width=600px }
