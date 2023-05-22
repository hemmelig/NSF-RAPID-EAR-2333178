---
mainfont: Arial
fontsize: 10pt
geometry: letterpaper, margin=1in
output: pdf_document
---
\pagenumbering{gobble}

## DATA MANAGEMENT PLAN

All data recorded as part of this RAPID proposal will be freely and openly available via field-standard portals.

### Magnetometer network
The magnetometer network will be registered with the FDSN (international Federation of Digital Seismograph Networks), which will provide in return a Digital Object Identifier for the network data and metadata. The FDSN also provides field-standard definitions of data formats, including:

- The Standard for the Exchange of Earthquake Data (SEED) data file format, as well as the commonly used miniSEED file format.
- FDSN Source Identifiers, which define the construction of unique identifiers for data sources.
- The FDSN StationXML Schema, which specifies a baseline for magnetometric metadata.

Data recorded by the LEMI-039 3-component magnetometers are initially stored as ASCII-text files. Data from these files will be extracted and converted to the field-standard miniSEED file format. Streams for each component will be recorded at 1 Hz, with timestamps provided by a GPS-corrected clock.

** Statement from Joe regarding the data recorded by the low-cost devices. Will be broadly similar to the above statement for the LEMI-039 fluxgate magnetometers

All data will be assessed for quality, including the quality of the timing clock, before being submitted to the EarthScope Data Management Center for permanent archival. The EarthScope DMC provides web-API endpoints (after the FDSN web service specifications) for querying and downloading these data.

### Aerial magnetic surveys
Data recorded as part of the aerial magnetic surveys will be compiled into a repository and archived via a service (e.g. Zenodo) that will assign the data a Digital Object Identifier, making these data will be openly available and citable.
