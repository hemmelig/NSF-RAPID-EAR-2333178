Building the miniSEED archive
=============================

Read through the entire workflow before beginning, there are a number of important notes.

There are four stages to building the miniSEED waveform file from scratch:

1. Download and unzip the raw waveform recordings using the PMTK dataset fetch utility (which uses Pooch under the hood). The dataset is split into two ;
2. Process the raw ASCII files into miniSEED files;
3. Merge the two blocks into a unified archive;
4. Trim out the periods of time identified from QC as being of poor quality (mainly just the times during deployment, servicing, and recovery).

This work unit requires the following packages:

- Project Management Toolkit: https://github.com/hemmelig/pmtk
- miniSEED Archive Toolkit: https://github.com/hemmelig/miniseed-archivetk

Clone and install them in a virtual environment. I recommend using ``uv`` (see the ``pmtk`` repository for further information).

1 - Downloading the raw recordings
----------------------------------

The raw recordings can be retrieved from the Zenodo repository (https://zenodo.org/records/17965655) using the PMTK dataset fetching utility.

Note: This will download around 5.8 GB of data!

```bash
pmtk data fetch raw-recordings --all
```

Once downloaded, you will need to extract the files. They have been compressed using the free and open-source 7zip utility, and be decompressed using:

```bash
cd ../../data/external/raw-recordings
mkdir -p 2024 && 7z x -so 2024.tar.7z | tar xf - -C 2024
mkdir -p 2025 && 7z x -so 2025.tar.7z | tar xf - -C 2025
cd -
```

Note: The decompressed dataset is around 55 GB in size!

2 - Converting from ASCII to miniSEED
-------------------------------------

The ``lemi-ascii2mseed.py`` utility included in this work unit can be used to convert each file in turn as follows:

```bash
python lemi-ascii2mseed.py --station <STATION> --network 6D --input-dir ../../data/external/raw-recordings/2024 --output-dir ../../data/internal/2024/.
```

Repeat this for each station for each year. It is important not to direct the output to the same directory immediately, as there is some overlap in the output data that will be handled in the next step.

Note: There was an issue in 2025 with the timing antenna for the MOFM site. The timing antenna broke down on 2025-03-01, so a pivot date of "2025-03-02" must be supplied to correct timing. This correction was confirmed by comparing the timestamps of recordings of geomagnetic storms across the network.

```bash
python lemi-ascii2mseed.py --station MOFM --network 6D --input-dir ../../data/external/raw-recordings/2025 --output-dir ../../data/internal/2025/. --pivot 2025-03-02
```

3 - Building a unified archive
------------------------------

Once extracted, the next step is to merge these two temporary miniSEED archives into a single unified archive. This uses the ``archive-merge`` utility:

```bash
archive-merge --input-archive ../../data/internal/2024 --output-archive ../../data/internal/archive
archive-merge --input-archive ../../data/internal/2025 --output-archive ../../data/internal/archive --overwrite
```

4 - Trimming QC'd time periods from archive
-------------------------------------------

Finally, poor quality data identified by analyst QC is removed using the ``archive-clip`` utility. No data is lost, the clipped data are stored in a new archive next to the main archive:

```bash
archive-clip --config askja-mag-clip.conf
```

Note: If you want to check first what data will be clipped, you can add the ``--dry-run`` argument to the above command.

5 - Cleanup
-----------

Once you have completed all of the above, you will want to be sure to delete the raw recordings and unmerged archives, which at this point will be occupying around 100 GB!

```bash
rm -rf ../../data/external/raw-recordings/*
rm -rf ../../data/internal/202*
```

The final archive is approximately 15 GB for all 6 channels for all 6 stations.
