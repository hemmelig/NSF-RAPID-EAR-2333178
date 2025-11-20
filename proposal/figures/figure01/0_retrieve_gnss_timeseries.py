"""
Request GNSS time-series data from the IMO webserver.

:copyright:
    2023, Conor A. Bacon
:license:
    CC0 1.0 Universal License
    (https://creativecommons.org/publicdomain/zero/1.0/legalcode)

"""

import pathlib

import pandas as pd
import requests


repo_base = pathlib.Path.cwd().parents[1]
data_dir = repo_base / "data" / "gnss"
data_dir.mkdir(parents=True, exist_ok=True)

# Read in GNSS network (of interest)
gnss_network = pd.read_csv(
    repo_base / "metadata/instruments/gnss_network_22-23.txt",
    sep=r"\s+",
    header=None,
)

for _, station in gnss_network.iterrows():
    station_code = station[0]
    print(f"Requesting GNSS time-series data for {station_code}...")
    r = requests.get(
        f"http://brunnur.vedur.is/gps/timeseries/timeseries/{station_code}-plate.NEU"
    )
    print("    ...success, writing to file...")
    with (data_dir / f"{station_code}_timeseries.txt").open("wb") as f:
        f.write(r.content)
    print("...complete!\n")
