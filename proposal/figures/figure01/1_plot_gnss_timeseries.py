"""
Plot the vertical position GNSS time-series data for Askja.

:copyright:
    2023, Conor A. Bacon
:license:
    CC0 1.0 Universal License
    (https://creativecommons.org/publicdomain/zero/1.0/legalcode)

"""

from datetime import datetime as dt
import pathlib

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import obspy
import pandas as pd


plt.style.use("../basic_style.mplstyle")
mpl.rcParams["font.family"] = "Helvetica"

repo_base = pathlib.Path.cwd().parents[1]
data_dir = repo_base / "data" / "gnss"
data_dir.mkdir(parents=True, exist_ok=True)

starttime = obspy.UTCDateTime("2021-08-01")
stations = ["DYNG", "TANC", "JONC", "KASC", "OLAC"]
clrs = iter(
    plt.cm.magma(
        np.linspace(0, len(stations), len(stations) + 1) % len(stations) / len(stations)
    )
)

fig, ax = plt.subplots(1, 1, figsize=(7, 3), layout="constrained")
for station, clr in zip(stations, clrs):
    ts = pd.read_csv(
        data_dir / f"{station}_timeseries.txt", sep=r"\s+"
    )

    ts["utcdatetime"] = ts.apply(
        lambda row: obspy.UTCDateTime(f"{row['#yyyy/mm/dd']}T{row['HH:MM:SS.SSS']}"),
        axis=1,
    )

    ts = ts[ts["utcdatetime"] > starttime]

    zero_point = ts["dU[mm]"].values[0]
    (_, caps, _) = ax.errorbar(
        [t.datetime for t in ts["utcdatetime"]],
        [(t - zero_point) / 10 for t in ts["dU[mm]"].values],
        yerr=ts["DU[mm]"] / 10,
        label=station,
        fmt="s",
        markersize=1.2,
        color=clr,
        ecolor="k",
        elinewidth=0.2,
        capsize=2,
    )

    for cap in caps:
        cap.set_markeredgewidth(0.2)

ax.set_ylabel("Up, cm")
ax.set_xlim([dt(year=2021, month=9, day=1), dt.now()])
ax.set_xlabel("Date")
plt.legend()
plt.savefig("figure01.png", dpi=400)
