# Collaborative Research: RAPID: A novel magnetometer network to capture the ongoing inflationary episode at Askja volcano, Iceland

This repository brings together the code, data, and metadata used to prepare the proposal for the funded [NSF RAPID project EAR-2333178](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333178). This award is linked with [EAR-2333180](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333180).

To reproduce the documents and figures, clone this repository and navigate into the repository directory:

```
git clone https://github.com/hemmelig/NSF-RAPID-EAR-2333178
cd NSF-RAPID-EAR-2333178/proposal
```

## Steps to reproduce figures
1. Install the packages listed in the `requirements.txt` file, either manually, or using a virtual environment management system e.g. uv or conda:

```
conda create --name nsf-rapid-2333178 python=3.11
conda activate nsf-rapid-2333178
pip install -r requirements.txt
conda install -c conda-forge pygmt
```

2. Optional: Install Helvetica font for Matplotlib

3. For each figure, run the scripts in order e.g. `0_...` then `1_...`, etc using the relevant command-line directive i.e. `python` for `.py` files and `bash` for `.gmt` files.

## Steps to reproduce documents
A number of documents are built from Markdown files using `pandoc`. This can be installed by following the instructions in the `pandoc` [documentation](https://pandoc.org/installing.html). PDF documents are built using `XeLaTeX`, which provides good font control. Once `pandoc` has been installed:

1. Ensure all figures have been generated (see above).

2. Navigate to `docs` (command below assumes you are in the base directory of the repository) and run the `000_build_all.sh` shell script:

```
cd docs
bash 000_build_all.sh
```

## Notes
- Figures were prepared using macOS 12.5.1.
- DEM files used in the original proposal figures may differ from those available using this repository.
